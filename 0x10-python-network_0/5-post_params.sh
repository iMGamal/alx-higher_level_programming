#!/bin/bash
# Using curl to display body of response
curl -sX POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "${1}"
