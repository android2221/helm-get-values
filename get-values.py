import os
import shutil
import click
import subprocess


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
  subprocess.call(["helm", "fetch", "-d", tempdir, chartname]) 

# Create temp dir
createFolder(tempdir)

# Cleanup temp dir
# deleteFolder(tempdir)

# Click stuff
if __name__ == '__main__':
  chart()


# TODO: Correct usage help text