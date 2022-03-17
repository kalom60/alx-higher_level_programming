#!/bin/bash
# script that shows the content-length from HTTP request
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
