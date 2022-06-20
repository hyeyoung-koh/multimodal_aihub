#json파일 읽어서 data에 저장
#csv파일에 컬럼 헤더 저장
import json
import csv

#music.json파일을 읽어서 melon.csv파일에 저장하자.
with open('music.json','r',encoding='utf-8') as input_file,open('melon.csv','w',newline='') as output_file:
    data=json.load(input_file)
    #data[0]은 json파일의 한 줄을 보관한다.
    #data[0]['컬럼명']은 첫번째 줄의 해당 컬럼 element를 보관한다.
    f=csv.witer(output_file)

    #csv파일에 header를 추가한다.
    f.writerow(['title','songId','artist','img'])
    #노래 제목에 아래 문구가 포함되어있을 경우 csv저장하지 않는다.
    matches=['inst.','Inst.']

    #write each row of a json file
    for datum in data:
        #exclude instrument versions
        if any(x in datum['title'] for x in matches):
            continue
        f.writerow([datum['title'],datum['songId'],datum['artist'],datum['img']])