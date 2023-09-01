#!/bin/bash
# Send a get request to a url and display the body of the response

curl -sfL "$1" -X GET
