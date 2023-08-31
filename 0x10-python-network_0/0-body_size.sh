#!/bin/bash
# Send a get request to a url given as an argument.Print body size

url="$1"

size=$(echo curl -sl "$url" | grep -i 'content-length' | awk '{print $2}')

echo "$size"
