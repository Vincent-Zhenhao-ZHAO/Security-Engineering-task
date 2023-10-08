# File descriptation:
#############################################################################################################
# Problem 1: Threat Modelling -> three questions has been answered in three files:
# 1.1: Threat Modelling - Question 1  -> Assumptions.pdf
# 1.2: Threat Modelling - Question 2  -> Attack_tree.pdf
# 1.3: Threat Modelling - Question 3  -> Risk_assessment.pdf

#############################################################################################################
# Problem 2: Certificate Authority and PKI (RC) -> two questions has been answered in two files:
# 2.1: Certificate Authority and PKI - PKI Infrastructure -> rootCA folder
# - CA's public-key Certificate: ca.crt
# - Server's public-key Certificate: server.crt
# 2.2: Man in the middle -> client.py, server.py, mitm.py, evidence
# - client.py, serer.py -> build TLS connection
# - mitm.py -> Man in the middle attack
# - evidence -> This is in folder: Evidence_for_mitm
# # - picture about processing the mitm attack,
# # - picture about finally check the ip address,
# # - picture about saved the data in the file: arper.pcap -> open in wireshark
# # - picture about arper.pcap in wireshark
# # - video about the whole process

#############################################################################################################
# Problem 3: File Integrity (RC):
# 3.1: File Integrity - Question 1 -> Signed_Files/q3.py
# 3.2: File Integrity - Question 2 -> File_integrity_report.pdf

#############################################################################################################
How to run the code:
#############################################################################################################
How to run server.py, client.py, mitm.py:
1. Ensure server.py in the machine B, client.py in the machine A, mitm.py in the machine M
2. In the machine B, run server.py: python3 /path/to/server.py [server_port] [server.crt] [server.key]
You should see: Waiting for client...
3. In the machine A, run client.py: python3 /path/to/client.py www.technowizard.com [server_port] [client.crt]
Note: You need to modify the "www.technowizard.com" to server IP address as there's no ip address in server certificate
instructions:1: On machine A, terminal: nano /etc/hosts
             2: Add the server IP address and the domain name at the last line. (www.technowizard.com)
             3: Save and exit

You should see: "Enter message: "

4. In the machine M, run mitm.py: python3 /path/to/mitm.py [victim_ip] [server_ip] [interface]
You should able to see the successful message as shown in the evidence.
If you want to quit, press "Ctrl + C" in the machine M, you should see the message: "KeyboardInterrupt"
And the data file will be saved in the same folder as mitm.py, called "arper.pcap". You can open it in wireshark.

#############################################################################################################
How to run Signed_Files/q3.py:
1. Ensure q3.py, message.txt, messageTwo.txt, public.key, signature.pem in the same folder:
2. Run q3.py: python3 q3.py
You should see the result message.
#############################################################################################################

