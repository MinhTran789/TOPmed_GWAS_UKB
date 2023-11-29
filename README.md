# TOPmed_GWAS_UKB

Check the main tutorial at https://dnanexus.gitbook.io/uk-biobank-rap/science-corner/genomic-target-discovery-for-ischaemic-heart-disease-using-gwas-ld-clumping-and-phewas#imputed-data-qc

This repository contains the modified bgens_qc.wdl workflow from https://github.com/dnanexus/UKB_RAP/blob/main/end_to_end_gwas_phewas/bgens_qc/bgens_qc.wdl so that it can work for UKB TOPmed Imputation data (Data-field 21007).

The original tutorial used the GEL Imputed data, however, for TOPmed data the resulting variants passing filter did not have rsID. Therefore, the snplist file from PLINK2 only contains dots "."

The bgens_qc.wdl was modified to include parameters `--set-missing-var-ids`, `--new-id-max-allele-len`, and `--export bgen-1.2 'bits=8'` to PLINK2 to give custom names to the variants and create new bgen, sample files.

GWAS was performed using the regenie app. The last step, "concatenate_and_plot", launched by this app did not have dynamic instance allocation and therefore ran out of memory. Therefore we need to specify a non-default instance with `--instance-type '{"concatenate_and_plot":"mem3_ssd1_v2_x16"}'`.