#!/usr/bin/env bash

shell_dir=$(dirname "$0")

cd "$shell_dir"

rm -f ai-lab-1_zz2960.zip

zip -r ai-lab-1_zz2960.zip hill_climbing hill_climb README.md
