import pandas as pd
import csv 

ctoi_review_fp = 'CTOI_Review_FP.csv'
exofop = 'exofop_edited.csv'

ctoi_review_fp_df = pd.read_csv(ctoi_review_fp)
exofop_df = pd.read_csv(exofop)
# Goal: make a csv file of all the fp and also include the "NOTEs" field from the CTOI_ereicew_fp.csv




marked_as_fp = []
marked_as_fp_ctoi = []
marked_as_fp_exofop = []


# ideal output would be .csv with the columns headers 
# TIC ID, CTOI ID, transit epoch, period, planet radius, duration, depth, and TFOPWG Disposition


# Number of rows for both exofop and ctoi_review_fp df
ctoi_review_fp_df_rows = len(ctoi_review_fp_df)
exofop_df_rows = len(exofop_df)

# print(f"ctoi length {ctoi_review_fp_df_rows}")
# print(f"exofop length {exofop_df_rows}")
# Append the column to the false positive list
column_title_for_ctoi_fp = ['TIC', 'CTOI','Period (exfop)', 'Notes']
column_title_for_exofop_fp = ['TIC ID', 'CTOI', 'Transit Epoch (BJD)', 'Period (days)', 'Planet Radius (R_Earth)', 'Duration (hours)', 'Depth (mmag)', 'TFOPWG Disposition']


marked_as_fp_ctoi.append(column_title_for_ctoi_fp)
marked_as_fp_exofop.append(column_title_for_exofop_fp)




# Loop through each row in the two df 
for ctoi_index, ctoi_row in ctoi_review_fp_df.iterrows():
    if ctoi_row['TEV Disposition'] == 'FP (EB)' or ctoi_row['TEV Disposition'] == 'FP(EB)' or ctoi_row['TEV Disposition'] == 'EB':
        ctoi_row_values = [
            ctoi_row['TIC'],
            ctoi_row['CTOI'],
            ctoi_row['Period (exofop)'],
            ctoi_row['Notes']
        ]

        marked_as_fp_ctoi.append(ctoi_row_values)



for exofop_index, exofop_row in exofop_df.iterrows():
    if exofop_row['TFOPWG Disposition'] == 'FP':
        exofop_row_values = [
            exofop_row['TIC ID'],
            exofop_row['CTOI'],
            exofop_row['Transit Epoch (BJD)'],
            exofop_row['Period (days)'],
            exofop_row['Planet Radius (R_Earth)'],
            exofop_row['Duration (hours)'],
            exofop_row['Depth (mmag)'],
            exofop_row['TFOPWG Disposition']  
        ]

        marked_as_fp_exofop.append(exofop_row_values)



ctoi_fp_s = 'ctoi_false_ps.csv'
exofop_fp_s = 'exofop_false_ps.csv'


with open(ctoi_fp_s, 'w', newline='') as ctoi_fp_file:
    ctoi_fp_data = csv.writer(ctoi_fp_file)
    ctoi_fp_data.writerows(marked_as_fp_ctoi)


# with open(exofop_fp_s, 'w', newline='') as exofop_fp_file:
#     exofop_fp_data = csv.writer(exofop_fp_file)
#     exofop_fp_data.writerows(marked_as_fp_exofop) 

