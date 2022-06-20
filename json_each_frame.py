import json

f=open('clip_1.json','rt', encoding='UTF8')
data=json.load(f)
print(data['data']['128'])


print(data['data']['128']['2']) #여기서 2는 객체 id이다.
print(data['data']['128']['2']['person_id']) #2-인물ID
print(data['data']['128']['2']['emotion'])
print(data['data']['128']['2']['emotion']['image'])
print(data['data']['128']['2']['emotion']['image']['emotion'])
print(data['data']['128']['2']['emotion']['image']['emotion_sub'])
print(data['data']['128']['2']['emotion']['image']['valence'])
print(data['data']['128']['2']['emotion']['image']['arousal'])


print(data['data']['128']['2']['predicate'])
print(data['data']['128']['2']['predicate']['3'])
print(data['data']['128']['2']['xtl'])
print(data['data']['128']['2']['ybr'])
print(data['data']['128']['2']['ytl'])
print(data['data']['128']['2']['frame'])
print(data['data']['128']['2']['xbr'])
print(data['data']['128']['2']['label'])
print(data['data']['128']['2']['position'])

print(data['data']['128']['3']) #사물의 위치 관련 정보

print(data['data']['128']['1']['person_id']) #1
print(data['data']['128']['1']['emotion']) #1
print(data['data']['128']['1']['emotion']['text']) #1
print(data['data']['128']['1']['emotion']['text']['emotion']) #1
print(data['data']['128']['1']['emotion']['text']['valence']) #1
print(data['data']['128']['1']['emotion']['text']['arousal']) #1

print(data['data']['128']['1']['emotion']['sound'])
print(data['data']['128']['1']['emotion']['sound']['emotion']) #1
print(data['data']['128']['1']['emotion']['sound']['valence']) #1
print(data['data']['128']['1']['emotion']['sound']['arousal']) #1

print(data['data']['128']['1']['emotion']['multimodal'])
print(data['data']['128']['1']['emotion']['multimodal']['emotion']) #1
print(data['data']['128']['1']['emotion']['multimodal']['valence']) #1
print(data['data']['128']['1']['emotion']['multimodal']['arousal']) #1

print(data['data']['128']['1']['emotion']['image'])
print(data['data']['128']['1']['emotion']['image']['valence']) #1
print(data['data']['128']['1']['emotion']['image']['arousal']) #1

print(data['data']['128']['1']['text'])
print(data['data']['128']['1']['text']['strategy'])
print(data['data']['128']['1']['text']['script_end'])
print(data['data']['128']['1']['text']['script_start'])
print(data['data']['128']['1']['text']['script'])
print(data['data']['128']['1']['text']['morpheme'])
print(data['data']['128']['1']['text']['intent'])


#text안에 strategy,script_end,script_start,script,morpheme,intent가 있음.
print(data['data']['128']['1']['xtl'])
print(data['data']['128']['1']['ybr'])
print(data['data']['128']['1']['ytl'])
print(data['data']['128']['1']['frame'])
print(data['data']['128']['1']['xbr'])
print(data['data']['128']['1']['label'])
print(data['data']['128']['1']['position']) #위치 관계 정보