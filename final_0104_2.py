import csv
import json
import pandas as pd

for t in range(50,51):
    a=str(t)
    with open('D:\\json_file_list\\clip_' + a + '.json', 'r', encoding='utf-8-sig') as input_file, open('D:\\json_file_list\\clip_' + a + '_final_20220104.csv', 'w', newline='', encoding='cp949') as output_file:
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
                        if '1' in key:
                            fo.writerow([data['data'][j]['1']['person_id'],
                                data['data'][j]['1']['emotion']['text']['emotion'],
                                data['data'][j]['1']['emotion']['text']['valence'],
                                data['data'][j]['1']['emotion']['text']['arousal'],
                                data['data'][j]['1']['emotion']['sound']['emotion'],
                                data['data'][j]['1']['emotion']['sound']['valence'],
                                data['data'][j]['1']['emotion']['sound']['arousal'],
                                data['data'][j]['1']['emotion']['multimodal']['emotion'],
                                data['data'][j]['1']['emotion']['multimodal']['valence'],
                                data['data'][j]['1']['emotion']['multimodal']['arousal'],
                                data['data'][j]['1']['text']['strategy'],
                                data['data'][j]['1']['text']['script_end'],
                                data['data'][j]['1']['text']['script_start'],
                                data['data'][j]['1']['text']['script'],
                                data['data'][j]['1']['text']['intent']])
                            continue
                        if '2' in key:
                            fo.writerow([data['data'][j]['2']['person_id'],
                                data['data'][j]['2']['emotion']['text']['emotion'],
                                data['data'][j]['2']['emotion']['text']['valence'],
                                data['data'][j]['2']['emotion']['text']['arousal'],
                                data['data'][j]['2']['emotion']['sound']['emotion'],
                                data['data'][j]['2']['emotion']['sound']['valence'],
                                data['data'][j]['2']['emotion']['sound']['arousal'],
                                data['data'][j]['2']['emotion']['multimodal']['emotion'],
                                data['data'][j]['2']['emotion']['multimodal']['valence'],
                                data['data'][j]['2']['emotion']['multimodal']['arousal'],
                                data['data'][j]['2']['text']['strategy'],
                                data['data'][j]['2']['text']['script_end'],
                                data['data'][j]['2']['text']['script_start'],
                                data['data'][j]['2']['text']['script'],
                                data['data'][j]['2']['text']['intent']])
                            continue
                    if key=='3':
                        pass
            except:
                pass

    df_process=pd.read_csv('D:\\json_file_list\\clip_' + a + '_final_20220104.csv',encoding='cp949')
    df_process.drop_duplicates(subset=None,keep='first',inplace=True,ignore_index=True)
    #df_process.to_csv('clip_'+a+'csvfile_final.csv',encoding='cp949')
    df_process.to_csv('D:\\json_file_list\\clip_' + a + 'csvfile_20220104_0000.csv', encoding='cp949')
    t+=1

