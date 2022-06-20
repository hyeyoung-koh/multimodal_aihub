import pickle
with open('C:/Users/hyeyoung/PycharmProjects/test/mult2/korean_audiotext_transformer/mydataset/test.pkl','rb') as fr:
    test_data=pickle.load(fr)

print(len(test_data)) #6349이다.
LABEL_DICT={
    'angry':0,
    'neutral':1,
    'fear':2,
    'contempt':3,
    'sad':4,
    'surprise':5,
    'dislike':6,
    'happy':7
}
label=[LABEL_DICT[e] for e in test_data['multimodal_emotion']]
test_data['multimodal_emotion']=label
test_data['multimodal_emotion']
test_data.drop(['Episode_no','Episode_sequence','audio','person_id'],axis=1,inplace=True)

print(test_data.columns)

test_data.to_csv('test.tsv',sep='\t')

import pandas as pd
dataset=pd.read_csv('test.tsv',delimiter='\t')
print(dataset)
#------------------
dataset.drop(['Unnamed: 0'],axis=1,inplace=True)
print(dataset) #Unnamed:0, text_script, multimodal_emotion

print(type(dataset)) #dataframe이다.
print(dataset.columns) #Unnamed:0, multimodal_emotion, text_script

#Unnamed:0을 제거하자.
dataset.drop(['Unnamed: 0'],axis=1,inplace=True)
print(dataset.columns) #multimodal_emotion, text_script
print(dataset.iloc[0])

# dataset.to_csv('train_v1.tsv',sep='\t')
# train_v1_df=pd.read_csv('train_v1.tsv',delimiter='\t')
# print(train_v1_df)

