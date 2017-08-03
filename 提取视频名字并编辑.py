import os
import re

def ListFilesToTxt(dir,file,recursion):
    name_list=[]
    i=0
    os.system('ls')
    print()
    for root, subdirs, files in os.walk(dir):
        for name in files:
            # 先判断文件名中是否有空格，如果有的话，需要用正则替换成空字符
            print("开始判断文件名是否合法（不含空格）")
            real_name=name.replace(' ','')
            print("----NAME IS"+name+"    REALNAME IS"+real_name)
            os.system('mv \"'+name+'\" '+real_name)
            print('mv '+name+' '+real_name+"-----改名成功")
            name=real_name
            # Judge if the name of the file is a video's name
            p=re.compile(r".*.mp4")  # 以下为利用正则进行视频链接的提取
            m=p.search(name)
            if (m):   #  标示查找到是是否为视频文件
                print("--------------------查找到一个视频")
            else:
                print("--------------------查找失败，name="+name)
                continue
        # -------
            name_list.insert(i,name)
            #print("插入名字成功"+name)
            #print(name_list[i])
            # 处理视频
            # command=('ffmpeg -i '+name+' -vf \"crop=w=iw-70:h=ih:x=12:y=34,rotate=-5*PI/180,colorchannelmixer=.393:.769:.189:0:.349:.686:.168:0:.272:.534:.131\" ./new/'+name+'.mpeg')
            command=('ffmpeg -i '+name+' -vf \"crop=w=iw-70:h=ih:x=12:y=34,rotate=-5*PI/180,colorchannelmixer=.393:.769:.189:0:.349:.686:.168:0:.272:.534:.131\" ./new/'+name+'.mpg')
            print("command is :"+command)
            os.system(command) #　视频处理完成
            print("name is <"+name+'>')
            os.system('rm '+name)
            i=i+1
        if(not recursion):
            break
     #   print("name_____list")
    #print(name_list)

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
