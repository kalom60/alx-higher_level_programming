#!/bin/bash
# script that takes in a URL, make response
curl -sX POST 0.0.0.0:5000/catch_me -H "Content-Type: text/html" -d 'You got me!'
