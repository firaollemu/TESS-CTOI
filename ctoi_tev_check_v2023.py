import numpy as np
import pandas as pd
import datetime
from scipy.special import erfcinv
from datetime import date

date = date.today()

def ephemeris_match(p1, t1, p2, t2):
    '''From Coughlin paper - https://arxiv.org/pdf/1401.1240.pdf. p1, t1 are periods and epoch of cTOIs while p2, t2 are values for TCEs'''
    if np.isnan(p1) == True:
        #catches single case errors where period is NaN
        sp = 0
        st = 0
    else:
        dp = (p1 - p2) / p1
        dt = (t1 - t2) / p1

        try:
            dpp = np.abs(dp - round(dp))
            dtp = np.abs(dt - round(dt))
            sp = np.sqrt(2) * erfcinv(dpp)
            st = np.sqrt(2) * erfcinv(dtp)
        except OverflowError:
            print ("A wild zero denominator has appeared!")
            sp = 0
            st = 0
    return sp, st

exofop = pd.read_csv('%s/CTOIs_to_review%s.csv' % (date, date), delimiter=',') # csv with exofop data, skiprows # will differ
col_f = exofop.columns
tev = pd.read_csv('%s/atlas_ctois%s_review.csv' % (date, date), delimiter = ',') # atlas signal csv from TEV, ask willie
col_t = tev.columns

tic_f = np.array(exofop['TIC ID'])
ctoi_f = np.array(exofop['CTOI'])
per_f = np.array(exofop['Period (days)']) #includes NaNs for single targets
t0_f = np.array(exofop['Transit Epoch (BJD)'])
tmag_f = np.array(exofop['TESS Mag'])
user = np.array(exofop['User'])

#From my CTOI code
tic_t = np.array(tev['TIC ID'])
per_t = np.array(tev['Period (days)'])
t0_t = np.array(tev['Transit Epoch (BJD)'])
comments_t = np.array(tev['Comments'])

ind_f = [] # indices of matches
ind_t = []

non_match_f = []
non_match_t = []
non_match_per = []
non_match_disp = []
non_match_toi = []

no_tev = []
singles = []

for i, p1, t1 in zip(ctoi_f, per_f, t0_f): # match exofop TIC+period string to tev
	match_flag = False
	t = int(i)
	if t in tic_t:
		tm = np.argwhere(tic_t == t)[:,0]
		for j in tm:
			print("test 2")
			p2, t2 = per_t[j], t0_t[j]
			if not match_flag:
				try:
					print("test 3")
					sigs = ephemeris_match(p1, t1, p2, t2)
					if sigs[0] > 2 and sigs[1] > 1: # should be 2 and 1 minimum, respectively
						print("test 4")
						match_flag = True
						n = list(ctoi_f).index(i)
						ind_f.append(n)
						ind_t.append(j)
					else:
						print("test 5")
						if j == tm[-1]:
							n = list(ctoi_f).index(i)
							non_match_f.append(n)
							non_match_t.append(j)
							per_nm = [round(per_t[k], 4) for k in tm]
							non_match_per.append(str(per_nm).strip('[').strip(']'))
							#dp = [tev['toi_disposition'][k] for k in tm]
							#non_match_disp.append(str(dp).strip('[').strip(']'))
							#tois = [tev['full_toi_id'][k] for k in tm]
							#non_match_toi.append(str(tois).strip('[').strip(']'))
				except ValueError:
					singles.append(i)
	else:
		no_tev.append(i)

print ("Singles: ", singles)
mtic = tic_f[ind_f] # TIC ids of matches
mctoi = ctoi_f[ind_f]
mper = per_f[ind_f]
mtmag = tmag_f[ind_f]
muser = user[ind_f]
mper_t = per_t[ind_t]
mcom = comments_t[ind_t]
#mdisp = np.array(tev['toi_disposition'])[ind_t]
#mtoi = np.array(tev['full_toi_id'])[ind_t]
#mdisp[[type(m) != str for m in mdisp]] = '' # replace nans with empty strings

f = np.array([mctoi, mper, mper_t, mtmag, mcom, muser])
#sf = sorted(f, key = lambda x: x[4])[::-1] # sort by dispositions, reverse alphabetical

now = datetime.datetime.now()
year, month, day = now.year, now.month, now.day
filename = 'Exofop_CTOI_TEV_match_%d-%02d-%02d.csv' % (year, month, day) # include date in filename to lower risk of accidental overwrite

df = pd.DataFrame(columns = ['TIC','Period (exofop)', 'Period (TEV)', 'TESS mag', 'Public Comment', 'User'])
df['TIC'] = mctoi
df['Period (exofop)'] = mper
df['Period (TEV)'] = mper_t
df['TESS mag'] = mtmag
df['Public Comment'] = mcom
df['User'] = muser
df.to_csv(filename, header = True, index = False)

# non-matches

nmtic = tic_f[non_match_f] # TIC ids of non matches
nmctoi = ctoi_f[non_match_f]
nmper = per_f[non_match_f]
nmtmag = tmag_f[non_match_f]
nmuser = user[non_match_f]

#f = np.array([nmctoi, nmper, np.array(non_match_per), nmtmag, np.array(non_match_disp), np.array(non_match_toi), nmuser]).T

now = datetime.datetime.now()
year, month, day = now.year, now.month, now.day
filename = 'Exofop_CTOI_TEV_nonmatch_%d-%02d-%02d.csv' % (year, month, day) # include date in filename to lower risk of accidental overwrite

df = pd.DataFrame(columns = ['TIC', 'Period (exofop)', 'Period (TEV)', 'TESS mag', 'User'])
df['TIC'] = nmctoi
df['Period (exofop)'] = nmper
df['Period (TEV)'] = np.array(non_match_per)
df['TESS mag'] = nmtmag
df['User'] = nmuser
df.to_csv(filename, header = True, index = False)

# ctoi tics not in tev

f = np.array(no_tev).T
filename = 'Exofop_CTOI_no-TEV_%d-%02d-%02d.txt' % (year, month, day) # include date in filename to lower risk of accidental overwrite

np.savetxt(filename, f, header = 'TIC', fmt = '%0.2f')
