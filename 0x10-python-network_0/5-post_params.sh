#!/bin/bash
# Using curl to display body of response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "${1}"
