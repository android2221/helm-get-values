#!/usr/bin/env python

import os
import click
from valuestools import valuestools

tempdir = os.environ['HELM_PLUGIN_DIR'] + "/charts/"
extractpath = tempdir + "extract/"

# Fetch helm chart to temp dir
@click.command()
@click.argument('chartname')
def chart(chartname):

  setupsuccess = valuestools.setup(tempdir)

  if not setupsuccess:
    click.echo("Please add a values.yaml file")
    exit()

  click.echo("Getting values from " + chartname)
  
  getchartsuccess = valuestools.getchart(tempdir, extractpath, chartname)

  if not getchartsuccess:
    click.echo("Could not locate values.yaml in downloaded chart, exiting!")
    valuestools.deleteFolder(tempdir)
    exit()

  # Open downloaded values and append with indent to values file in current directory
  updatesuccess = valuestools.appendValues(extractpath)

  if updatesuccess:
    click.echo("Values file updated with values from the " + chartname + " chart")

  # Clean up
  valuestools.deleteFolder(tempdir)

if __name__ == '__main__':
  chart()
