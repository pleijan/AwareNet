import scapy.all as scapy


def network_scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    client_dict = {"ip": "128.168.2.2", "mac": "00:00:00:00:00:00"}
    clients_list.append(client_dict)

    client_dict = {"ip": "128.168.2.3", "mac": "00:00:00:00:00:10"}
    clients_list.append(client_dict)

    return clients_list
