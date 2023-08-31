#!/bin/bash

url="$1"

size=$(curl -sl "$url" | iF 'content-length' | awk '{print$2}')

echo "$size"
