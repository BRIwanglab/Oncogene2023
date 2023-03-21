for bamfile in $(ls ../aligned_data/bwa_mem_mm10/*.bam); do
echo "Sorting $bamfile...";
samtools sort -@ 9 -o ..$(echo $bamfile | cut -d'.' -f 3).sorted.bam $bamfile && rm $bamfile;
echo "indexing..."
samtools index ..$(echo $bamfile | cut -d'.' -f 3).sorted.bam;
done;

