# Project Documentation

Welcome to our project! This documentation provides an overview of the problems addressed in the project and instructions on how to execute related codes.

## 📚 Table of Contents
- [Problem Descriptions](#problem-descriptions)
  - [Threat Modelling](#threat-modelling)
  - [Certificate Authority and PKI (RC)](#certificate-authority-and-pki-rc)
  - [File Integrity (RC)](#file-integrity-rc)
  - [MITM](#execution-instructions)
- [Execution Instructions](#execution-instructions)
## Problem Descriptions

### Threat Modelling

Addressed in three files:
- `Assumptions.pdf`: Contains answers for Threat Modelling - Question 1.
- `Attack_tree.pdf`: Contains answers for Threat Modelling - Question 2.
- `Risk_assessment.pdf`: Contains answers for Threat Modelling - Question 3.

### Certificate Authority and PKI (RC)

Detailed in two parts:
- **PKI Infrastructure**:
  - Found within the `rootCA` folder.
  - Includes CA's Public-Key Certificate (`ca.crt`) and Server's Public-Key Certificate (`server.crt`).
- **Man in the Middle**:
  - Scripts: `client.py` and `server.py` (for building TLS connections), `mitm.py` (for executing the MITM attack).
  - `Evidence_for_mitm` folder contains visuals and data relevant to the MITM attack.

### File Integrity (RC)

- `Signed_Files/q3.py`: Contains script related to File Integrity - Question 1.
- `File_integrity_report.pdf`: Contains answers for File Integrity - Question 2.

## Execution Instructions

### Running TLS Connection and MITM Scripts

1. Ensure server.py in the machine B, client.py in the machine A, mitm.py in the machine M
2. In the machine B, run server.py:
   
```bash
python3 /path/to/server.py [server_port] [server.crt] [server.key]
```

You should see: 

```bash
Waiting for client...
```

4. In the machine A, run client.py:

```bash
python3 /path/to/client.py www.technowizard.com [server_port] [client.crt]
```

(Note: You need to modify the "www.technowizard.com" to server IP address as there's no ip address in server certificate)
   -  On machine A, terminal: nano /etc/hosts
   -  Add the server IP address and the domain name at the last line. (www.technowizard.com)
   -  Save and exit

You should see:

```bash
"Enter message: "
```
5. In the machine M, run mitm.py: python3 /path/to/mitm.py [victim_ip] [server_ip] [interface]
You should able to see the successful message as shown in the evidence. If you want to quit, press "Ctrl + C" in the machine M, you should see the message: "KeyboardInterrupt" And the data file will be saved in the same folder as mitm.py, called "arper.pcap". You can open it in wireshark.

[!Exmaple Video](recorded_video.gif)

### Running Signed_Files/q3.py
1. Ensure q3.py, message.txt, messageTwo.txt, public.key, signature.pem in the same folder:
2. Run q3.py:
   
```bash
python3 q3.py
```
You should see the result message.
   
