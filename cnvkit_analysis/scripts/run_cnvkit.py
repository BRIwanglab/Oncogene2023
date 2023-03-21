# %%
import os
import re
from subprocess import Popen


# %%
bam_path = "../aligned_data/bwa_mem_mm10/"
bam_files = [file for file in os.listdir(bam_path) if file.endswith(".bam")]

samples = set()

for file in bam_files:
    samples.add(re.search("_(B\d{4})_", file).group(1))


# %%
bam_files

# %%
for sample in samples:
    control = list(filter(lambda item: "tail" in item and sample in item, bam_files))
    exp = list(filter(lambda item: "tail" not in item and sample in item, bam_files))
    print(control, exp)
    assert len(control) == 1 and len(exp) == 1
    control = control.pop()
    exp = exp.pop()

    out_path = f"../results/bwa_mem_mm10_matched/{sample}"
    os.makedirs(out_path, exist_ok = True)

    print(f"Starting cnvkit for {sample}")

    with open(f"{out_path}/stdout_log.txt", "w") as stdout:
        args = [
            "cnvkit.py",
            "batch",
            f"../aligned_data/bwa_mem_mm10/{exp}",
            "-n", f"../aligned_data/bwa_mem_mm10/{control}",
            "--targets", "../pipeline_resources/baits_mm10_liftover.bed",
            "-f", "../pipeline_resources/mm10.fa",
            "--annotate", "../pipeline_resources/mm10_refflat.txt",
            "-p", "9",
            "--output-reference", f"../results/bwa_mem_mm10_matched/{sample}_mm10.cnn",
            "-d", out_path,
            "--scatter",
            "--diagram",
        ]
        print(" ".join(args))
        p = Popen(args, stdout=stdout, stderr=stdout, preexec_fn=os.setsid)
        try:
            result_code = p.wait()
        except:
            os.killpg(p.pid)
            raise
        
        if result_code != 0:
            raise Exception("Run failed!")
    
    print(f"Finished {sample}.\n")


# %%



