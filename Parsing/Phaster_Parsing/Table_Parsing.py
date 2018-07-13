#!/usr/bin/python
import pandas as pd
import argparse
import warnings

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description= 'Edit Table')
parser.add_argument('table',help='Location of summary table')
parser.add_argument('namez', help='Name of output')

args = parser.parse_args()

df = pd.read_table(args.table)

columns_to_keep = ["REGION_LENGTH", "COMPLETENESS(score)", "SPECIFIC_KEYWORD", "ASSEMBLY_CONTIG_NUMBER", "CONTIG_LENGTH", "ATT_SITE_SHOWUP", "MOST_COMMON_PHAGE_NAME(hit_genes_count)", "FIRST_MOST_COMMON_PHAGE_PERCENTAGE"]
df2 = df[columns_to_keep]


names = df2["MOST_COMMON_PHAGE_NAME(hit_genes_count)"]
top = [x.split(",")[0] for x in names]
name = [x.split("_")[1:3] for x in top]
name2 = ["_".join(x) for x in name]
df2["MOST_COMMON_PHAGE_NAME(hit_genes_count)"] = name2

val = args.namez.split("_")[0]
output_name = val +".csv"
df2.to_csv(output_name, index=False)

