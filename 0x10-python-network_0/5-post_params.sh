#!/bin/bash
# Using curl to display body of response
curl -sH "email: test@gmail.com" -sH "subject: I will always be here for PLD" -sX POST "${1}"
