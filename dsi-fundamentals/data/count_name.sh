#!/bin/bash

NAME=$(echo $1 | tr [A-Z] [a-z])
cat $2 | tr [A-Z] [a-z] | tr ' ' '\n' | grep ^$NAME$ | wc -l
