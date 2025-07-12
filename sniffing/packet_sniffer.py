import scapy.all as scapy

def sniff(interface):
    print(f"[+] Listening on {interface}...")
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    print(packet.summary())

sniff("eth0")
