import sys
import os
import subprocess
import string
import optparse

from moduleStat.limitsUtils import *
from moduleStat.settings import *

usage = 'usage: %prog [--cat N]'
parser = optparse.OptionParser(usage)
parser.add_option("-c","--channel",dest="ch",type="string",default="all",help="Indicate channels of interest. Default is all")
parser.add_option("-y","--years",dest="years",type="string",default="2016",help="Indicate years of interest. Default is 2016")
parser.add_option('-m', '--method', dest='method', type='string', default = 'hist', help='Run a single method (hist, template, all)')
parser.add_option('-d', '--dir', dest='dir', type='string', default = 'outdir', help='datacards direcotry')
parser.add_option('',"--getSingleCats",dest="getSingleCats",action='store_true', default=False)

(opt, args) = parser.parse_args()

os.system("mkdir -p data")

years = ["2016", "2017", "2018"]
if opt.years != "all": 
    y_clean = opt.years.replace(" ", "")
    years = y_clean.split(",")


categories = channels
methods = ["hist", "template"]
if opt.ch != "all":
    ch_clean = opt.ch.replace(" ", "")
    categories = ch_clean.split(",")


if opt.method != "all": 
    meth_clean = opt.method.replace(" ", "")
    methods = meth_clean.split(",")
    

for y in years: 
    categories = [c + "_" + y for c in categories]

 
for method in methods:
    post = "_" + method
    get_limits(opt.dir, post)
    
    if opt.getSingleCats:
        for cat in categories:
            post = "_" + cat + "_" + method
            get_limits(opt.dir, post)
