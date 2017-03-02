#!/usr/bin/env python

from PandaCore.Tools.condor import htcondor,classad

logsdir = '/home/snarayan/condortest/logs/'
dict_classad = {
    "Cmd" : "/bin/sleep",
#    "Arguments" : "10",
    "UserLog" : '{0}/test.log'.format(logsdir),
#    "Out" : 'strcat("{0}/",strcat(ProcId,".out"))'.format(logsdir),
#    "Err" : 'strcat("{0}/",strcat(ProcId,".err"))'.format(logsdir),
    "WhenToTransferOutput" : "ON_EXIT",
    "ShouldTransferFiles" : "YES",
#    "Requirements" : '( UidDomain == "mit.edu" && Arch == "X86_64" && OpSysAndVer == "SL6" ) && ( ( Arch == "INTEL" || Arch == "X86_64" ) ) && ( TARGET.Disk >= RequestDisk ) && ( TARGET.Memory >= RequestMemory ) && ( TARGET.HasFileTransfer )',
    "AcctGroup" : "group_t3mit.urgent",
    "In" :"/dev/null",
    "X509UserProxy" : "/tmp/x509up_u67051",
}


#with open('templ.jdl') as ftempl:
#    str_classad = ftempl.read()
#print str_classad

ad = classad.ClassAd()
for k,v in dict_classad.iteritems():
    ad[k] = v

coll = htcondor.Collector()
schedd = htcondor.Schedd(coll.locate(htcondor.DaemonTypes.Schedd,"t3home000.mit.edu"))

to_submit = []
for i in xrange(10):
    proc_ad = classad.ClassAd()
    dict_procad = {
        "Arguments" : str(i*10),
        "Out" : '{0}/{1}.out'.format(logsdir,i),
        "Err" : '{0}/{1}.err'.format(logsdir,i),
    }
    for k,v in dict_procad.iteritems():
        proc_ad[k] = v
    #print proc_ad
    to_submit.append((proc_ad,1))

print schedd.submitMany(ad,to_submit)

