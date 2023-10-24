#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the
body of the response. If the HTTP status code is greater than or equal to 400,
it prints an error message with the status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Envoie une requête GET à l'URL spécifiée
    response = requests.get(url)

    # Vérifie si le code de statut est supérieur ou égal à 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
