#!/usr/bin/python3
"""prend en compte une URL et une adresse électronique
envoie une requête POST à l'URL
passée avec l'email comme paramètre, et enfin affiche le corps de la réponse"""
import requests
from sys import argv


if __name__ == '__main__':
    result = requests.post(argv[1], data={'email': argv[2]})
    print(result.text)
