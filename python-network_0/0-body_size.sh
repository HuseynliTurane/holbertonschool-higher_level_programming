#!/bin/bash
# Query URL and display response body size in bytes
curl -s "$1" | wc -c
