# Molecular characterization stratifies VQ myeloma cells into two clusters with distinct risk signatures and drug responses

## Running Title: risk-stratification of VQ myeloma lines

## Abstract

Multiple myeloma (MM) is a cancer of malignant plasma cells in the bone marrow and extramedullary sites. We previously characterized a VQ model for human high-risk MM. Different VQ lines display distinct disease phenotypes and survivals, suggesting significant intra-model variation. Here, we use whole exome sequencing and copy number variation (CNV) analysis coupled with RNA-Seq to stratify VQ lines into corresponding clusters: Group A cells had monosomy chr5 and overexpressed genes and pathways associated with sensitivity to bortezomib (Btz) treatment in human MM patients. By contrast, Group B VQ cells carried recurrent amplification (Amp) of chromosome (chr) 3 and displayed high-risk MM features, including downregulation of Fam46c, upregulation of cancer growth pathways associated with functional high-risk MM, and expression of Amp1q and high-risk UMAS-70 and EMC-92 gene signatures. Consistently, in sharp contrast to Group A VQ cells that showed short-term response to Btz, Group B VQ cells were de novo resistant to Btz in vivo. Our study highlights Group B VQ lines as highly representative of the human MM subset with ultrahigh risk.

## Methods and Code
- B cell receptor (BCR) Immunoglobulin heavy (IgH) chain and Immunoglobulin light (IgL) chain repertoire sequencing
  - VQ_Samples_RepSeq_Mutation_Analysis.Rmd
- Whole Exome Sequencing (WES) and copy number variation (CNV) analysis
- RNA-Seq
  - VQ_RNASeq_Analysis.Rmd

## SessionInfo

```
> sessionInfo()
R version 4.2.1 (2022-06-23)
Platform: x86_64-apple-darwin17.0 (64-bit)
Running under: macOS Ventura 13.2.1

Matrix products: default
LAPACK: /Library/Frameworks/R.framework/Versions/4.2/Resources/lib/libRlapack.dylib

locale:
[1] en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-8

attached base packages:
[1] grid      stats4    stats     graphics  grDevices utils     datasets  methods   base     

other attached packages:
 [1] shazam_1.1.2                alakazam_1.2.1              ggpubr_0.6.0               
 [4] rstatix_0.7.2               xlsx_0.6.5                  msigdbr_7.5.1              
 [7] limma_3.52.4                lubridate_1.9.2             forcats_1.0.0              
[10] stringr_1.5.0               dplyr_1.1.0                 purrr_1.0.1                
[13] readr_2.1.4                 tidyr_1.3.0                 tibble_3.2.0               
[16] tidyverse_2.0.0             Rtsne_0.16                  readxl_1.4.2               
[19] ReactomePA_1.40.0           enrichplot_1.18.3           EnhancedVolcano_1.14.0     
[22] gplots_3.1.3                org.Mm.eg.db_3.15.0         AnnotationDbi_1.60.2       
[25] genefilter_1.78.0           pheatmap_1.0.12             clusterProfiler_4.7.1.003  
[28] ggrepel_0.9.3               ggplot2_3.4.1               biomaRt_2.52.0             
[31] tximport_1.24.0             DESeq2_1.36.0               SummarizedExperiment_1.26.1
[34] Biobase_2.58.0              MatrixGenerics_1.8.1        matrixStats_0.63.0         
[37] GenomicRanges_1.48.0        GenomeInfoDb_1.34.9         IRanges_2.32.0             
[40] S4Vectors_0.36.2            BiocGenerics_0.44.0        

loaded via a namespace (and not attached):
  [1] utf8_1.2.3               tidyselect_1.2.0         RSQLite_2.3.0           
  [4] BiocParallel_1.32.5      scatterpie_0.1.8         airr_1.4.1              
  [7] munsell_0.5.0            codetools_0.2-19         withr_2.5.0             
 [10] colorspace_2.1-0         GOSemSim_2.24.0          filelock_1.0.2          
 [13] knitr_1.42               rstudioapi_0.14          ggsignif_0.6.4          
 [16] rJava_1.0-6              DOSE_3.24.2              GenomeInfoDbData_1.2.9  
 [19] polyclip_1.10-4          bit64_4.0.5              farver_2.1.1            
 [22] downloader_0.4           vctrs_0.5.2              treeio_1.22.0           
 [25] generics_0.1.3           gson_0.1.0               xfun_0.37               
 [28] timechange_0.2.0         BiocFileCache_2.4.0      doParallel_1.0.17       
 [31] diptest_0.76-0           R6_2.5.1                 graphlayouts_0.8.4      
 [34] locfit_1.5-9.7           bitops_1.0-7             cachem_1.0.7            
 [37] fgsea_1.24.0             gridGraphics_0.5-1       DelayedArray_0.22.0     
 [40] scales_1.2.1             ggraph_2.1.0             gtable_0.3.1            
 [43] tidygraph_1.2.3          rlang_1.0.6              splines_4.2.1           
 [46] lazyeval_0.2.2           broom_1.0.4              yaml_2.3.7              
 [49] reshape2_1.4.4           abind_1.4-5              backports_1.4.1         
 [52] qvalue_2.30.0            tools_4.2.1              ggplotify_0.1.0         
 [55] ellipsis_0.3.2           RColorBrewer_1.1-3       Rcpp_1.0.10             
 [58] plyr_1.8.8               progress_1.2.2           zlibbioc_1.44.0         
 [61] RCurl_1.98-1.10          prettyunits_1.1.1        viridis_0.6.2           
 [64] cowplot_1.1.1            magrittr_2.0.3           data.table_1.14.8       
 [67] reactome.db_1.81.0       hms_1.1.2                xlsxjars_0.6.1          
 [70] patchwork_1.1.2          evaluate_0.20            xtable_1.8-4            
 [73] HDO.db_0.99.1            XML_3.99-0.13            gridExtra_2.3           
 [76] compiler_4.2.1           KernSmooth_2.23-20       crayon_1.5.2            
 [79] shadowtext_0.1.2         htmltools_0.5.4          ggfun_0.0.9             
 [82] tzdb_0.3.0               geneplotter_1.74.0       aplot_0.1.10            
 [85] DBI_1.1.3                tweenr_2.0.2             WriteXLS_6.4.0          
 [88] dbplyr_2.3.1             MASS_7.3-58.3            rappdirs_0.3.3          
 [91] babelgene_22.9           ade4_1.7-22              Matrix_1.5-3            
 [94] car_3.1-1                cli_3.6.0                parallel_4.2.1          
 [97] igraph_1.4.1             pkgconfig_2.0.3          GenomicAlignments_1.32.1
[100] foreach_1.5.2            xml2_1.3.3               ggtree_3.6.2            
[103] annotate_1.74.0          XVector_0.38.0           yulab.utils_0.0.6       
[106] digest_0.6.31            graph_1.74.0             Biostrings_2.66.0       
[109] rmarkdown_2.20           cellranger_1.1.0         fastmatch_1.1-3         
[112] tidytree_0.4.2           curl_5.0.0               Rsamtools_2.12.0        
[115] gtools_3.9.4             graphite_1.42.0          lifecycle_1.0.3         
[118] nlme_3.1-162             jsonlite_1.8.4           carData_3.0-5           
[121] seqinr_4.2-23            viridisLite_0.4.1        fansi_1.0.4             
[124] pillar_1.8.1             lattice_0.20-45          KEGGREST_1.38.0         
[127] fastmap_1.1.1            httr_1.4.5               survival_3.5-5          
[130] GO.db_3.16.0             glue_1.6.2               iterators_1.0.14        
[133] png_0.1-8                bit_4.0.5                ggforce_0.4.1           
[136] stringi_1.7.12           blob_1.2.3               caTools_1.18.2          
[139] memoise_2.0.1            ape_5.7  

```


