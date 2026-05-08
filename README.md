# 🛡️ Multi-Threaded Network Auditor & Port Scanner (v5.0)

A powerful collection of Python-based security tools designed for network auditing and vulnerability assessment. This project evolves from a basic scanner to a professional-grade multi-threaded auditor with full CLI support.

## 🚀 Key Features
- **[span_0](start_span)[span_1](start_span)Multi-threaded Core:** Uses Python's `threading` library to scan hundreds of ports in seconds[span_0](end_span)[span_1](end_span).
- **[span_2](start_span)[span_3](start_span)[span_4](start_span)[span_5](start_span)Service Fingerprinting:** Automatically maps open ports to common services like SSH, HTTP, FTP, and SMTP[span_2](end_span)[span_3](end_span)[span_4](end_span)[span_5](end_span).
- **[span_6](start_span)Professional CLI:** v5.0 includes an advanced command-line interface with `-t` (target) and `-p` (port range) arguments[span_6](end_span).
- **[span_7](start_span)[span_8](start_span)[span_9](start_span)Structured Reporting:** Generates detailed `.log` files for every scan session to maintain audit trails[span_7](end_span)[span_8](end_span)[span_9](end_span).
- **[span_10](start_span)[span_11](start_span)[span_12](start_span)[span_13](start_span)Multi-Target Support:** Capable of auditing both Localhost (127.0.0.1) and Remote Targets (scanme.nmap.org)[span_10](end_span)[span_11](end_span)[span_12](end_span)[span_13](end_span).

## 📁 Project Structure
- [span_14](start_span)`Scanner.py`: The basic TCP connect scanner implementation[span_14](end_span).
- [span_15](start_span)`Scanner_v2.py`: Enhanced version with multi-threading for speed[span_15](end_span).
- [span_16](start_span)`Network_auditor.py`: Final professional auditor with CLI arguments and logging[span_16](end_span).
- [span_17](start_span)[span_18](start_span)[span_19](start_span)`Network_port_scanner.pdf`: Complete documentation of the scanning process and results[span_17](end_span)[span_18](end_span)[span_19](end_span).

## 📸 Proof of Concept (Results)

### 1. Terminal Output (v5.0 Auditor)
[span_20](start_span)[span_21](start_span)The screenshot below shows the tool identifying 19 open ports on a remote target[span_20](end_span)[span_21](end_span):
![Elite Auditor Results](1000061434.jpg)

### 2. Service Discovery (v2.0 implementation)
[span_22](start_span)Identification of specific services like FTP, Telnet, and Domain during a live scan[span_22](end_span):
![Service Discovery](1000061431.jpg)

## 🛠️ How to Run
To use the final professional auditor, use the following command format:
```bash
python3 network_auditor.py -t <target_ip> -p <port_range>
