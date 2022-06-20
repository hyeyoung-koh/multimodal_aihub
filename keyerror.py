path='C:/Users/hyeyoung/PycharmProjects/test/mult2/korean_audiotext_transformer/mydataset'
file=path+'/train.pkl'

import pandas as pd
import pickle5 as pickle
data=open(file,'rb')
pickle_data=pickle.load(data)
print(len(pickle_data)) #6349
print(pickle_data[4105])
pickle_data.iloc[0]
pickle_data.iloc[4105]
pickle_data.iloc[4106]

import pandas as pd
mergeAll=pd.read_csv('C:/Users/hyeyoung/PycharmProjects/aihub/mergeAll.tsv',delimiter='\t')
print(len(mergeAll)) #79346
print(type(mergeAll)) #dataframe
print(mergeAll['multimodal_emotion'])
#mergeAll['multimodal_emotion']==6
mergeAll['multimodal_emotion'].value_counts()

print(type(mergeAll['multimodal_emotion'].iloc[0])) #numpy.int64임.
sort_emotion=mergeAll.sort_values(by=['multimodal_emotion'],ascending=True).head()
sort_emotion['multimodal_emotion'].head(20)

