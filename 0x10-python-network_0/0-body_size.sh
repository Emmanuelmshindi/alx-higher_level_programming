#!/bin/bash

url="$1"

size=$(curl -sl "$url" | grep 'content-length' | awk '{print $2}')

echo "$size"
