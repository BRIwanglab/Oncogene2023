for FILE in $(ls ../aligned_data/bwa_mem_mm10/*.bam); do
picard MarkDuplicates -I $FILE -O ..$(echo $FILE | cut -d'.' -f 3).sorted.markdups.bam -M ..$(echo $FILE | cut -d'.' -f 3).dupmetrics.txt && rm $FILE;
done