#!/bin/bash
# POST request with the contents of a file
curl -s -X POST "$1" -H "Content-Type: application/json" -d "$(cat "$2")"
