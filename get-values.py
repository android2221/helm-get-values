import os
import shutil
import click
import subprocess
import tarfile

tempdir = os.environ['HELM_PLUGIN_DIR'] + "/charts"

print("hello from python!" + tempdir)

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



# Fetch helm chart to temp dir
@click.command()
@click.argument('chartname')
def chart(chartname):
  # Create temp dir and extract values.yaml
  createFolder(tempdir)
  subprocess.call(["helm", "fetch", "-d", tempdir, chartname])
  for file in os.listdir(tempdir):
    tar = tarfile.open(tempdir + "/" + file)
    tarfiles = tar.getmembers()
    for f in tarfiles:
      if "values.yaml" in f.path:
        tar.extract(f.path, path=tempdir + '/extract')
        break
      #click.echo("Could not locate values.yaml in downloaded chart, exiting!")
      #exit
    # appen values to current values.yaml
  
  deleteFolder(tempdir)

# Click stuff
if __name__ == '__main__':
  chart()


# TODO: Correct usage help text