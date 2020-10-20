## Python examples historical jobs

To run examples, download data from https://jobtechdev.se/docs/apis/historical/ and extract into the data folder.  
To be able to run the examples which rely on access to an api ([Taxonomy](https://jobtechdev.se/en/docs/apis/taxonomy/) and/or [JobAd Enrichments](https://jobtechdev.se/en/docs/apis/enrich/)), an api key should be put in the file [config.json](config.json). This key can be retrieved from https://apirequest.jobtechdev.se.

### [example_bibliotekarie.py](example_bibliotekarie.py)
Description: For year 2019, filter out all ads in the occupation 'Bibliotekarie' (occupation name with id 5899).

Uses: [Historical Jobs](https://jobtechdev.se/docs/apis/historical/)

Output:
```
antal annonser totalt år 2019 => 640257
antal annonser med id 5899 => 667
```

### [example_remote_work.py](example_remote_work.py)
Description: For years 2010-2020, filter out ads which contains the substring 'distans' during Aug 15-Sept 14.

Uses: [Historical Jobs](https://jobtechdev.se/docs/apis/historical/), [Taxonomy](https://jobtechdev.se/en/docs/apis/taxonomy/) (to do occupation name -> ssyk level 4)

Output: 
```
counts ads in date range (8, 15) to (9, 14) => {2010: 26385, 2011: 33735, 2012: 34090, 2013: 34167, 2014: 41235, 2015: 52198, 2016: 63842, 2017: 63773, 2018: 60832, 2019: 51706, 2020: 36642}
with keywords ['distans'] => {2010: 87, 2011: 129, 2012: 168, 2013: 147, 2014: 239, 2015: 257, 2016: 407, 2017: 340, 2018: 541, 2019: 400, 2020: 483}

```
![](output_remote_work.png | width=400px)

### [example_ssyk_similarities.py](example_ssyk_similarities.py)
Description: Calculate and visualize the statistical similarities between different occupations (of ssyk level 4). Similarity between two occupations is set as the correlation between their normalized counts of competencies, occupation titles and traits.

Uses: [Historical Jobs](https://jobtechdev.se/docs/apis/historical/), [Taxonomy](https://jobtechdev.se/en/docs/apis/taxonomy/), [JobAd Enrichments](https://jobtechdev.se/en/docs/apis/enrich/)

Output: Ordered similarity matrix and dendogram.

Zoomed sub-part: 