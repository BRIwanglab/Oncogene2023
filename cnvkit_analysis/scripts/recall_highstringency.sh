shopt -s extglob;
for FOLDER in $(ls -l ../results/bwa_mem_mm10_matched/ | grep ^d | awk '{print $9}'); 
    do
    CNS_FILE=$(ls ../results/bwa_mem_mm10_matched/$FOLDER/*@(dups|MM).cns);
    CNR_FILE=$(ls ../results/bwa_mem_mm10_matched/$FOLDER/*@(dups|MM).cnr);
    FILE_PREFIX=$(echo $CNS_FILE | awk '{print substr($1,1,length($1)-4)}');
    cnvkit.py call -m clonal --purity 1 -x f --drop-low-coverage --filter ci --center median $CNS_FILE -o $FILE_PREFIX.morestringent.call.cns;
done;

    
    
