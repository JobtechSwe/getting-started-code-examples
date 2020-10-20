# counts and extracts information from ads with occupation id 5899 (ssyk level 5)

import json

filename = 'data/2019.json'

with open(filename) as f:
    ads = json.load(f)

bibliotekarie_kod = '5899'
ads_bibliotekarie = []

for ad in ads:
    if ad['occupation']['legacy_ams_taxonomy_id'] == bibliotekarie_kod:
        ads_bibliotekarie.append(ad)

print('total nr ads for year 2019 =>', len(ads))
print('nr ads with occupation id', bibliotekarie_kod, '=>', len(ads_bibliotekarie))

filename_out = 'output.txt'

with open(filename_out,'w') as f:
    for ad in ads_bibliotekarie:
        f.write(ad['headline'] + '\n')
        f.write(ad['publication_date'] + '\n')
        f.write('antal platser: ' + str(ad['number_of_vacancies']) + '\n')
        f.write(ad['description']['text'] + '\n\n')