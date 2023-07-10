import pandas as pd
import csv 
import numpy as np


ctoi_review_sheet = 'CTOI_review_sheet.csv'
exofop = 'exofop_edited.csv'

ctoi_fp = 'master1.csv'
toi = 'new_tois.csv'


ctoi_review_sheet_df = pd.read_csv(ctoi_review_sheet)
exofop_df = pd.read_csv(exofop)

ctoi_fp_df = pd.read_csv(ctoi_fp)
toi_df = pd.read_csv(toi)



ctoi_review_sheet_header = ['TIC', 'CTOI', 'Period (exofop)', 'Period (TEV)', 'Notes']
exofop_header = ['TIC ID', 'CTOI', 'Period (days)']


ctoi_fp_TICs= ctoi_fp_df['TIC'].tolist()
toi_TICs = toi_df['TIC ID'].tolist()



ctois_need_more_review_from_review_sheet = []
ctois_need_more_review_from_review_sheet.append(ctoi_review_sheet_header)


ctois_need_more_review_from_tois = []
ctois_need_more_review_from_tois.append(exofop_header)


# loop through the ctoi_review_sheet and see if the TIC exists in either the ctoi_fp. If not add it to a list to be added to a new csv file.
for _, row in ctoi_review_sheet_df.iterrows():
    if (row['TIC'] not in ctoi_fp_TICs) and (row['TIC'] not in toi_TICs):
        row_values = [
            row['TIC'],
            row['CTOI'],
            row['Period (exofop)'],
            row['Period (TEV)'],
            row['Notes']
        ]

        ctois_need_more_review_from_review_sheet.append(row_values)

    


# Now, do the excat same thing for the TOIs
for _, row in toi_df.iterrows():
    if (row['TIC ID'] not in ctoi_fp_TICs) and (row['TIC ID'] not in toi_TICs):
        row_values = [
            int(row['TIC ID']),
            row['CTOI'],
            row['Period (days)']
        ]

        ctois_need_more_review_from_tois.append(row_values)




# Now merge this two lists.
master_csv_header = ['TIC', 'CTOI', 'Period (exofop)', 'Period (TEV)', 'TESS mag', 'TFOPWG Disposition', 'Notes']

# Period (days) in new_tois same thing as period (exofop) in ctoi_fp_sheet

ctois_need_more_review_from_fp_sheet = 'need_more_review_from_fp_sheet.csv'
ctois_need_more_review_from_TOI_csv = 'need_more_review_from_TOIs.csv'

with open(ctois_need_more_review_from_fp_sheet, 'w', newline='') as from_fp_sheet:
    writer = csv.writer(from_fp_sheet)
    writer.writerows(ctois_need_more_review_from_review_sheet)



with open(ctois_need_more_review_from_TOI_csv, 'w', newline='') as from_TOIs:
    writer = csv.writer(from_TOIs)
    writer.writerows(ctois_need_more_review_from_tois)










