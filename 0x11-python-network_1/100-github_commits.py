#!/usr/bin/python3
"""
This script lists 10 commits of the repository "rails"
by the user "rails".
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construit l'URL de l'API GitHub pour récupérer les commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Envoie une requête GET à l'URL spécifiée
    response = requests.get(url)

    # Vérifie si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Récupère les 10 premiers commits de la réponse JSON
        commits = response.json()[:10]

        # Affiche chaque commit avec son sha et l'auteur
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Erreur lors de la requête à l'API GitHub")
