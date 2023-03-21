#! /bin/bash

for FILE in $(ls ../aligned_data/bwa_mem_mm10/*.bai); do 
NEWNAME="$(echo $FILE | awk -F "bam.bai" '{print $1}')markdups.bam.bai";
mv $FILE $NEWNAME; 
done