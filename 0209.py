from pydub import AudioSegment
import pandas as pd

def extract_audio_feature(wav_file):
    audio=AudioSegment.from_wav(wav_file)
    audio=audio.set_channels(1)
    audio=audio.get_array_of_samples()
    print(type(audio))
    return audio

#1부터1000 for i in range(1001)
import os
os.listdir('F:/wav_file')
audio_feature_list_2000_new=[]
j=1
j_list=[]
for j in range(1,1001): #1부터 1000
    if j==3193 or j==3290 or j==3251 or j==3337 or j==2005:
        continue
    ii=[i for i in os.listdir('F:/wav_file') if 'clip'+str(j)+'_' in i]
    print(ii)
    print('길이:',len(ii)) #길이 나옴.
    print('j',j)
    j_list.append(j)
    print()
    for k in range(len(ii)):
        wav_cut_file='F:/wav_file/'+ii[k]
        audio_feature=extract_audio_feature(wav_cut_file)
        audio_feature_list_2000_new.append(audio_feature)
    j+=1
#--------------------------------
print(len(audio_feature_list_2000_new)) #13422 ->딱 맞음.

df_audio_1to1000=pd.DataFrame({'audio':audio_feature_list_1000_new})
df_audio_1to1000.to_csv('D:/json_file_list/1to1000_audio.csv')

#1001부터 2000
#누락 확인
import os
os.listdir('F:/wav_file')
audio_feature_list_2000_=[]
j=1
for j in range(1001,2001): #1부터 5600
    ii=[i for i in os.listdir('F:/wav_file') if 'clip'+str(j)+'_' in i]
    print(ii)
    print('길이:',len(ii)) #이것 길이 나옴.
    print('j',j)
    print()
    for k in range(len(ii)):
        wav_cut_file='F:/wav_file/'+ii[k]
        audio_feature=extract_audio_feature(wav_cut_file)
        audio_feature_list_2000_.append(audio_feature)
    j+=1

df_audio_1000to2000=pd.DataFrame({'audio':audio_feature_list_2000_})
df_audio_1000to2000.to_csv('D:/json_file_list/1000to2000_audio_.csv')

print(len(audio_feature_list_2000_))
#---------------------------------------------------
from pydub import AudioSegment
import pandas as pd

def extract_audio_feature(wav_file):
    audio=AudioSegment.from_wav(wav_file)
    audio=audio.set_channels(1)
    audio=audio.get_array_of_samples()
    print(type(audio))
    return audio

import os
os.listdir('F:/wav_file')
audio_feature_list_3000=[]
j=1
for j in range(1907,1985): #1부터 5600
    if j==3193 or j==3290 or j==3251 or j==3337 or j==2005:
        continue
    ii=[i for i in os.listdir('F:/wav_file') if 'clip'+str(j)+'_' in i]
    print(ii)
    print('길이:',len(ii)) #이것 길이 나옴.
    print('j',j)
    print()
    for k in range(len(ii)):
        wav_cut_file='F:/wav_file/'+ii[k]
        audio_feature=extract_audio_feature(wav_cut_file)
        audio_feature_list_3000.append(audio_feature)
    j+=1

df_audio_2000to3000=pd.DataFrame({'audio':audio_feature_list_3000})
df_audio_2000to3000.to_csv('D:/json_file_list/2000to3000_audio.csv')

#------------------------
from pydub import AudioSegment
import pandas as pd
import os

def extract_audio_feature(wav_file):
    audio=AudioSegment.from_wav(wav_file)
    audio=audio.set_channels(1)
    audio=audio.get_array_of_samples()
    #print(type(audio))
    return audio

#os.listdir('F:/wav_file')
audio_feature_list_5600=[]
j=1
for j in range(1,5601): # j-> Episode_no 컬럼
    if j==2005 or j==3038 or j==3109 or j==3166 or j==3173 or j==3174 or j==3177 or j==3193 or j==3251 or j==3270 or j==3273 or j==3274 or j==3288 or j==3289 or j==3290 or j==3291 or j==3295 or j==3296 or j==3299 or j==3301 or j==3305 or j==3312 or j==3315 or j==3316 or j==3320 or j==3331 or j==3333 or j==3337 or j==3356 or j==3366 or j==3401 or j==3402 or j==3405 or j==3406 or j==3408 or j==3412 or j==3414 or j==3415 or j==3416 or j==3427 or j==3429 or j==3435 or j==3437 or j==3440:
        continue
    ii=[i for i in os.listdir('F:/wav_file_cut') if 'clip'+str(j)+'_' in i]
    print(ii)
    # print('길이:',len(ii))
    # print('j',j)
    # print()
    for k in range(len(ii)): #k-> Episode_sequence 컬럼
        wav_cut_file='F:/wav_file_cut/'+ii[k]
        audio_feature=extract_audio_feature(wav_cut_file)
        audio_feature_list_5600.append(audio_feature)
    j+=1

df_audio_1to5600=pd.DataFrame({'Episode_no':j,'Episode_sequence':k+1,'audio':audio_feature_list_5600})
#여기까지 실행함.
print(len(df_audio_1to5600))

df_audio_1to5600.to_pickle('D:/json_file_list/1to5600_audio_new.pkl')

#데이터 로드
data=pd.read_pickle('D:/json_file_list/1to5600_audio_new.pkl')



