import scapy.all as scapy
import socket

def scan_and_resolve(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for sent, received in answered_list:
        ip_address = received.psrc
        mac_address = received.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            alias = socket.gethostbyaddr(ip_address)[1]
            #hostname = str(socket.gethostbyaddr(ip_address))
        except socket.herror:
            hostname = "Unknown"
            alias = "Unknown"
        clients_list.append({"ip": ip_address, "mac": mac_address, "hostname": hostname, "alias": alias})
    return clients_list

def display_results(results):
    print("IP Address\t\tMAC Address\t\tHostname\t\tAlias")
    for client in results:
        print(f"{client['ip']}\t\t{client['mac']}\t\t{client['hostname']}\t\t{client['alias']}")

target_subnet = "10.0.0.0/24"  # Replace with your network's subnet
results = scan_and_resolve(target_subnet)
display_results(results)
