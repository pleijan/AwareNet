import matplotlib.pyplot as plt
import random

def createPlot() :
    # Générer des données aléatoires

    plt.clf()

    nombre_requetes = 100
    temps = list(range(nombre_requetes))
    valeurs = [random.randint(0, 100) for _ in range(nombre_requetes)]

    # Créer le graphique
    plt.plot(temps, valeurs)
    plt.xlabel('Temps')
    plt.ylabel('Nombre de requêtes')

    # Sauvegarder le graphique au format JPEG
    plt.savefig('static/img/graphique.jpg', format='jpeg')