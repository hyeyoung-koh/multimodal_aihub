import csv
import json
import pandas as pd

for t in range(50,51):
    k=str(t)
    with open('D:\\json_file_list\\clip_' + k + '.json', 'r', encoding='utf-8-sig') as input_file, open('D:\\json_file_list\\clip_' + k + '_final_20220105bbbb.csv', 'w', newline='', encoding='cp949') as output_file:
        fo=csv.writer(output_file)
        fo.writerow(['episode_no','age','gender','person_id','text_emotion','text_valence','text_arousal','sound_emotion','sound_valence','sound_arousal',
                     'multimodal_emotion','multimodal_valence','multimodal_arousal','text_strategy','text_script_end','text_script_start','text_script','text_intent'])
        data=json.load(input_file)
        frame_num = int(data['nr_frame'])
        dkeys=[]
        akeys=[]
        for key,value in data['data'].items():
            dkeys.append(key)
            for m in dkeys:
                a=str(m)
                print(a)
        for key2,value2 in data['actor'].items():
            akeys.append(key2)
            for x in akeys:
                if x==data['data'][a]['2']['person_id'] or x==data['data'][a]['1']['person_id']:
                    print(x)
                    person_id=x
                # if x==data['data'][a]['1']['person_id']:
                #     person_id2=x
                    # fo.writerow(data['actor'][person_id2]['age'])
                    # fo.writerow(data['actor'][person_id2]['gender'])
                try:
                    fo.writerow([data['clip_id'], #episode_no
                      data['data'][a]['2']['person_id'],
                      data['data'][a]['2']['emotion']['text']['emotion'],
                      data['data'][a]['2']['emotion']['text']['valence'],
                      data['data'][a]['2']['emotion']['text']['arousal'],
                      data['data'][a]['2']['emotion']['sound']['emotion'],
                      data['data'][a]['2']['emotion']['sound']['valence'],
                      data['data'][a]['2']['emotion']['sound']['arousal'],
                      data['data'][a]['2']['emotion']['multimodal']['emotion'],
                      data['data'][a]['2']['emotion']['multimodal']['valence'],
                      data['data'][a]['2']['emotion']['multimodal']['arousal'],
                      data['data'][a]['2']['text']['strategy'],
                      data['data'][a]['2']['text']['script_end'],
                      data['data'][a]['2']['text']['script_start'],
                      data['data'][a]['2']['text']['script'],
                      data['data'][a]['2']['text']['intent']])
                except:
                    pass
                try:
                    fo.writerow([data['clip_id'],
                      data['data']['actor'][person_id]['age'],
                      data['data']['actor'][person_id]['gender'],
                      data['data'][a]['1']['person_id'],
                      data['data'][a]['1']['emotion']['text']['emotion'],
                      data['data'][a]['1']['emotion']['text']['valence'],
                      data['data'][a]['1']['emotion']['text']['arousal'],
                      data['data'][a]['1']['emotion']['sound']['emotion'],
                      data['data'][a]['1']['emotion']['sound']['valence'],
                      data['data'][a]['1']['emotion']['sound']['arousal'],
                      data['data'][a]['1']['emotion']['multimodal']['emotion'],
                      data['data'][a]['1']['emotion']['multimodal']['valence'],
                      data['data'][a]['1']['emotion']['multimodal']['arousal'],
                      data['data'][a]['1']['text']['strategy'],
                      data['data'][a]['1']['text']['script_end'],
                      data['data'][a]['1']['text']['script_start'],
                      data['data'][a]['1']['text']['script'],
                      data['data'][a]['1']['text']['intent']])
                except:
                    pass


df_process=pd.read_csv('D:\\json_file_list\\clip_' + k + '_final_20220105bbbb.csv',encoding='cp949')
df_process.drop_duplicates(subset=None,keep='first',inplace=True,ignore_index=True)
#df_process.to_csv('clip_'+k+'csvfile_final.csv',encoding='cp949')
df_process.to_csv('D:\\json_file_list\\clip_' + k + 'csvfile_20220105_1719.csv', encoding='cp949')


