#!/usr/bin/python
import os, shutil
src='/home/tue86025/Desktop/sourceFolder'
dst='/home/tue86025/Desktop/Destimation'

def cpfile(src,dst):
 for i in os.listdir(src):
   filepath=src+os.sep+i
   if os.path.isdir(filepath):
      cpfile(filepath,dst)
   else:
      print 'copy ',filepath,' to ',src
      shutil.copy(filepath,dst)

if __name__ == '__main__':
    cpfile(src,dst)
