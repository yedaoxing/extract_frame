# coding=utf-8
# 无法支持中文命名的视频

import os
import re

import cv2


#直接设置视频来源路径与截图保存路径运行程序,如果是windows需要用正则合法化路径
#videos_src_path = "D:\download_videos"
#videos_src_path = re.sub(r'\\','\\\\',videos_src_path)
#frames_save_path = 'D:\download_videos\\videos_frames'
#frames_save_path = re.sub(r'\\','\\\\',frames_save_path)
#videos_type = 'mp4'


#通过命令行交互由用户自己输入参数运行程序
videos_src_path = input('Please input videos floder path:（请输入视频来源路径） ')
frames_save_path = input('Please input save path:（请输入截图保存路径） ')
videos_type = input('Please input videos type:（请输入视频后缀名） ')
interval = input('Please input frames interval: （请输入截取帧数间隔，一般为30）')

#读取以videos_type结尾的视频文件列表
videos = os.listdir(videos_src_path)
videos = filter(lambda x: x.endswith(videos_type),videos)

print('running please wait...(程序正在提取视频帧，请稍等...)')
#读取每个视频
for each_video in videos:
	print ('正在处理视频: ' + each_video)
	
	#获得每个视频名称并创建文件夹（用来保存截图）
	each_video_name, _ =each_video.split('.')
	os.mkdir(frames_save_path + '\\' + each_video_name)
	each_frames_save_full_path = os.path.join(frames_save_path, each_video_name) + '\\'
	
	#使用每个视频名称获取视频来源路径，打开视频并提取截图
	each_video_full_path = os.path.join(videos_src_path,each_video)
	
	cap = cv2.VideoCapture(each_video_full_path)
	frame_count = 1
	snap_count = 0
	success = True
	while(success):
		success,frame = cap.read()
		#使用print除错
		#print('--->正在读取第%d帧'%frame_count,success)
		
		#按帧数间隔读取帧保存
		if int(interval) == 1:
			cv2.imwrite(each_video_save_full_path + each_video_name + '_%d.jpg' %frame_count,frame)
			snap_count += 1
		elif frame_count % int(interval) == 1:
			cv2.imwrite(each_frames_save_full_path + each_video_name + '_%d.jpg' %frame_count,frame)
			snap_count += 1
		frame_count += 1

cap.release()
num = str(snap_count)
print('共提取视频帧数：' + num)

