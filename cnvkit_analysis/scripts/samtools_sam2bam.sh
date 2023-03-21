for samfile in $(ls ../aligned_data/bwa_mem_mm10/*.sam); do
echo "converting $samfile...";
samtools view -@ 9 -b -o ..$(echo $samfile | cut -d'.' -f 3).bam $samfile && rm $samfile;
done;