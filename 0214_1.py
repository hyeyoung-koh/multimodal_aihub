import pandas as pd

df3000=pd.read_pickle('F:/pickle/df_pickle_3000.pkl')
#다시
print(len(df3000))

df4000=pd.read_pickle('F:/pickle/df_pickle_4000.pkl')
print(len(df4000))

df5000=pd.read_pickle('D:/json_file_list/df_pickle_5000.pkl') #(4001~5000) (56743행~70758(팔)행)
print(len(df5000))



