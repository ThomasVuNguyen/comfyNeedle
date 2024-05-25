#Scan the network for all connected devices

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        clients_list.append({"ip": element[1].psrc, "mac": element[1].hwsrc})
    return clients_list

def display_result(results):
    print("IP Address\t\tMAC Address\n")
    for client in results:
        print(client["ip"] + "\t\t" + client["mac"])

# Replace '192.168.1.1/24' with your network's subnet
target_ip = "10.0.0.0/24"
results = scan(target_ip)
display_result(results)
