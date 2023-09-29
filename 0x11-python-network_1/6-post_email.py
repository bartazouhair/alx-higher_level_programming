#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Paramètres à inclure dans la requête POST
    params = {'email': email}

    # Envoie une requête POST à l'URL spécifiée
    response = requests.post(url, data=params)

    print("Your email is:", email)
