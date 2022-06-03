#!/bin/bash


function transform()
{
echo -e "#> python3 create_firenofire_patches.py \"$1\""
# has been create_firenofire_patches.py
if ! python3 flexipatches.py "$1" ; then
    echo
    echo "FATAL: File \"$1\" failed to transform"
    echo -n "DU: "; du --bytes "$1"
    echo -n "FI: "file "$1"
fi
}

export -f transform

# we only consider products, not the tiles from Dima
ls /data/bulk/rsDatasets/wildfire/data/data/mlab_processed/S2*_prod.tif | parallel -j 4 --progress transform {} > firedataset.log


