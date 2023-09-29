#!/usr/bin/python3
"""
This script sends a request to a URL and displays the body of the response.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Utilise la méthode urllib pour effectuer la requête GET
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # En cas d'erreur HTTP, imprime le code d'erreur
        print("Error code:", e.code)
