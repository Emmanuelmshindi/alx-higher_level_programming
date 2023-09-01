#!/bin/bash
# Send a get request to a url given as an argument.Print body size
curl -s "$1" | wc -c
