#my_list(self,file_path)함수:폴더 안에 있는 파일들을 리스트로 정리해서 리스트를 반환
#check_json(self,file_name)함수:해당 파일이 json파일인지 아닌지를 확인하고 json이라면 json_list에 추가
#add_files(self,file_path)함수:모든 파일리스트를 file_dic에 저장
#create_ouput(self)함수:json파일을 다 뽑아낸 후에 데이터처리.output_dic에 저장
import os
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
        #만약 json파일까지 도달했다면,그 json파일은 json_list에 저장하고,아직 폴더가 남았다면,
        #다시 add_files()를 호출해서 file_dic사전에 추가정리.
        if(self.file_dic[file_name][0].endswith('.json')):
            self.json_list.extend(self.file_dic[file_name])
        else:
            for name in self.file_dic[file_name]:
                self.add_files(name)
    def add_files(self,file_path):
        #main함수-my_list로 폴더 안의 파일리스트를 받아서 file_dic에 저장
        #그리고 json파일까지 도달했는지 체크한다.
        self.file_dic[file_path]=self.my_list(file_path)
        self.check_json(file_path)
    def create_output(self):
        #이제 다 뽑아낸 json_list(시리얼넘버)들로 각각의 json파일 안의 'sampleId'의 value값을 뽑아
        #output_dic사전에 저장한다.
        for filename in self.json_list:
            with open(filename,'r',) as file:
                json_data=json.load(file)
            self.output_dic[filename]=json_data['sampleId']

if __name__=="__main__":
    folder_name=input('input folder address:')
    #파이썬 파일과 폴더가 동일할 때는 folder_name="./"+folder_name 코드를 쓴다.
    folder=FindID(folder_name)
    #output_dic(키:json파일경로,value:ID값)
    #사전에 있는 값을 csv에 옮겨적는다.
    #시리얼 넘버는 키값인 json파일 경로에서 뽑아냈다.
    with open('output.csv','w',newline='') as csvfile:
        writer=csv.writer(csvfile)

        writer.writerow(['Path','Sirial Number','ID'])
        for key,val in folder.output_dic.items():
            writer.writerow( [key,key.split('/')[-1][:-8],val])
            #시리얼넘버는 키값인 json파일경로에서 뽑아냈다.
            #key.split('/')[-1][:-8]