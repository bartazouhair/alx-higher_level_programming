#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email as a parameter.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode les paramètres pour les inclure dans l'URL de la requête POST
    params = urllib.parse.urlencode({'email': email})
    params = params.encode('utf-8')  # Encode les données en bytes

    # Utilise la méthode urllib.request.urlopen pour effectuer la requête POST
    with urllib.request.urlopen(url, params) as response:
        # Lit et décode la réponse
        body = response.read().decode('utf-8')
        print(body)
