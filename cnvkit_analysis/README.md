Author: Anthony Veltri  
Date: September 9, 2022  

# Overview
This project aims to compare the transcriptome and genome structure of mouse models of multiple myeloma. 

A preprint of the study is available at [BioRxiv](https://doi.org/10.1101/2022.08.21.504657) and was submitted to journal Oncogene.

>Flietner E, Yu M, Rajagopalan A, Zhou Y, Feng Y, Veltri AJ, et al. Genomic and transcriptional profiling stratifies VQ myeloma lines into two clusters with distinct risk signatures and drug responses. bioRxiv. 2022 Aug 22;2022.08.21.504657. DOI:10.1101/2022.08.21.504657 

# Analysis
Analysis proceeded as outlined in `./scipts/analysis.Rmd`.  
Raw files were supplied as unaligned or aligned BAM files. CNVkit was run using tumor and matched control tail samples per the preferences of the researchers.
>**NOTE:** raw files starting with 7732 or 7733 were supplied as aligned BAM files. BAM headers indicated that bwa_mem was used to align to mm10, so other files were aligned the same way.  

Scripts should be run with the `./scripts` folder as the working directory.

# Methods section included in manuscript
> Whole exome sequencing data was aligned to the mm10 reference genome using BWA MEM [CITATION]. Copy number variation analysis was carried out using matched controls for each sample with the CNVkit Python library and command-line software toolkit to infer and visualize copy number from high-throughput DNA sequencing data as described [CITATION]. Copy number calling was performed with default parameters, with the exception of increasing stringency through the use of `-m clonal –purity 1` arguments.

# Environment specification
Environment was managed with `conda`. Conda environment specification is in `environment.yml`.


