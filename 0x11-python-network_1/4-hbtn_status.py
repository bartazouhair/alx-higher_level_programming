#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using requests module.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Envoie une requête GET à l'URL spécifiée
    response = requests.get(url)

    # Affiche les informations sur la réponse
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
