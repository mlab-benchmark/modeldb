#!/bin/bash

downloadAndUnzip () {
  local usr=$1
  local pwd=$2
  local baseurl=$3
  local name=$4
  local out=$5

  curl -u "${usr}:${pwd}" "${baseurl}/rs_data/${name}" -o "${out}/${name}"
  unzip "${out}/${name}" -d ${out}
}

out="./data"

if [ -n "$1" ]; then
  out=$1
fi

mkdir -p $out

usr=$(grep 'User:' credentials.yaml | tail -n1 | awk '{ print $2}')
pwd=$(grep 'Pwd:' credentials.yaml | tail -n1 | awk '{ print $2}')
baseurl=$(grep 'Url:' credentials.yaml | tail -n1 | awk '{ print $2}')

datasets=(aid.zip eurosat_ms.zip eurosat_rgb.zip gaofen.zip resisc45.zip rsicb256.zip ucmerced.zip wildfire.zip)
for name in ${datasets[@]}; do
  downloadAndUnzip $usr $pwd $baseurl $name $out
done


