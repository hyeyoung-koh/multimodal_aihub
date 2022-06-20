import pickle5 as pickle
import pandas as pd
f1=open('./multTest.pkl','rb')

c1=pickle.load(f1)

print(len(c1)) #7936임.

c1.head(5)

c1.columns #Episode_no,Episode_sequence,audio,person_id,multimodal_emotion,text_script

train_df=c1.iloc[0:6349]
print(len(train_df)) #6349
dev_df=c1.iloc[6349:7143]
print(len(dev_df)) #794
test_df=c1.iloc[7143:7937]
print(len(test_df)) #793
#6349, 794, 793
#6349+794=
train_df.to_pickle('./train_df_pickle.pkl')
dev_df.to_pickle('./dev_df_pickle.pkl')
test_df.to_pickle('./test_df_pickle.pkl')

test_df.head(5)
test_df['multimodal_emotion']

test_df.columns
#Episode_no, Episode_sequence, audio, person_id, multimodal_emotion, text_script

