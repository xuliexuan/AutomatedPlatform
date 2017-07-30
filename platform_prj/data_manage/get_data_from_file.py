# -*- coding: utf-8 -*-
import os
message = ''
file = r'F:\Python_prj\data_file\topSongInfo.md'
f=open(file,'rb')
while True:
	line = f.readline().decode('utf-8')
	if line:
		message+=line
	else:
		break
f.close()
