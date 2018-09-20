import os
import shutil

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

def verifyChart(files):
   # Verify chart has a values file
  valuesfilepath = ""
  for f in files:
    if "values.yaml" in f.path:
      valuesfilepath = f.path
      break
  return valuesfilepath