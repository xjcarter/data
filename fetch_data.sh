#!/bin/bash

source /home/jcarter/sandbox/trading/env.sh
home="/home/jcarter/sandbox/trading/data/"

echo
if [ $# -lt 1 ]
then
    echo "Uaage: fetch_data.sh <fetch_list_file>"
else
    fetch_file="${home}/${1}"
    if [ ! -f ${fetch_file} ]
    then
        echo "fetch_list_file: ${fetch_file} not found."
        exit 1
    else
        echo "Using fetch_file ${fetch_file} ..."
        python ${home}/yahoo_data.py --file="${fetch_file}" 
        python ${home}/data_catalog.py --file="${fetch_file}" 
    fi
fi



