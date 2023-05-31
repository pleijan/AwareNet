# installation projet

## Prérequis

avoir python 3.10 d'installé

avoir github d'installé

## installation du NIDS

git clone https://github.com/pleijan/AwareNet

## installation librairies

    pip install pyvis
    pip install scapy
    pip install matplotlib
    pip install flask

## definir adresse ip reseaux

dans app.py 

l.13 - CreateGraph.createGraph(1, "mettre ip reseau ici")

l.20 - CreateGraph.createGraph(1, "mettre ip reseau ici")

## lancement du NIDS

    cd AwareNet
    python3 app.py