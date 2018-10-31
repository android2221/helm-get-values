#!/usr/bin/env python

import os, argparse
from valuestools import valuestools

parser = argparse.ArgumentParser(description="Get a helm chart's default values when using helm dependencies. \n\n Usage: helm get-values <chartname>", formatter_class=argparse.RawTextHelpFormatter )
parser.add_argument('chartname', type=str, help='the name of the charts\' values to append to your values file')
args = vars(parser.parse_args())

tempdir = os.environ['HELM_PLUGIN_DIR'] + "/charts/"
extractpath = tempdir + "extract/"

# Fetch helm chart to temp dir
def chart(chartname):

  setupsuccess = valuestools.setup(tempdir)

  if not setupsuccess:
    print("Please add a values.yaml file")
    exit()

  print("Getting values from " + chartname)
  
  getchartsuccess = valuestools.getchart(tempdir, extractpath, chartname)

  if not getchartsuccess:
    print("Could not locate values.yaml in downloaded chart, exiting!")
    valuestools.deleteFolder(tempdir)
    exit()

  # Open downloaded values and append with indent to values file in current directory
  updatesuccess = valuestools.appendValues(extractpath)

  if updatesuccess:
    print("Values file updated with values from the " + chartname + " chart")

  # Clean up
  valuestools.deleteFolder(tempdir)

if __name__ == '__main__':
  chart(args['chartname'])
