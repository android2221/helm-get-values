import os
import shutil
import click
import subprocess
import tarfile
from valuestools import valuestools

tempdir = os.environ['HELM_PLUGIN_DIR'] + "/charts"
extractpath = tempdir + '/extract'

# Fetch helm chart to temp dir
@click.command()
@click.argument('chartname')
def chart(chartname):
  # Create temp dir and extract values.yaml
  valuestools.deleteFolder(tempdir)
  valuestools.createFolder(tempdir)
  click.echo("Getting " + chartname)
  subprocess.call(["helm", "fetch", "-d", tempdir, chartname])
  for file in os.listdir(tempdir):
    tar = tarfile.open(tempdir + "/" + file)
    tarfiles = tar.getmembers()
    foundvalues = False
    for f in tarfiles:
      if "values.yaml" in f.path:
        foundvalues = True
        tar.extract(f.path, path=extractpath)
        break
    if not foundvalues:
      click.echo("Could not locate values.yaml in downloaded chart, exiting!")
      exit
    # append values to current values.yaml
    if not os.path.exists("values.yaml"):
      click.echo("Could not locate values.yaml in current directory, exiting!")
      exit
    currentvaluesfile = open("values.yaml", "a")
    charttitle = os.listdir(extractpath)[0]
    newvaluesfile = open(extractpath + "/" + charttitle + "/values.yaml")
    currentvaluesfile.write("\n" + charttitle + ":" + "\n" + "  " + newvaluesfile.read().replace("\n", "\n  "))
    click.echo("Values file updated with values from the " + charttitle + "chart")

  valuestools.deleteFolder(tempdir)


# Click stuff
if __name__ == '__main__':
  chart()


# TODO: Correct usage help text
