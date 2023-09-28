#!/bin/bash
# posts json file propice
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
