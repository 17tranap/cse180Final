# Python Scripts for Post-Processing of DESeq2 Output Files
### Alexandria Tran, Riya Verma, Jiayan Ma

After completion of an RNA-seq differential expression analysis workflow, two files require post-processing for neater visualization. 

One file contains normalized feature counts of each gene alignment for each sample -- referred to from now on as the "counts file". 
Another contains relevant statistical information -- "stats file" from now on -- for the different levels of transcript maps to each gene across the different conditions: flox and knockdown of a gene of interest. 

## normalizedOutputFormatter.py
#### Input:File path to the counts file and the file path to the stats file. 
Read each file and remove the mapped sequences that do no correspond to annotated genes (denoted by a geneid of "MSTRG") as well as the gene rows that hold trivial values such as all "0"s or "NA"s. Outputted files are named "RelevantNormalizedCountsDeseq.tabular" and "RelevantDESEQpvalueslog.tabular".

## geneIDReplacer.py
#### Input: File paths to relevant counts and stats files and biotools geneid annotation
These scripts were built to clean up the file outputs that used the Mus Musculus reference genome (FASTA) and genome annotations (.gff). Because of this the reads are mapped to UCSC indexed geneids that correspond to known genes. To get the known genes, we take the column of relevant geneids in "RelevantNormalizedCountsDeseq.tabular" and convert them using biotools.fr/mouse/ucsc_id_converter. In geneIDReplacer.py, a dictionary is formed with the tab-separated output form biotools and converts all geneids to the genes, excluding rows where geneids do not correspond to known genes. 

## getSignificantGenes.py and makeNewFeatureCounts.py
#### Input: File paths to counts and stats files with relevant annotated genes
With the known genes, we select only the rows with significant p-values of below 0.05 using getSignificantGenes.py and the relevant genes stats file. Using this set of significant genes, we then only select the feature counts rows of these genes in makeNewFeatureCounts.py. 

This makeNewFeatureCounts.py file now is ready to be inputted to visualization softwares.

## Note about data:
As the datasets come from a UC San Diego Lab, access to original sequence read datasets requires permission. Code for the tools and pipelines used to generate the sample data for these Python scripts can be found at: https://usegalaxy.org:/u/riya_verma/h/cse180-final-project

