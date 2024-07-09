#!/bin/bash
# Using curl to display body of response
curl -sd "param1=email:test@gmail.com&param2=subject:I will always be here for PLD" -X POST "${1}"
