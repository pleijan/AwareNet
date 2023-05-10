from flask import Flask, render_template
from pyvis.network import Network

app = Flask(__name__)

@app.route('/')
def index():
    # Créer un objet Network Pyvis
    net = Network()

    # Ajouter des nœuds et des arêtes au graphique
    net.add_node(1, label="Node 1")
    net.add_node(2, label="Node 2")
    net.add_edge(1, 2)

    # Rendre le graphique Pyvis dans un fichier HTML
    net.write_html("templates/mygraph.html")

    # Renvoyer le contenu HTML dans une vue Flask
    return render_template("index.html")

@app.route('/reseaux/')
def reseaux():
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


if __name__ == '__main__':
    app.run(debug=True)
