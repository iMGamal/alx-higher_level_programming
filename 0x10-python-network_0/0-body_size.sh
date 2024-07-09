#!/bin/bash
# Using curl to get size of Response body
curl -sI "${1}" | grep "Content-Length" | cut -c 17-
