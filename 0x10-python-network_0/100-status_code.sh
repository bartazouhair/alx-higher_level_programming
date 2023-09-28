#!/bin/bash
# prints status code propice
curl -so /dev/null -w "%{http_code}" $1
