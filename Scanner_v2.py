import socket
import threading
from datetime import datetime

# Initialize a lock for thread-safe output
print_lock = threading.Lock()

def scan_port(target, port, log_file):
    try:
        # Establish a TCP connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.5)
            if s.connect_ex((target, port)) == 0:
                # Resolve service name if possible
                try:
                    service = socket.getservbyport(port)
                except (OSError, socket.error):
                    service = "unknown"

                # Attempt banner grabbing for version identification
                try:
                    s.send(b"HEAD / HTTP/1.1\r\n\r\n")
                    banner = s.recv(1024).decode().strip()
                except Exception:
                    banner = "n/a"

                result = f"[+] {port:<5} | Service: {service:<12} | Info: {banner if banner else 'no response'}"
                
                # Sync terminal output and file logging
                with print_lock:
                    print(result)
                    with open(log_file, "a") as f:
                        f.write(f"{result}\n")
    except Exception:
        pass

def main():
    print("-" * 65)
    print("      MULTI-THREADED NETWORK AUDITOR v2.0")
    print("-" * 65)

    host = input("[?] Target Host: ")
    try:
        start_p = int(input("[?] Start Port: "))
        end_p = int(input("[?] End Port: "))
    except ValueError:
        print("[!] Invalid input. Numeric values required for ports.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    log_name = f"scan_{host}_{timestamp}.txt"

    print(f"\n[*] Target: {host}")
    print(f"[*] Report: {log_name}")
    print("=" * 65)

    worker_threads = []
    for p in range(start_p, end_p + 1):
        t = threading.Thread(target=scan_port, args=(host, p, log_name))
        worker_threads.append(t)
        t.start()

    for t in worker_threads:
        t.join()

    print("=" * 65)
    print(f"[*] Scan finalized. Results persisted to {log_name}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Process terminated by user.")
