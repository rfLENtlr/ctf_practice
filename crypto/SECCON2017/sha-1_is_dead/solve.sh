#!/bin/bash

wget https://shattered.it/static/shattered-1.pdf
wget https://shattered.it/static/shattered-2.pdf

size=$(wc shattered-1.pdf | awk '{print $3}')
pad=$((2017 * 1024 - $size + 10))  # 10は適当

for _ in $(seq 1 $pad)
do
  echo -n a >> shattered-1.pdf
  echo -n a >> shattered-2.pdf
done
