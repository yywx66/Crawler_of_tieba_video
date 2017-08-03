import os
import re

def ListFilesToTxt(dir,file,recursion):
    name_list=[]
    i=0
    os.system('ls')
    print()
    for root, subdirs, files in os.walk(dir):
        for name in files:
            # Judge if the name of the file is a video's name
            p=re.compile(r".*.mp4")  # 以下为利用正则进行视频链接的提取
            m=p.search(name)
            if (m):
                print()
            else:
                continue
        # -------
            #name_list.insert(i,name)
            #print(name_list[i])
            # 处理视频
            command=('ffmpeg -i '+name+' -vf \"crop=w=iw-70:h=ih:x=12:y=34,rotate=-5*PI/180,curves=r=\'0/0.11 .42/.51 1/0.95\':g=\'0/0 0.50/0.48 1/1\':b=\'0/0.22 .49/.44 1/0.8\'\" ./new/'+name+'.mpeg')
            print("command is :"+command)
            os.system(command) #　视频处理完成
            i=i+1
        if(not recursion):
            break
#    print(name_list)

def Test():
  dir="./"
  outfile="bi.txt"
  #wildcard = ".mp4 .flv .rmvb .3gp .mpeg"
  file = open(outfile,"w")
  if not file:
    print ("cannot open the file %s for writing" % outfile)
  ListFilesToTxt(dir,file, 0)
  file.close()
  print()
  print("ALL DOWN!!")

Test()
