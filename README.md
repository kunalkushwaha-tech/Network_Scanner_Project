# 🛡️ Multi-Threaded Network Auditor & Port Scanner (v5.0)

A powerful collection of Python-based security tools designed for network auditing and vulnerability assessment. This project evolves from a basic scanner to a professional-grade multi-threaded auditor with full CLI support.

## 🚀 Key Features
- **Multi-threaded Core:** Uses Python's `threading` library to scan hundreds of ports in seconds.
- **Service Fingerprinting:** Automatically maps open ports to common services like SSH, HTTP, FTP, and SMTP.
- **Professional CLI:** v5.0 includes an advanced command-line interface with `-t` (target) and `-p` (port range) arguments.
- **Structured Reporting:** Generates detailed `.log` files for every scan session to maintain audit trails.
- **Multi-Target Support:** Capable of auditing both Localhost (127.0.0.1) and Remote Targets (scanme.nmap.org).

## 📁 Project Structure
- `Scanner.py`: The basic TCP connect scanner implementation.
- `Scanner_v2.py`: Enhanced version with multi-threading for speed.
- `Network_auditor.py`: Final professional auditor with CLI arguments and logging.
- `Network_port_scanner.pdf`: Complete documentation of the scanning process and results.

## 📸 Proof of Concept (Results)

### 1. Terminal Output (v5.0 Elite Auditor)
The screenshot below shows the tool identifying 19 open ports on a remote target with a structured CLI:
![Elite Auditor Results](IMG-20260508-WA0013.jpg)

### 2. Service Discovery & Mapping
Identification of specific services like FTP, Telnet, and Domain during a live multi-threaded scan:
![Service Discovery](IMG-20260508-WA0016.jpg)

## 🛠️ How to Run
To use the final professional auditor, use the following command format:
```bash
python3 network_auditor.py -t <target_ip> -p <port_range>
