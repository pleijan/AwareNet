import nmap


def network_scan(ip):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, arguments="-sn")

    clients_list = []
    for element in nm.all_hosts():
        if "mac" in nm[element]["addresses"]:
            client_dict = {"ip": element, "mac": nm[element]["addresses"]["mac"], "name":nm[element].hostname()}
            clients_list.append(client_dict)

    return clients_list
