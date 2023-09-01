#!/bin/bash
# Takes in a url and displays all HTTP methods the server accepts
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
