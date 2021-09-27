import os
import shutil 
import time

d = "repos"



for dirpath, dirnames, filenames in os.walk(d):
     for f in filenames:
          full_path =  os.path.join(dirpath, f)
          #print(full_path)
          if full_path.endswith(".py"):
               pass
             # print((f"Keeping {full_path}"))
          else:
              #print((f"Deleting {full_path}")) 

              if d in full_path:
                  os.chmod(full_path)
                  shutil.rmtree
              else:
                  print("something is wrong")
                  time.sleep(60)
                 