import os
import tarfile
import shutil
import subprocess

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

def setup(tempdir):
    if not os.path.isfile("values.yaml"):
      return False
    deleteFolder(tempdir)
    createFolder(tempdir)
    return True

def getchart(tempdir, extractpath, chartname):
  subprocess.call(["helm", "fetch", "-d", tempdir, chartname])
  downloadedpath = tempdir + os.listdir(tempdir)[0]
  downloadedtar = tarfile.open(downloadedpath)
  tarfiles = downloadedtar.getmembers()
  valuesfilepath = verifyChart(tarfiles)
  if valuesfilepath:
    downloadedtar.extract(valuesfilepath, path=extractpath)
    return True
  else:
    return False

def verifyChart(files):
   # Verify chart has a values file
  valuesfilepath = ""
  for f in files:
    if "values.yaml" in f.path:
      valuesfilepath = f.path
      break
  return valuesfilepath

def appendValues(extractpath):
  charttitle = os.listdir(extractpath)[0]
  with open(extractpath + "/" + charttitle + "/values.yaml") as extractedvalesfile:
    appenddata = charttitle + ":" + "\n" + "  " + extractedvalesfile.read().replace("\n", "\n  ")
  with open("values.yaml", "a") as currentvalues:
    currentvalues.write('\n' + appenddata)
  return True