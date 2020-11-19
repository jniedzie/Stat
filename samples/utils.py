
import ROOT
import collections
import os, subprocess


d = "/scratch/decosa/v9/"

jetLabel = "jetsAK4_"


class sample(object):
    pass


def outlist(repodir,dirn):
    cmd = "ls " + repodir + dirn
    status,ls_la = subprocess.getstatusoutput( cmd )
    list = ls_la.split(os.linesep)
    files = [d + "/"+dirn+ "/"+ l for l in list]
    return files

