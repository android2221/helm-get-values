import os
import click
import subprocess
import tarfile
from valuestools import valuestools

tempdir = os.environ['HELM_PLUGIN_DIR'] + "/charts/"
extractpath = tempdir + "extract/"

# Fetch helm chart to temp dir
@click.command()
@click.argument('chartname')
def chart(chartname):
  charthasvaluesfile = False
  # Create temp dir 
  valuestools.deleteFolder(tempdir)
  valuestools.createFolder(tempdir)

  # Get chart
  click.echo("Getting values from " + chartname)
  subprocess.call(["helm", "fetch", "-d", tempdir, chartname])
  downloadedpath = tempdir + os.listdir(tempdir)[0]
  downloadedtar = tarfile.open(downloadedpath)
  tarfiles = downloadedtar.getmembers()

  # Verify chart has a values file
  valuesfilepath = ""
  for f in tarfiles:
    if "values.yaml" in f.path:
      charthasvaluesfile = True
      valuesfilepath = f.path
      break

  # Extract if values.yaml exists
  if charthasvaluesfile:
    downloadedtar.extract(valuesfilepath, path=extractpath)
  else:
    click.echo("Could not locate values.yaml in downloaded chart, exiting!")
    exit

  # Open downloaded values and append with indent to values file in current directory
  currentvaluesfile = open("values.yaml", "a")
  charttitle = os.listdir(extractpath)[0]
  newvaluesfile = open(extractpath + "/" + charttitle + "/values.yaml")
  currentvaluesfile.write("\n" + charttitle + ":" + "\n" + "  " + newvaluesfile.read().replace("\n", "\n  "))
  click.echo("Values file updated with values from the " + chartname + " chart")

  # Clean up
  valuestools.deleteFolder(tempdir)

if __name__ == '__main__':
  chart()


# TODO: Correct usage help text
