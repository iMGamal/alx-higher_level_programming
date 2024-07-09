#!/bin/bash
# Using curl to display all methods that server will accept
curl -sX OPTIONS "${1}" | grep "Allow" | cut -c 8-
