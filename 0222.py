import pickle
# with open('C:/Users/hyeyoung/PycharmProjects/test/mult2/korean_audiotext_transformer/mydataset/train.pkl','rb') as fr:
#     train_data=pickle.load(fr)
with open('./train.pkl','rb') as fr:
    train_data=pickle.load(fr)

print(len(train_data)) #6349이다.
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
label=[LABEL_DICT[e] for e in train_data['multimodal_emotion']]
train_data['multimodal_emotion']=label
train_data.drop(['Episode_no','Episode_sequence','audio','person_id'],axis=1,inplace=True)

print(train_data.columns)
train_data.to_csv('train.tsv',sep='\t')

import pandas as pd
dataset=pd.read_csv('train.tsv',delimiter='\t')
print(dataset) #Unnamed:0, text_script, multimodal_emotion

print(type(dataset)) #dataframe이다.
print(dataset.columns) #Unnamed:0, multimodal_emotion, text_script

#Unnamed:0을 제거하자.
dataset.drop(['Unnamed: 0'],axis=1,inplace=True)
print(dataset.columns) #multimodal_emotion, text_script
print(dataset.iloc[0])
dataset['multimodal_emotion']==0


# dataset.to_csv('train_v1.tsv',sep='\t')
# train_v1_df=pd.read_csv('train_v1.tsv',delimiter='\t')
# print(train_v1_df)

