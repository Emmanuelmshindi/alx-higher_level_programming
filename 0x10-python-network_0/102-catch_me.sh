#!/bin/bash
# Make a request to 0.0.0.0:5000/catch_me respond with You got me! in the response body
curl -sLX PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
