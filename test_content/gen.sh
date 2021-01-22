#!/bin/bash


# Generates files with corresponding random strings of certain byte length in base64 format.

for x in 1000 10000 100000 500000 1000000 2000000 3000000 4000000 5000000 6000000; do
	dd if=/dev/urandom bs="$x" count=1 | base64 > "./data_$x_bytes" && stat --printf="%s" "./data_$x_bytes";
done
