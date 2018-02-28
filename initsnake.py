from init.txt import *
if isfirstrun!=1:
      init_txt=open("init.txt","w")
      init_txt.write("isfirstrun=1")
      init_txt.close
      path=input("whats the path?\n")
      bpath=input("Whats the path to the backup?\n")
      limit=input("Whats the limit?")
      init_txt=open("init.txt","a")
      init_txt.write(path, "\n", bpath, "\n", limit)
      init_txt.close
import overlordsnake
