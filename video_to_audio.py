#pip install moviepy

#import moviepy.editor as mp

#clip=np.VideoFileClip('file to extract audio.')
import subprocess
item= #mp4파일
this_path= #현재 경로
save_file_id= #저장할 wav파일
command = "ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn {}".format(item, os.path.join(this_path, save_file_id))

subprocess.call(command, shell=True)