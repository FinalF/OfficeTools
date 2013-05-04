#!/usr/bin/python
import os, shutil,sys
#src='/home/tue86025/Desktop/sourceFolder'
#dst='/home/tue86025/Desktop/Destimation'
src=sys.argv[1]
dst=sys.argv[2]


def cpfile(src,dst):
 for i in os.listdir(src):
   filepath=src+os.sep+i
   if os.path.isdir(filepath):
      cpfile(filepath,dst)
   else:
  #    print 'copy ',filepath,' to ',dst
      shutil.copy(filepath,dst)

if __name__ == '__main__':
    cpfile(src,dst)
