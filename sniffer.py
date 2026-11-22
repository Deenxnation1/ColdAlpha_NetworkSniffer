from scapy.all import sniff, IP

def process_packet(packet):
    # Check if the captured packet has an IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"[+] Source IP: {src_ip} --> Destination IP: {dst_ip} | Protocol: {protocol}")

print("Starting Network Sniffer... Press Ctrl+C to stop.")
# Capture packets continuously on your network interface
sniff(prn=process_packet, store=False)