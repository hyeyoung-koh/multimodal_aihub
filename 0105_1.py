import csv
import json
import pandas as pd

for t in range(50,51):
    a=str(t)
    with open('D:\\json_file_list\\clip_' + a + '.json', 'r', encoding='utf-8-sig') as input_file, open('D:\\json_file_list\\clip_' + a + '_final_20220105a.csv', 'w', newline='', encoding='cp949') as output_file:
        fo=csv.writer(output_file)
        fo.writerow(['person_id','text_emotion','text_valence','text_arousal','sound_emotion','sound_valence','sound_arousal',
                     'multimodal_emotion','multimodal_valence','multimodal_arousal','text_strategy','text_script_end','text_script_start','text_script','text_intent'])
        data=json.load(input_file)
        frame_num = int(data['nr_frame'])
        for i in range(1,frame_num):
            try:
                j = str(i)
                mydict=data['data'][j]
                # while (key!=1 or key!=2 or key!=3):
                #     for key,value in mydict.items():
                for key,value in mydict.items():
                    # for i in range(len(mydict)):
                    #     for m in key:
                    #         if m=='1':
                    for i in range(len(mydict)):
                        fo.writerow([data['data'][j][key]['person_id'],
                                data['data'][j][key]['emotion']['text']['emotion'],
                                data['data'][j][key]['emotion']['text']['valence'],
                                data['data'][j][key]['emotion']['text']['arousal'],
                                data['data'][j][key]['emotion']['sound']['emotion'],
                                data['data'][j][key]['emotion']['sound']['valence'],
                                data['data'][j][key]['emotion']['sound']['arousal'],
                                data['data'][j][key]['emotion']['multimodal']['emotion'],
                                data['data'][j][key]['emotion']['multimodal']['valence'],
                                data['data'][j][key]['emotion']['multimodal']['arousal'],
                                data['data'][j][key]['text']['strategy'],
                                data['data'][j][key]['text']['script_end'],
                                data['data'][j][key]['text']['script_start'],
                                data['data'][j][key]['text']['script'],
                                data['data'][j][key]['text']['intent']]
                                )
            except:
                pass

    df_process=pd.read_csv('D:\\json_file_list\\clip_' + a + '_final_20220105a.csv',encoding='cp949')
    df_process.drop_duplicates(subset=None,keep='first',inplace=True,ignore_index=True)
    #df_process.to_csv('clip_'+a+'csvfile_final.csv',encoding='cp949')
    df_process.to_csv('D:\\json_file_list\\clip_' + a + 'csvfile_20220105_00.csv', encoding='cp949')
    t+=1

