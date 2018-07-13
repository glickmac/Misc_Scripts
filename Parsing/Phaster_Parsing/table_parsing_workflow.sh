#!/bin/bash
set -euo pipefail  # bash strict mode http://redsymbol.net/articles/unofficial-b$
IFS=$'\n\t'

outdir=""
biom=""
threshold=""
main_dir=$(pwd)
threads=2

usage(){ echo "$0 usage:" && grep " .)\ #" $0; exit 0; }
[ $# -eq 0 ] && usage

while getopts ":h:t:" option
do
case "${option}" in
        t) # The path to and including the summary table
		table=${OPTARG};;
        h | *) # Display Help
                usage
                exit 0;;
esac
done

shift "$((OPTIND-1))"


sed -i '' -n '/REGION/,$p' $table

sed -i '' -e 's/-//g' $table

sed -i '' -e 's/REGION_POSITION/ASSEMBLY_CONTIG_NUMBER   CONTIG_LENGTH      CONTIG_DEPTH/g' $table

awk -v OFS="\t" '$1=$1' $table > output.txt

./Table_Parsing.py output.txt $table

rm output.txt
