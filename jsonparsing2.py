import json

f=open('clip_1.json','rt',encoding='UTF8')
data=json.load(f)
#print(data)
for i in data['data']:
    print(i)
#print(data['situation'])
#print(data['video_size'])
#print(data['clip_id'])
#print(data['category'])
#print(data['data'])
#print(data['actor'])
#print(data['nr_frame'])
for i in