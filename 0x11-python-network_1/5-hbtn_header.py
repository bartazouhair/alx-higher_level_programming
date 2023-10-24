#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the
value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Envoie une requête GET à l'URL spécifiée
    response = requests.get(url)

    # Récupère la valeur de l'en-tête X-Request-Id
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
