#!/bin/bash

out="./data"

if [ -n "$1" ]; then
  out=$1
fi

mkdir -p $out

usr=$(grep 'User:' credentials.yaml | tail -n1 | awk '{ print $2}')
pwd=$(grep 'Pwd:' credentials.yaml | tail -n1 | awk '{ print $2}')

name=ucmerced.zip
curl -u "${usr}:${pwd}" http://tum4.icaml.org/rs_data/${name} -o "${out}/${name}"
unzip "${out}/${name}" -d ${out}