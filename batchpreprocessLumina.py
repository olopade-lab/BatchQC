#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:07:39 2020

@author: arvindkrishnan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:39:53 2020

@author: arvindkrishnan
"""
import pandas as pd 



data=pd.read_csv('./olopade.data.7.3.20.csv')


samples=pd.read_csv('./salmon_merged_gene_counts.csv')
samples=samples.columns[1:]
samples=samples.to_list()

key=pd.read_csv('./Sampleskey.csv')
key1=key['sampleID1'].tolist()

data=data[data['study_id'].isin(key1)]
data=data[data['analyte']=='rna']

#data=data[data['order_type']=='T']
#data=data[data['relationship']=='S']
#data=df[df['product']=='R']




data=data.drop(['order_type', 'relationship', 'product', 'panel', 'project',
       'pipeline_version', 'status_code','workflow',
       'assay.x', 'analyte', 'match_type.x', 'cancer_cohort', 'status',
       'created', 'updated', 'intent', 'is_qc4', 'is_control',
       'control_sample_type', 'msi_status_canonical_name', 'tmb',
       'race_concept_canonical_name', 'ethnicity_canonical_name',
       'est_immune_cells', 'est_b_cells', 'est_cd4_cells', 'est_cd8_cells',
       'est_mac_cells', 'est_nk_cells', 'tumor_purity', 'ENSG00000082175',
       'ENSG00000091831', 'ENSG00000141736', 'study_id',
       'study_sample_id', 'tumor_normal', 'assay.y', 'path review decision',
       'Rej. reason', 'QNS Type', 'QNS Date', 'match_type.y', 'qc_status',
       'QB DNA', 'QB RNA', 'DNA/RNA', 'Notes', 'X17'], axis=1
       )

df=pd.read_csv('./lumina.txt', header=None)
df=df[0].tolist()

batch=pd.DataFrame(columns=['sample_id','Instrument_name','Run_id','Flowcell_lane', 'InstrumentAndFlowcellLane', 'date', 'type', 'ER', 'PR', 'HER2'], 
                   #index=['sample_id']
                   )

sep='/'
for i in range(1,len(df),2):
    sep='/'
    df[i]=df[i].split(sep)[1]
    sep='.'
    df[i]=df[i].split(sep)[0]
    df[i]=df[i][0:len(df[i])-2]

for i in range(0,len(df),4):
    sep=':'
    listA=df[i].split(sep)
    tobatch= listA[0] + listA[1] + listA[3]
    s=data[data['isolate_id']==df[i+1][0:-11]]['exp_id']
    date=s[s.index[0]][0:6]
    Type=data[data['isolate_id']==df[i+1][0:-11]]['ER'].dropna()
    ER=data.loc[Type.index[0]]['ER']
    PR=data.loc[Type.index[0]]['PR']
    HER2=data.loc[Type.index[0]]['ERBB2']
    
    Type=data.loc[Type.index[0]]['ER']+data.loc[Type.index[0]]['PR']+data.loc[Type.index[0]]['ERBB2']

    toappend=pd.DataFrame([[df[i+1],listA[0], listA[1], listA[3], listA[0]+'_'+listA[3], date, Type, ER, PR, HER2]],columns=['sample_id','Instrument_name','Run_id','Flowcell_lane','InstrumentAndFlowcellLane', 'date', 'type', 'ER', 'PR', 'HER2'], index=['sample_id'])
    batch=batch.append(toappend)



# num=1
# for i in range(0,len(batch)):
#     val=batch.iloc[i,4]
#     if type(val)!=int:
#         for j in range(0,len(batch)):
#             if batch.iloc[j,4]==val:
#                 batch.iloc[j,4]=num
#         num+=1

#batch=batch.set_index('sample_id')
batch.to_csv('./metadata.csv', index=False)