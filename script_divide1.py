import json

f=open('clip_1.json','rt', encoding='UTF8')
data=json.load(f)
#141번째에서 194번째의 프레임에 해당하는 발화를 가져오자.->사람2
#사람1에 관해서는 emotion-image만 나와있다.
#->사람2
for i in range(966,1047):
    j=str(i)
    #2번은 혼나는 사람이다.
    print(data['data'][j]['2']['person_id'],end=' ')  # 1
    #print(data['data'][j]['2']['emotion'])  # 1
    #print(data['data'][j]['2']['emotion']['text'])  # 1
    print(data['data'][j]['2']['emotion']['text']['emotion'],end=' ')  # 1
    print(data['data'][j]['2']['emotion']['text']['valence'],end=' ')  # 1
    print(data['data'][j]['2']['emotion']['text']['arousal'],end=' ')  # 1

    #print(data['data'][j]['2']['emotion']['sound'])
    print(data['data'][j]['2']['emotion']['sound']['emotion'],end=' ')  # 1
    print(data['data'][j]['2']['emotion']['sound']['valence'],end=' ')  # 1
    print(data['data'][j]['2']['emotion']['sound']['arousal'],end=' ')  # 1

    #print(data['data'][j]['2']['emotion']['multimodal'])
    print(data['data'][j]['2']['emotion']['multimodal']['emotion'],end=' ')  # 1
    print(data['data'][j]['2']['emotion']['multimodal']['valence'],end=' ')  # 1
    print(data['data'][j]['2']['emotion']['multimodal']['arousal'],end=' ')  # 1

    #print(data['data'][j]['2']['text'])
    print(data['data'][j]['2']['text']['strategy'],end=' ')
    print(data['data'][j]['2']['text']['script_end'],end=' ')
    print(data['data'][j]['2']['text']['script_start'],end=' ')
    print(data['data'][j]['2']['text']['script'],end=' ')
    #print(data['data'][j]['2']['text']['morpheme'])
    print(data['data'][j]['2']['text']['intent'],end=' ')
    print()
