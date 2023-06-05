from flask import Flask, render_template

import CreatePlot
import CreateGraph


app = Flask(__name__)

@app.route('/')
def index():


    CreateGraph.createGraph(1, "192.168.1.0/24")
    CreatePlot.createPlot()
    return render_template("index.html")

@app.route('/reseaux/')
def reseaux():

    CreateGraph.createGraph(0, "192.168.1.0/24")
    return render_template('reseaux.html')

@app.route('/tableau/')
def tableau():
    return render_template('tableau.html')

@app.route('/graph/')
def graph():
    CreatePlot.createPlot()
    return render_template('graph.html')

@app.route('/carte/')
def carte():
    return render_template('mygraph.html')

@app.route('/carteGrand/')
def carteGrand():
    return render_template('mygraph2.html')


if __name__ == '__main__':
    app.run(debug=True)
