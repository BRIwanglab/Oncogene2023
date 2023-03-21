# %%
import os 
from subprocess import Popen
from sys import stderr, stdout
import sys
from collections import defaultdict

# %%
os.chdir("../raw_data")
files = [file for file in os.listdir() if file.endswith(".fastq")]

# %%
files

# %%
samples = defaultdict(lambda:None)

# %%
for file in files:
    samples[file[:-9]]

# %%
samples

# %% [markdown]
# # Define Hisat2 alignment

# %%
def hisat_alignment():
    for sample in samples.keys():
        print("starting", sample)
        p = Popen([
            "hisat2",
            "-p", "9",
            "-x", "../pipeline_resources/mm39_hisat_index/mm39_hisat_index",
            "-1", f"./{sample}_R1.fastq",
            "-2", f"./{sample}_R2.fastq",
            "-S", f"../aligned_data/hisat_aligned_mm39/{sample}.sam"
        ], stdout=stdout, stderr=stderr)
        p.wait()
        print(sample, "done.")

# %% [markdown]
# # Define BWA-MEM alignment

# %%
def bwa_mem_alignment():
        for sample in samples.keys():
            with open(f"../aligned_data/bwa_mem_mm10/logs/{sample}_alignment.log", "w") as logfile:
                print("starting", sample)
                cmd = [
                    "bwa", "mem",
                    "-t", "9",
                    "-M", #mark shorter split hits as secondary for picard compatibility
                    "-o", f"../aligned_data/bwa_mem_mm10/{sample}.sam",
                    "../pipeline_resources/bwa_index_mm10/bwa_index_mm10",
                    f"./{sample}_R1.fastq",
                    f"./{sample}_R2.fastq",
                ]
                print(" ".join(cmd))
                p = Popen(cmd, stdout=logfile, stderr=logfile)
                p.wait()
            print(sample, "done.\n")

# %% [markdown]
# # Run alignment

# %%
# only run when run as a script
if __name__ == "__main__":
    if "__file__" in globals():
        if sys.argv[1] == "bwa":
            bwa_mem_alignment()
        elif sys.argv[1] == "hisat2":
            hisat_alignment()
        else:
            raise Exception("incorrect aligner specified")
    else:
        # run when run as notebook
        bwa_mem_alignment()


# %%
#hisat_alignment()



# %%
