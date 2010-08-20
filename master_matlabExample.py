#!/usr/bin/env python
#
#  master_matlabExample.py
#  matlabExample
#
#  Created by nicain on 8/16/10.
#  Copyright (c) 2010 University of Washington. All rights reserved.
#

################################################################################
# Preamble:
################################################################################

# Import necessary functions:
import pbsTools as pt

################################################################################
# Settings:
################################################################################

# pbsTools Settings:
commandString = 'matlab -nosplash -nojvm -r \'slave_matlabExample $ID\''
fileList = ('slave_matlabExample.m', 'setprod.m')

dryRun = 0
runLocation = 'local'
runType = 'batch'

nodes = 3*3*3
ppn = 'default'
verbose = 1
niceLevel = 20

################################################################################
# Run the job:
################################################################################

pt.runPBS(commandString, 
			fileList = fileList,
			dryRun = dryRun,
			runLocation = runLocation,
			runType = runType,
			nodes = nodes,
			ppn = ppn,
			verbose = verbose,
			niceLevel = niceLevel)