import json

f=open('clip_1.json','rt', encoding='UTF8')
data=json.load(f)

#31번째에서 131번째의 프레임에 해당하는 발화를 가져오자.
for i in range(31,132):
    j=str(i)
    print(data['data'][j]['2'])
    print(data['data'][j]['2']['person_id'])
    print(data['data'][j]['2']['emotion'])
    print(data['data'][j]['2']['emotion']['image'])
    print(data['data'][j]['2']['emotion']['image']['emotion'])
    print(data['data'][j]['2']['emotion']['image']['emotion_sub'])
    print(data['data'][j]['2']['emotion']['image']['valence'])
    print(data['data'][j]['2']['emotion']['image']['arousal'])
    print(data['data'][j]['2']['predicate'])
    print(data['data'][j]['2']['predicate']['3'])
    print(data['data'][j]['2']['xtl'])
    print(data['data'][j]['2']['ybr'])
    print(data['data'][j]['2']['ytl'])
    print(data['data'][j]['2']['frame'])
    print(data['data'][j]['2']['xbr'])
    print(data['data'][j]['2']['label'])
    print(data['data'][j]['2']['position'])
    print(data['data'][j]['3'])  # 사물의 위치 관련 정보

    print(data['data'][j]['1']['person_id'])  # 1
    print(data['data'][j]['1']['emotion'])  # 1
    print(data['data'][j]['1']['emotion']['text'])  # 1
    print(data['data'][j]['1']['emotion']['text']['emotion'])  # 1
    print(data['data'][j]['1']['emotion']['text']['valence'])  # 1
    print(data['data'][j]['1']['emotion']['text']['arousal'])  # 1

    print(data['data'][j]['1']['emotion']['sound'])
    print(data['data'][j]['1']['emotion']['sound']['emotion'])  # 1
    print(data['data'][j]['1']['emotion']['sound']['valence'])  # 1
    print(data['data'][j]['1']['emotion']['sound']['arousal'])  # 1

    print(data['data'][j]['1']['emotion']['multimodal'])
    print(data['data'][j]['1']['emotion']['multimodal']['emotion'])  # 1
    print(data['data'][j]['1']['emotion']['multimodal']['valence'])  # 1
    print(data['data'][j]['1']['emotion']['multimodal']['arousal'])  # 1

    print(data['data'][j]['1']['emotion']['image'])
    print(data['data'][j]['1']['emotion']['image']['valence'])  # 1
    print(data['data'][j]['1']['emotion']['image']['arousal'])  # 1

    print(data['data'][j]['1']['text'])
    print(data['data'][j]['1']['text']['strategy'])
    print(data['data'][j]['1']['text']['script_end'])
    print(data['data'][j]['1']['text']['script_start'])
    print(data['data'][j]['1']['text']['script'])
    print(data['data'][j]['1']['text']['morpheme'])
    print(data['data'][j]['1']['text']['intent'])
    # text안에 strategy,script_end,script_start,script,morpheme,intent가 있음.
    print(data['data'][j]['1']['xtl'])
    print(data['data'][j]['1']['ybr'])
    print(data['data'][j]['1']['ytl'])
    print(data['data'][j]['1']['frame'])
    print(data['data'][j]['1']['xbr'])
    print(data['data'][j]['1']['label'])
    print(data['data'][j]['1']['position'])  # 위치 관계 정보
    print()
