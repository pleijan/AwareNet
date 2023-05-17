from flask import Flask, render_template
from pyvis.network import Network
import network_scan

app = Flask(__name__)

@app.route('/')
def index():
    net = Network()
    net.add_node("Routeur",color="#33FF6C")  # Ajoute un nœud pour le routeur

    # Récupère la liste des ordinateurs connectés
    clients_list = network_scan.network_scan("192.168.1.0/24")

    # Ajoute un nœud pour chaque ordinateur connecté
    for client in clients_list:
        net.add_node(client["ip"], label=client["ip"] + "\n" + client["mac"])

    # Ajoute une connexion entre le routeur et chaque ordinateur connecté
    for client in clients_list:
        net.add_edge("Routeur", client["ip"])

    net.height = "300px"
    # Rendre le graphique Pyvis dans un fichier HTML
    net.write_html("templates/mygraph.html")

    # Renvoyer le contenu HTML dans une vue Flask
    return render_template("index.html")

@app.route('/reseaux/')
def reseaux():
    # Créer un objet Network Pyvis
    net = Network()
    net.add_node("Routeur",color="#33FF6C")  # Ajoute un nœud pour le routeur

    # Récupère la liste des ordinateurs connectés
    clients_list = network_scan.network_scan("192.168.1.0/24")

    # Ajoute un nœud pour chaque ordinateur connecté
    for client in clients_list:
        net.add_node(client["ip"], label=client["ip"] + "\n" + client["mac"])

    # Ajoute une connexion entre le routeur et chaque ordinateur connecté
    for client in clients_list:
        net.add_edge("Routeur", client["ip"])

    net.height = "700px"
    # Rendre le graphique Pyvis dans un fichier HTML
    net.write_html("templates/mygraph2.html")

    return render_template('reseaux.html')

@app.route('/tableau/')
def tableau():
    return render_template('tableau.html')

@app.route('/graph/')
def graph():
    return render_template('graph.html')

@app.route('/carte/')
def carte():
    return render_template('mygraph.html')

@app.route('/carteGrand/')
def carteGrand():
    return render_template('mygraph2.html')


if __name__ == '__main__':
    app.run(debug=True)
