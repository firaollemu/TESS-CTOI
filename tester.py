import pandas as pd
import csv
import numpy as np

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


exofop_header = ['TIC', 'CTOI', 'Transit Epoch', 'Period', 'Duration',
                 'Depth', 'Planet Radius', 'Notes', 'TFOPWG Disposition', 'CTOI Designation']
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

#         exofop_false_positive.append(exofop_row_values)


ctoi_header = ['TIC', 'CTOI', 'Period (exofop)', 'Period (TEV)',
               'Notes', 'Public comment', 'TEV Disposition', 'CTOI Designation']
ctoi_review_false_positives.append(ctoi_header)

for index, row in ctoi_review_fp_df.iterrows():
    ctoi_row_values = [
        row['TIC'],
        row['CTOI'],
        row['Period (exofop)'],
        row['Period (TEV)'],
        row['Notes'],
        row['Public comment'],
        row['TEV Disposition']
    ]
    ctoi_row_values.append('Likely FP')

    ctoi_review_false_positives.append(ctoi_row_values)


ctoi_file = 'ctoi_false_postive.csv'
exofop_fp_file = 'exofop_fp_tester.csv'


# Now, merge those two file together
# Read both csv files both from ctoi list and the exofop one

ctoi_df = pd.read_csv(ctoi_file)
exofop_df = pd.read_csv(exofop_fp_file)

# Common headers
master_header = ['TIC ID', 'CTOI ID', 'Transit Epoch',
                 'Period (exofop)', 'Period (TEV)', 'Planet Radius', 'Duration', 'Depth', 'TFOPWG Disposition', 'TEV Disposition', 'Notes', 'CTOI Category']

master_df = pd.DataFrame(columns=master_header)  # make the column a header

master_list = [master_header]

master = 'master_test.csv'

with open(master, 'w', newline='') as m:
    writer = csv.writer(m)
    writer.writerows(master_list)


# with open(ctoi_file, 'w', newline='') as ctoi_fp_file:
#     writer = csv.writer(ctoi_fp_file)
#     writer.writerows(ctoi_review_false_positives)
#
#
# with open(exofop_fp_file, 'w', newline='') as exofop_fp:
#     writer = csv.writer(exofop_fp)
#     writer.writerows(exofop_false_positive)
