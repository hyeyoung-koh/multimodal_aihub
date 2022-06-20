import json
import csv

with open('clip_1.json','r',encoding='utf-8') as input_file,open('clip_1_final.csv','w',newline='') as output_file:
    data=json.load(input_file)
    f=csv.writer(output_file)

    #csv파일에 header를 추가한다.
    f.writerow(['person_id','text_emotion','text_valence','text_arousal','sound_emotion','sound_valence','sound_arousal',
                'multimodal_emotion','multimodal_valence','multimodal_arousal','text_strategy','text_script_end','text_script_start','text_script',
                'text_intent'])
    #for datum in data:
    #사람1
    n=[31,211,423,656,851] #사람1의 script_start
    i=0
    for i in range(len(n)):
        j=str(n[i])
        f.writerow([data['data'][j]['1']['person_id'],
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
        i+=1
    #사람2
    n2=[141,331,531,741,966] #사람2의 script_start
    k=0
    for k in range(len(n2)):
        m=str(n2[k])
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
        k+=1
