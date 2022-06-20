import glob
import json
import csv

class FindID:
    def __init__(self,path):
        self.path=path #폴더들 주소
        self.json_list=[] #폴더들에서 json파일만 뽑아서 저장
        self.file_dic={}#모든 폴더와 폴더경로 안의 파일들을 정리해놓은 사전.
        self.output_dic={} #마지막 출력을 위해 key->json파일이름,value->각각의 ID를 저장시킬 것임.
        self.add_files(path) #file_dic사전 만들기 시작
        self.create_output() #출력할 내용을 정리하는 output_dic에 값을 넣어주는 함수
    def my_list(selfself,file_path):
        #폴더 안의 파일들을 리스트로 정리해서 return해준다.
        #glob함수는 폴더 경로를 이용해 그 안에 있는 모든 파일을 출력해준다.
        file_list=glob.glob(file_path+'/*')
        return file_list

    def check_json(self,file_name):
        if(self.file_dic[file_name][0].endswith('.json')):
            self.json_list.extend(self.file_dic[file_name])
        else:
            for name in self.file_dic[file_name]:
                self.add_files(name)
    def add_files(selfself,file_path):
        self.file_dic[file_path]=self.my_list(file_path)
        self.check_json(file_path)

    def create_output(self):
        #이제 다 뽑아낸 json_list(시리얼넘버)들로 각각의 json파일 안의 'sampleId'의 value값을 뽑아
        #output_dic사전에 저장한다.
        script_start1=[]
        script_start2=[]
        i=0
        data_frame_count=int(data['nr_frame'])

        for filename in self.json_list:
            with open(filename,'r',) as file:
                json_data=json.load(file)
                script_start1=[]
                script_start2=[]
                i=0
                data_frame_count=int(data['nr_frame'])
                #list1=json_data['data'][j]['1']['text']['script_start']
                #list2=
                for i in range(len(list1)):
                    j=str(list1[i])
                    self.output_dic[personId]=json_data['data'][j]['1']['person_id']
                    self.output_dic[text_emotion]=json_data['data'][j]['1']['emotion']['text']['emotion']
                    self.output_dic[text_emotion_valence]=json_data['data'][j]['1']['emotion']['text']['valence']
                    self.output_dic[text_emotion_arousal]=json_data['data'][j]['1']['emotion']['text']['arousal']
                    self.output_dic[sound_emotion]=json_data['data'][j]['1']['emotion']['sound']['emotion']
                    self.output_dic[sound_valence]=json_data['data'][j]['1']['emotion']['sound']['valence']
                    self.output_dic[sound_arousal]=json_data['data'][j]['1']['emotion']['sound']['arousal']
                    self.output_dic[multimodal_emotion]=json_data['data'][j]['1']['emotion']['multimodal']['emotion']
                    self.output_dic[multimodal_valence]=json_data['data'][j]['1']['emotion']['multimodal']['valence']
                    self.output_dic[multiomdal_arousal]=json_data['data'][j]['1']['emotion']['multimodal']['arousal']
                    self.output_dic[text_strategy]=json_data['data'][j]['1']['text']['strategy']
                    self.output_dic[text_scipt_end]=json_data['data'][j]['1']['text']['script_end']
                    self.output_dic[text_script_start]=json_data['data'][j]['1']['text']['script_start']
                    self.output_dic[text_script]=json_data['data'][j]['1']['text']['script']
                    self.output_dic[text_intent]=json_data['data'][j]['1']['text']['intent']
                    i+=1

