#!/usr/bin/python3
"""
Ce script prend une lettre en argument et envoie une requête POST
à http://0.0.0.0:5000/search_user avec la lettre comme paramètre.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    params = {'q': q}

    # Envoie une requête POST à l'URL spécifiée
    response = requests.post(url, data=params)

    try:
        # Tente de charger la réponse au format JSON
        user_data = response.json()

        # Vérifie si la réponse contient des données
        if user_data:
            print("[{}] {}".format(user_data['id'], user_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
