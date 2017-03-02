#!/usr/bin/env python

from PandaCore.Tools.condor import htcondor,classad
from sys import argv

status = {
        1:'idle',
        2:'running',
        3:'removed',
        4:'completed',
        5:'held',
        6:'transferring output',
        7:'suspended',
        }

coll = htcondor.Collector()
schedd = htcondor.Schedd(coll.locate(htcondor.DaemonTypes.Schedd,"t3home000.mit.edu"))

jobs = schedd.query('Owner =?= "snarayan" && ClusterId =?= %i'%int(argv[1]))
for j in jobs:
    print '---JOB %i.%i SUMMARY---'%(j['ClusterId'],j['ProcId'])
    print '\tThis job is %s'%(status[j['JobStatus']])
    print '\tArguments are %s'%(j['Arguments'])
