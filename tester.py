import pandas as pd
import csv


ctoi_review_fp = 'CTOI_Review_FP.csv'
exofop = 'exofop_edited.csv'



ctoi_review_fp_df = pd.read_csv(ctoi_review_fp)
exofop_df = pd.read_csv(exofop)


exofop_false_positive_tic_ids = []
exofop_false_positive = []
ctoi_review_false_positives = []

# Goal: have a CSV file with the following header
# TIC, CTOI, Transit Epoch, Period (exofop), Period (TEV), Planet Radius, Duration, Depth, TFOPWG Disposition, TEV Disposition



# CTOI_Review_FP headers: TIC, CTOI, Period (exofop), Period (TEV), TEV Disposition [5]
# exofop_edited: TIC, CTOI, Transit Epoch, Period (exofop), Planet Radius, Duration, Depth, TFOPWG Disposition [8]


master_header = ['TIC ID', 'CTOI ID', 'Transit Epoch', 'Period (exofop)', 'Period (TEV)', 'Planet Radius', 'Duration',
'Depth', 'TFOPWG Disposition', 'TEV Disposition', 'Notes', 'CTOI Category']


exofop_header = ['TIC', 'CTOI', 'Transit Epoch', 'Period', 'Duration', 'Depth', 'Planet Radius', 'Notes', 'TFOPWG Disposition', 'CTOI Designation']
exofop_false_positive.append(exofop_header)




for index, row in exofop_df.iterrows():
    if row['TFOPWG Disposition'] == 'FP':
        exofop_row_values = [
            int(row['TIC ID']),
            row['CTOI'],
            row['Transit Epoch (BJD)'],
            row['Period (days)'],
            row['Duration (hours)'],
            row['Depth (mmag)'],
            row['Planet Radius (R_Earth)'],
            row['Notes'],
            row['TFOPWG Disposition']
        ]

        exofop_row_values.append('Likely FP')

        exofop_false_positive.append(exofop_row_values)



# for index, row in ctoi_review_fp_df.iterrows():
#     if row['TEV Disposition'] == category1 or row['TEV Disposition'] == category2:
#         row_values = [
#             int(row['TIC']),
#             row['CTOI'],
#             row['TEV Disposition'],
#             row['Notes']
#         ]
#         row_values.append('Likely FP')
#         ctoi_review_false_positives.append(row_values)





ctoi_file = 'ctoi_false_postive.csv'
exofop_fp_file = 'exofop_fp_tester.csv'




# Now, merge those two file together
# Read both csv files both from ctoi list and the exofop one

ctoi_df = pd.read_csv(ctoi_file)
exofop_df = pd.read_csv(exofop_fp_file)



common_columns = ['TIC', 'CTOI', 'Notes', 'CTOI Category']

# Rename the title of the column name in the EXOFOP false positive list
exofop_df.rename(columns={'TIC ID': 'TIC'}, inplace=True)




# Now, merge these two
# merged_df = pd.merge(ctoi_df, exofop_df, on=['TIC', 'CTOI', 'Notes', 'CTOI Category'], how='inner')



# save the merged pandas dataframe into a csv file
# merged_df.to_csv('Mereged_false_positives.csv', index=False)

# Merging error.
#
# with open(ctoi_file, 'w', newline='') as ctoi_fp_file:
#     writer = csv.writer(ctoi_fp_file)
#     writer.writerows(ctoi_review_false_positives)


with open(exofop_fp_file, 'w', newline='') as exofop_fp:
    writer = csv.writer(exofop_fp)
    writer.writerows(exofop_false_positive)
