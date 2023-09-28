#!/bin/bash
# sends a req to a URL and displays size of response propice
curl -so /dev/null -w '%{size_download}\n' $1
