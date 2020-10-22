import os
import pandas as pd
import time

# import matplotlib.pyplot as plt
# from sklearn.preprocessing import StandardScaler
#
# import numpy as np

PROJ_DIR = os.path.abspath(os.path.join(os.getcwd(), "../../../../"))
DATA_DIR = os.path.abspath(os.path.join(PROJ_DIR, 'original'))
OUTPUT_DIR = os.path.abspath(os.path.join(PROJ_DIR, 'output'))

# read tsv data
train = pd.read_csv(DATA_DIR + '/prediction.tsv', sep='\t', header=0)
# shape: 4, 766
# index: sentence word prediction score
# compare the score between prediction and original data
difference_rate = abs((train['prediction'] - train['score']) / train['score'] * 100)
train['difference_rate'] = difference_rate
train.sort_values("difference_rate", ascending=False, inplace=True)
# Write into new file
train.to_csv(OUTPUT_DIR + '/error_detection_' + str(int(time.time())) + '.csv', index=False)

# show the difference_rate
# average_rate = np.mean(difference_rate)
# print(difference_rate)
# plt.bar(range(len(difference_rate)), difference_rate)
# plt.axhline(y=average_rate, color="red")
# plt.show()
