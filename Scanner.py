import socket
import datetime
import threading

# Initialize a lock to prevent overlapping output from multiple threads
print_lock = threading.Lock()

def scan_port(ip, port):
    """
    Attempts to connect to a specific port on the target IP.
    If the connection is successful, it identifies the service name.
    """
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Timeout set to 1 second
        
        # connect_ex returns 0 if the connection is successful
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            try:
                # Attempt to resolve service name (e.g., 80 -> HTTP)
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"
            
            # Synchronized printing using lock
            with print_lock:
                print(f"[+] Found Open Port: {port:<5} | Service: {service}")
        
        sock.close()
    except Exception:
        pass

def main():
    # Application Header
    print("=" * 50)
    print("      MULTI-THREADED TCP PORT SCANNER v1.0")
    print("=" * 50)

    try:
        target_ip = input("[?] Enter Target IP/Domain: ")
        start_port = int(input("[?] Enter Starting Port: "))
        end_port = int(input("[?] Enter Ending Port: "))
        
        print(f"\n[*] Scanning Target: {target_ip}")
        print(f"[*] Scan Started at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 50)

        threads = []
        
        # Spawning threads for parallel execution
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(t)
            t.start()

        # Ensure all threads complete before finishing the script
        for t in threads:
            t.join()

        print("-" * 50)
        print(f"[*] Scan Completed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user. Exiting...")
    except ValueError:
        print("\n[!] Error: Please enter valid port numbers.")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
