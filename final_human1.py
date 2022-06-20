import json

f=open('clip_1.json','rt', encoding='UTF8')
data=json.load(f)
#31번째에서 131번째의 프레임에 해당하는 발화를 가져오자.->사람1
for i in range(31,132):
    j=str(i)
    print(type(data['data'][j]))
    print(data['data'][j])
    print(list(data['data'][j].keys())[0]) #이게 사람1/사람2 구별하는 코드
    #print(data['data'][j][0])
    #1번은 뭐라고 화내는 사람이다.
    print(data['data'][j]['1']['person_id'])  # 1

    print(type(data['data'][j]['1']['person_id'])) #str이라고 출력됨.
    #print(data['data'][j]['1']['emotion'])  # 1
    #print(data['data'][j]['1']['emotion']['text'])  # 1
    print(data['data'][j]['1']['emotion']['text']['emotion'])  # 1
    print(data['data'][j]['1']['emotion']['text']['valence'])  # 1
    print(data['data'][j]['1']['emotion']['text']['arousal'])  # 1

    #print(data['data'][j]['1']['emotion']['sound'])
    print(data['data'][j]['1']['emotion']['sound']['emotion'])  # 1
    print(data['data'][j]['1']['emotion']['sound']['valence'])  # 1
    print(data['data'][j]['1']['emotion']['sound']['arousal'])  # 1

    #print(data['data'][j]['1']['emotion']['multimodal'])
    print(data['data'][j]['1']['emotion']['multimodal']['emotion'])  # 1
    print(data['data'][j]['1']['emotion']['multimodal']['valence'])  # 1
    print(data['data'][j]['1']['emotion']['multimodal']['arousal'])  # 1

    #print(data['data'][j]['1']['text'])
    print(data['data'][j]['1']['text']['strategy'])
    print(data['data'][j]['1']['text']['script_end'])
    print(data['data'][j]['1']['text']['script_start'])
    print(data['data'][j]['1']['text']['script'])
    #print(data['data'][j]['1']['text']['morpheme'])
    print(data['data'][j]['1']['text']['intent'])
    print()
