import os

def banner():
    print("""
╔══════════════════════════════════╗
║   Ethical Hacking Toolkit (Py)   ║
╚══════════════════════════════════╝
     ->  faijan h4cker  <-

1. Whois Lookup
2. Port Scanner
3. Subdomain Scanner
4. SSH Brute Force
5. FTP Brute Force
6. Packet Sniffer
7. Generate Payload
8. A Gift For You
0. Exit

""")

def main():
    while True:
        banner()
        choice = input("Select Option > ")
        if choice == '1':
            os.system("python3 info_gathering/whois_lookup.py")
        elif choice == '2':
            os.system("python3 scanning/port_scanner.py")
        elif choice == '3':
            os.system("python3 scanning/subdomain_scanner.py")
        elif choice == '4':
            os.system("python3 brute_force/ssh_brute.py")
        elif choice == '5':
            os.system("python3 brute_force/ftp_brute.py")
        elif choice == '6':
            os.system("python3 sniffing/packet_sniffer.py")
        elif choice == '7':
            os.system("python3 payloads/payload_generator.py")
        elif choice == '8':
            os.system("python3 gift/gift.py")    
        elif choice == '0':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
