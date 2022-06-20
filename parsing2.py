import json

with open('D:\0001-0400\0001-0400\clip_1\clip_1') as json_file:
    json_data=json.load(json_file)
    json_value=json_data['situation']
    print(json_value)