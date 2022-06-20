import json
import csv
import json
import pandas as pd

#for t in range(1,5201):
#for t in range(5201,5600):
for t in range(50,51):
    a=str(t)
    #with open('D:\\json_file_list\\clip_'+a+'.json','r',encoding='utf-8-sig') as input_file,open('clip_'+a+'_final_out3.csv','w',newline='',encoding='utf-8-sig') as output_file:
    with open('D:\\json_file_list\\clip_' + a + '.json', 'r', encoding='utf-8-sig') as input_file, open('D:\\json_file_list\\clip_' + a + '_final_out3.csv', 'w', newline='', encoding='cp949') as output_file:
    #f=open('D:\\json_file_list\\clip_'+t+'.json',encoding='UTF-8')
#f=open('clip_2.json','rt', encoding='UTF-8')
        data=json.load(input_file)
        #data=json.load(input_file.replace("\'","\""))
        #print(data.type())
        #data=data.replace("\'","\"")
#print(data)
        frame_num=int(data['nr_frame'])
#type(frame_num) #int임
        i=0
        script_start1 = []
        script_start2 = []
        for i in range(frame_num):
            try:
                j=str(i)
                script_start1.append(data['data'][j]['1']['text']['script_start'])
        #print(data['data'][j]['1']['text']['script']) #사람1
        #print(data['data'][j]['2']['text']['script']) #사람2
        #print(i)
                i+=1
            except:
                pass
        # i=0
        # for i in range(frame_num):
        #     try:
        #         j=str(i)
        #         script_start2.append(data['data'][j]['2']['text']['script_start']) #사람1
        # #print(data['data'][j]['2']['text']['script']) #사람2
        # #print(i)
        #         i+=1
        #     except:
        #         pass
        k=0
        for k in range(frame_num):
            try:
                p=str(k)
                script_start2.append(data['data'][p]['2']['text']['script_start'])
                k+=1
            except:
                pass
        script_start1=set(script_start1)
        script_start2=set(script_start2)
    #print(set(script_start1))
    #print(set(script_start2))
#with open('clip_1.json','r',encoding='utf-8') as input_file,open('clip_1_final_11081.csv','w',newline='') as output_file:
#for t in range(1,5201):
    #with open('D:\\json_file_list\\clip_'+t+'.json','r',encoding='UTF-8') as input_file,open('clip_'+t+'_final_1110_5.csv','w',newline='',encoding='UTF-8') as output_file:
    #data=json.load(input_file)
    #data=json.load(f)
        fo=csv.writer(output_file)

    #csv파일에 header를 추가한다.
        fo.writerow(['age','gender','person_id','text_emotion','text_valence','text_arousal','sound_emotion','sound_valence','sound_arousal',
                'multimodal_emotion','multimodal_valence','multimodal_arousal','text_strategy','text_script_end','text_script_start','text_script',
                'text_intent'])
    #for datum in data:
    #사람1
        x=0 #i대신 x 넣고, j 대신 y 넣자.
    #for i in range(len(n1)):
        for x in range(len(script_start1)):
            try:
                y=str(script_start1[x])
                fo.writerow([
                        data['actor']['1']['age'],
                        data['actor']['1']['gender'],
                        data['data'][y]['1']['person_id'],
                        data['data'][y]['1']['emotion']['text']['emotion'],
                        data['data'][y]['1']['emotion']['text']['valence'],
                        data['data'][y]['1']['emotion']['text']['arousal'],
                        data['data'][y]['1']['emotion']['sound']['emotion'],
                        data['data'][y]['1']['emotion']['sound']['valence'],
                        data['data'][y]['1']['emotion']['sound']['arousal'],
                        data['data'][y]['1']['emotion']['multimodal']['emotion'],
                        data['data'][y]['1']['emotion']['multimodal']['valence'],
                        data['data'][y]['1']['emotion']['multimodal']['arousal'],
                        data['data'][y]['1']['text']['strategy'],
                        data['data'][y]['1']['text']['script_end'],
                        data['data'][y]['1']['text']['script_start'],
                        data['data'][y]['1']['text']['script'],
                        data['data'][y]['1']['text']['intent']])
                x+=1
            except:
                pass
    #사람2
    #n2=[141,331,531,741,966] #사람2의 script_start
        l=0
        for l in range(len(script_start2)):
            try:
                m=str(script_start2[l])
                fo.writerow([
                        data['actor']['2']['age'],
                        data['actor']['2']['gender'],
                        data['data'][m]['2']['person_id'],
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
            except:
                pass
    df_process=pd.read_csv('D:\\json_file_list\\clip_' + a + '_final_out3.csv',encoding='cp949')
    df_process.drop_duplicates(subset=None,keep='first',inplace=True,ignore_index=True)
    #df_process.to_csv('clip_'+a+'csvfile_final.csv',encoding='cp949')
    df_process.to_csv('clip_' + a + 'csvfile_final0104_505000.csv', encoding='cp949')
    t+=1
