import json
#여기서는 clip_1.json파일을 이용함.
f=open('clip_2.json','rt', encoding='UTF8')
data=json.load(f)
#print(data['nr_frame']) #이게 전체 frame수를 구하는 것임.
#print(type(data['nr_frame'])) #str
script_start1 = []
script_start2 = []
#i=0
#print(data['nr_frame'])
#print(type(data['nr_frame'])) #str
data_frame_count=int(data['nr_frame'])
#print(data_frame_count)
#print(data['data']['128']['1']['person_id']) #->1이라 출력됨.
i=0
#print(data_frame_count)
for i in range(1,data_frame_count+1):
    j=str(i)
    try:
        if list(data['data'][j].keys())[0]=='1': #사람1
            script_start1.append(data['data'][j]['1']['text']['script_start'])
            i+=1
        elif list(data['data'][j].keys())[0]=='2': #사람2
            script_start2.append(data['data'][j]['2']['text']['script_start'])
            i+=1
        else:
            i+=1
    except:
        pass
#print(script_start1)
#print(script_start2)
print(set(script_start1))
print(set(script_start2))