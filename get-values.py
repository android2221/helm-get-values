import os
import shutil
from subprocess import call

tempdir = "./charts"

print("hello from python!")

def deleteFolder(directory):
  try:
    if os.path.exists(directory):
      shutil.rmtree(directory)
  except:
    print ('Could not delete the temp directory' + directory)

def createFolder(directory):
  try:
    if not os.path.exists(directory):
      os.makedirs(directory)
  except OSError:
      print ('Error creating directory ' +  directory)

# Create temp dir
createFolder(tempdir)

# Cleanup temp dir
deleteFolder(tempdir)
