#!/bin/bash
# Using curl to display all methods that server will accept
curl -siX OPTIONS "${1}" | grep "Allow" | cut -c 8-
