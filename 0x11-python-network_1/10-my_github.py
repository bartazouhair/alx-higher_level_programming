#!/usr/bin/python3
"""
This script uses the GitHub API to display your GitHub id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    # Crée un en-tête d'authentification avec (token)
    auth = (username, password)

    # Utilise la méthode GET pour récupérer les informations de l'utilisateur
    response = requests.get('https://api.github.com/user', auth=auth)

    # Vérifie si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Récupère l'ID de l'utilisateur depuis la réponse JSON
        user_id = response.json()['id']
        print(user_id)
    else:
        print(None)
