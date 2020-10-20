import json
import datetime

import numpy as np
import visualize


def in_date_range(date_string,start,end):

    month = int(date_string[5:7])
    day = int(date_string[8:10])

    if start <= (month,day) <= end:
        return True

    return False
    

def get_data(filenames, start_date, end_date):

    filtered_ads = []

    for filename in filenames:

        with open(filename) as f:
            ads = json.load(f)

        for ad in ads:
            if in_date_range(ad['publication_date'], start_date, end_date):
                filtered_ads.append(ad)

        print('.', end='')
        #print(len(filtered_ads),'ads after',filename)

    print('\n' + len(filtered_ads),'total filtered ads')

    return filtered_ads


years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
keywords = ['distans']

filepath = 'data/'
filenames = [filepath + str(y) + '.json' for y in years]

start_date = (8,15) # Aug 15
end_date = (9,14) # Sept 14

ads = get_data(filenames,start_date,end_date)

counts_keywords = { y: 0 for y in years }
counts_total = { y: 0 for y in years }

for i,ad in enumerate(ads):

    year = int(ad['publication_date'][0:4])
    counts_total[year] += 1 # counts total ads, could change 1 to nr positions to count total positions

    for word in keywords:
        try:
            if word in ad['description']['text'].lower() or word in ad['headline'].lower():
                counts_keywords[year] += 1
        except: # any missing values?
            print(ad['description']['text'])
            print(ad['headline'])

fractions = { y: 100.0 * counts_keywords[y] / counts_total[y] for y in years }

print('counts ads in date range', start_date, 'to', end_date, '=>', counts_total)
print('with keywords', keywords, '=>', counts_keywords)
print('fractions [%] =>', fractions)

visualize.visualize_result(fractions)