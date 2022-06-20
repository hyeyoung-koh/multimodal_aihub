# import json
#
# #f=open('clip_1.json','rt', encoding='UTF8')
# f=open('clip_1.json','rt', encoding='UTF8')
# data=json.load(f)
# #print(data)
# print(data['situation'])
# print(data['video_size'])
# print(data['clip_id'])
# print(data['category'])
# print(data['data'])
# print(data['actor'])
# print(data['nr_frame'])

import csv
import json
import pandas as pd

for i in range(1,5201):
    j=str(i)
    f=open('D:\\json_file_list\\clip_'+j+'.json','rt',encoding='euc-kr')
    data=json.load(f)
    #i+=1
#print(data)
    frame_num=int(data['nr_frame'])
#type(frame_num) #int임
    m=0
    script_start1 = []
    script_start2 = []
    for m in range(frame_num):
        try:
            j=str(m)
            script_start1.append(data['data'][j]['1']['text']['script_start'])
        #print(data['data'][j]['1']['text']['script']) #사람1
        #print(data['data'][j]['2']['text']['script']) #사람2
        #print(i)
            m+=1
        except:
            pass
    s=0
    for s in range(frame_num):
        try:
            j=str(s)
            script_start2.append(data['data'][j]['2']['text']['script_start']) #사람1
        #print(data['data'][j]['2']['text']['script']) #사람2
        #print(i)
            s+=1
        except:
            pass
#print(set(script_start1))
#print(set(script_start2))
    my_set1=set(script_start1)
    my_set2=set(script_start2)
    my_list1=list(my_set1)
    my_list2=list(my_set2)
    #print(new_script_start1)
    #print(new_script_start2)
#with open('clip_1.json','r',encoding='utf-8') as input_file,open('clip_1_final_11081.csv','w',newline='') as output_file:
#h=0
#for h in range(1,5201):
#    u=str(h)
    with open('D:\\json_file_list\\clip_'+j+'.json','rt',encoding='UTF-8') as input_file,open('clip_'+j+'_final_1114.csv','w',newline='',encoding='euc-kr') as output_file:
        data=json.load(input_file)
        f=csv.writer(output_file)

    #csv파일에 header를 추가한다.
        f.writerow(['person_id','text_emotion','text_valence','text_arousal','sound_emotion','sound_valence','sound_arousal',
                'multimodal_emotion','multimodal_valence','multimodal_arousal','text_strategy','text_script_end','text_script_start','text_script',
                'text_intent'])
    #for datum in data:
    #사람1
        t=0
    #for i in range(len(n1)):
        for t in range(len(my_list1)):
            b=str(my_list1[t])
            f.writerow([data['data'][b]['1']['person_id'],
                        data['data'][b]['1']['emotion']['text']['emotion'],
                        data['data'][b]['1']['emotion']['text']['valence'],
                        data['data'][b]['1']['emotion']['text']['arousal'],
                        data['data'][b]['1']['emotion']['sound']['emotion'],
                        data['data'][b]['1']['emotion']['sound']['valence'],
                        data['data'][b]['1']['emotion']['sound']['arousal'],
                        data['data'][b]['1']['emotion']['multimodal']['emotion'],
                        data['data'][b]['1']['emotion']['multimodal']['valence'],
                        data['data'][b]['1']['emotion']['multimodal']['arousal'],
                        data['data'][b]['1']['text']['strategy'],
                        data['data'][b]['1']['text']['script_end'],
                        data['data'][b]['1']['text']['script_start'],
                        data['data'][b]['1']['text']['script'],
                        data['data'][b]['1']['text']['intent']])
            t+=1
    #사람2
    #n2=[141,331,531,741,966] #사람2의 script_start
        l=0
        for l in range(len(my_list2)):
            m=str(my_list2[l])
            f.writerow([data['data'][m]['2']['person_id'],
                        data['data'][m]['2']['emotion']['text']['emotion'],
                        data['data'][m]['2']['emotion']['text']['valence'],
                        data['data'][m]['2']['emotion']['text']['arousal'],
                        data['data'][m]['2']['emotion']['sound']['emotion'],
                        data['data'][m]['2']['emotion']['sound']['valence'],
                        data['data'][m]['2']['emotion']['sound']['arousal'],
                        data['data'][m]['2']['emotion']['multimodal']['emotion'],
                        data['data'][m]['2']['emotion']['multimodal']['valence'],
                        data['data'][m]['2']['emotion']['multimodal']['arousal'],
                        data['data'][m]['2']['text']['strategy'],
                        data['data'][m]['2']['text']['script_end'],
                        data['data'][m]['2']['text']['script_start'],
                        data['data'][m]['2']['text']['script'],
                        data['data'][m]['2']['text']['intent']
                    ])
            l+=1
    df_process=pd.read_csv('clip_'+j+'_final_1114.csv',encoding='utf-8')
    df_process.drop_duplicates(subset=None,keep='first',inplace=True,ignore_index=True)
    df_process.to_csv('clip_'+j+'_drop_duplicate_finalfinal.csv',encoding='utf-8-sig')
    print(j)
    j+=1