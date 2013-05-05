#!/usr/bin/python
#####find and rename all the files in a folder, then copy them to the destination folder######
import os, shutil,sys
#src='/home/tue86025/Desktop/sourceFolder'
#dst='/home/tue86025/Desktop/Destimation'
src=sys.argv[1]
dst=sys.argv[2]


def cpfile(src,dst):
 for i in os.listdir(src):
   newname=os.path.basename(src)+i
   newfilepath=src+os.sep+newname
   filepath=src+os.sep+i
   print 'old path is ',filepath
   print 'new path is ',newfilepath
   if os.path.isdir(filepath):
      cpfile(filepath,dst)
   else:
  #    print 'copy ',filepath,' to ',dst
      #print 'old name is ',i           
      print 'old path is ',filepath
      print 'new path is ',newfilepath
      os.rename(filepath,newfilepath)
      print 'copy ',newfilepath,' to ',dst
      shutil.copy(newfilepath,dst)

if __name__ == '__main__':
    cpfile(src,dst)
