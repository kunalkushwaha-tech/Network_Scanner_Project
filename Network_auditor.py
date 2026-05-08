import socket
import threading
import argparse
import sys
from datetime import datetime

# Professional Colors
G = '\033[92m'  # Green
R = '\033[91m'  # Red
Y = '\033[93m'  # Yellow
B = '\033[94m'  # Blue
C = '\033[0m'   # Reset

print_lock = threading.Lock()
discovered_ports = []

def scan_port(target, port, log_file):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.2)
            if s.connect_ex((target, port)) == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                
                try:
                    s.send(b"HEAD / HTTP/1.1\r\n\r\n")
                    banner = s.recv(1024).decode().strip().replace('\n', ' ')[:40]
                except:
                    banner = "no-response"

                result = f"{G}[+]{C} {port:<7} | {service:<15} | {banner}"
                with print_lock:
                    print(result)
                    discovered_ports.append((port, service))
                    with open(log_file, "a") as f:
                        f.write(f"PORT: {port} | SERVICE: {service} | INFO: {banner}\n")
    except:
        pass

def main():
    # Command Line Arguments Setup
    parser = argparse.ArgumentParser(description="Professional Network Auditor v5.0")
    parser.add_argument("-t", "--target", help="Target Hostname or IP Address", required=True)
    parser.add_argument("-p", "--ports", help="Port Range (e.g. 20-1024)", default="1-1024")
    args = parser.parse_args()

    # ASCII Banner
    print(f"{B}{'='*65}\n      ELITE COMMAND-LINE AUDITOR v5.0\n{'='*65}{C}")

    # Resolve Target
    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"{R}[!] Error: Could not resolve {args.target}{C}")
        return

    # Parse Port Range
    try:
        start_p, end_p = map(int, args.ports.split('-'))
    except:
        print(f"{R}[!] Error: Use format 1-1000 for ports.{C}")
        return

    log_name = f"audit_{target_ip}.log"
    
    print(f"{B}[*]{C} Target: {target_ip} ({args.target})")
    print(f"{B}[*]{C} Range : {start_p} to {end_p}")
    print(f"{B}[*]{C} Report: {log_name}\n" + "-"*65)

    threads = []
    for p in range(start_p, end_p + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, p, log_name))
        threads.append(t)
        t.start()
        if threading.active_count() > 200:
            t.join()

    for t in threads:
        t.join()

    print("-" * 65 + f"\n{G}Scan Complete. {len(discovered_ports)} open ports found.{C}")

if __name__ == "__main__":
    main()
