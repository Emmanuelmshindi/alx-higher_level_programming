#!/bin/bash
# Sends a request and displays status code of the response
curl -s -o /dev/null -I --w "%{http_code}" "$1" 
