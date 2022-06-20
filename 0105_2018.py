import csv
import json
import pandas as pd

for t in range(50,51):
    k=str(t)
    with open('D:\\json_file_list\\clip_' + k + '.json', 'r', encoding='utf-8-sig') as input_file, open('D:\\json_file_list\\clip_' + k + '_20220105^^;;.csv', 'w', newline='', encoding='cp949') as output_file:
        fo=csv.writer(output_file)
        fo.writerow(['episode_no','person_id','text_emotion','text_valence','text_arousal','sound_emotion','sound_valence','sound_arousal',
                     'multimodal_emotion','multimodal_valence','multimodal_arousal','text_strategy','text_script_end','text_script_start','text_script','text_intent'])
        data=json.load(input_file)
        frame_num = int(data['nr_frame'])

        dkeys=[]
        for key,value in data['data'].items():
            print(key)
            dkeys.append(key)
            for key2,value2 in data['data'][key].items():
                print(key2) #128,2,1/1296,2,1/1184,2,1/1679,2,1/255,2,1/1823,2,1/1799,2,1/

    for i in range(len(dkeys)):
        a=dkeys[i]
            i=0
            for i in range(len(dkeys)):
                a=dkeys[i]

                for num in data['data'][a].keys():
                    if 'text' in data['data'][a][num].keys():
                        fo.writerow([data['clip_id'],
                                 data['data'][a][num]['person_id'],
                                 data['data'][a][num]['emotion']['text']['emotion'],
                                 data['data'][a][num]['emotion']['text']['valence'],
                                 data['data'][a][num]['emotion']['text']['arousal'],
                                 data['data'][a][num]['emotion']['sound']['emotion'],
                                 data['data'][a][num]['emotion']['sound']['valence'],
                                 data['data'][a][num]['emotion']['sound']['arousal'],
                                 data['data'][a][num]['emotion']['multimodal']['emotion'],
                                 data['data'][a][num]['emotion']['multimodal']['valence'],
                                 data['data'][a][num]['emotion']['multimodal']['arousal'],
                                 data['data'][a][num]['text']['strategy'],
                                 data['data'][a][num]['text']['script_end'],
                                 data['data'][a][num]['text']['script_start'],
                                 data['data'][a][num]['text']['script'],
                                 data['data'][a][num]['text']['intent']])

    #output_file.close()
    #df_process=pd.read_csv('D:\\json_file_list\\clip_' + k + '_20220105_r.csv',encoding='cp949')
    #df_process.drop_duplicates(subset=None,keep='first',inplace=True,ignore_index=True)
    #df_process.to_csv('D:\\json_file_list\\clip_' + k + '_20220105fr.csv', encoding='cp949')
