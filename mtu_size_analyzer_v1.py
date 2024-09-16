from scapy.all import rdpcap, IP
import time

print("MTU size analyzer by Nils Kruchem ©")
print("")

time.sleep(2)

def find_mtu_size(pcap_file):
    packets = rdpcap(pcap_file)
    max_length = 0

    for packet in packets:
        if IP in packet:
            ip_packet = packet[IP]
            packet_length = ip_packet.len
            if packet_length > max_length:
                max_length = packet_length
    print("")
    print(f"MTU size: {max_length} bytes")
    print("Please note that MTU size may be slightly smaller than this value due to packet headers.")
    print("")

if __name__ == "__main__":
    pcap_file = input("Please enter the path to your PCAP file: ")
    try:
        find_mtu_size(pcap_file)
    except FileNotFoundError:
        print(f"Error: The file '{pcap_file}' was not found.")
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        input("Press enter to leave the program...")