import json

f=open('clip_2.json','rt', encoding='UTF8')
data=json.load(f)

i=0
for i in range(1077):
    try:
        j=str(i)
        print(data['data'][j]['1']['text']['script']) #사람1
        #print(data['data'][j]['2']['text']['script']) #사람2
        print(i)
        i+=1
    except:
        pass
i=0
for i in range(1077):
    try:
        j=str(i)
        print(data['data'][j]['2']['text']['script']) #사람1
        #print(data['data'][j]['2']['text']['script']) #사람2
        print(i)
        i+=1

    except:
        pass
# print(data['nr_frame'])

# for i in range(1077):
#    print(data['data'][i])

#for i in range(1077):
#    print(data['data'][i])

#print(data['data']['1']['1'])
#print(data['data']['1']['2'])
#print(data['data']['2']['1'])
#print(data['data']['2']['2'])
#발화
#data_frame=data['data']
#while True:
#    try:
#        for i in data_frame:
#            print(data['data'][i]['1']['text']['script'])
#    except:
#        pass
#print(data['data']['128']['1']['text']['script'])
