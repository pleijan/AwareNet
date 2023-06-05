import string

from pyvis.network import Network
import network_scan


def createGraph(type, IP):
    net = Network()
    net.add_node("Routeur", color="#33FF6C")  # Ajoute un nœud pour le routeur

    # Récupère la liste des ordinateurs connectés
    clients_list = network_scan.network_scan(IP)

    # Ajoute un nœud pour chaque ordinateur connecté
    for client in clients_list:
        net.add_node(client["ip"], label=client["name"]+"\n"+client["ip"] + "\n" + client["mac"])

    # Ajoute une connexion entre le routeur et chaque ordinateur connecté
    for client in clients_list:
        net.add_edge("Routeur", client["ip"])

    if type == 1:
        net.height = "300px"
    else:
        net.height = "700px"
    # Rendre le graphique Pyvis dans un fichier HTML
    net.write_html("templates/mygraph.html")
