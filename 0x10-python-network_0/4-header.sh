#!/bin/bash
# Takes in a URL sends a GET request and returns response body header variable 
curl -s -H "X-School-User-Id: 98" "$1" 
