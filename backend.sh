#!/bin/bash

shared_content=""

while IFS= read -r line; do
  shared_content="$line"
  echo "$shared_content"
done
