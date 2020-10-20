import numpy as np
import json
import visualize
import pickle

load_result = True
filename_res = 'ssyk2vector.pkl'

if load_result == False:
    years = [2019]
    filepath = 'data/'

    filenames = [filepath + str(y) + '.json' for y in years]

    all_competencies_by_ssyk = {}

    with open(filepath + 'occId_2_ssyk2012.json') as f:
        occ2ssyk = json.load(f)

    all_competencies = {}

    for filename in filenames:

        with open(filename) as f:
            ads = json.load(f)
            print('loaded', filename)

        for ad in ads:
            if 'enriched_candidates' in ad:
                
                occ_id = ad['occupation']['legacy_ams_taxonomy_id']

                if occ_id in occ2ssyk:
                    ssyk = occ2ssyk[occ_id]
                    
                    if ssyk not in all_competencies_by_ssyk:
                        all_competencies_by_ssyk[ssyk] = {}
                        
                    for c in ad['enriched_candidates']['competencies']:
                        if c['concept_label'] not in all_competencies_by_ssyk[ssyk]:
                            all_competencies_by_ssyk[ssyk][c['concept_label']] = 0
                        if c['concept_label'] not in all_competencies:
                            all_competencies[c['concept_label']] = 0
                        
                        all_competencies_by_ssyk[ssyk][c['concept_label']] += 1
                        all_competencies[c['concept_label']] += 1

    # sort
    print('sorting')
    comps_sorted = {}
    sorted_competencies = sorted(all_competencies.items(), key=lambda kv: kv[1],reverse=True)

    print('calculating vectors')
    comp2index = {}
    for i,s in enumerate(sorted_competencies):
        comp2index[s[0]] = i

    ssyk2vector = {}
    for ssyk in all_competencies_by_ssyk:
        ssyk2vector[ssyk] = np.zeros(len(sorted_competencies))

        for n in all_competencies_by_ssyk[ssyk].keys():
            ssyk2vector[ssyk][comp2index[n]] = all_competencies_by_ssyk[ssyk][n]
        
        # normalize
        tot = 1.0*np.sum(ssyk2vector[ssyk])
        ssyk2vector[ssyk] = ssyk2vector[ssyk] / tot

    with open(filename_res,'wb') as f:
        pickle.dump(ssyk2vector,f, protocol=pickle.HIGHEST_PROTOCOL)#np.save(f,ssyk2vector)
else:
    with open(filename_res,'rb') as f:
        ssyk2vector = pickle.load(f)#ssyk2vector = np.load(f)#, allow_pickle=True)

visualize.visualize_correlation_matrix(ssyk2vector)