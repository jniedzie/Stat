from utils import *

ZJetsToNuNu_Zpt100to200 = sample()
ZJetsToNuNu_Zpt100to200.files = outlist (d,"ZJetsToNuNu_Zpt-100to200")
ZJetsToNuNu_Zpt100to200.jpref = jetLabel 
ZJetsToNuNu_Zpt100to200.jp = jetLabel 
ZJetsToNuNu_Zpt100to200.sf = 1. #43.5543
ZJetsToNuNu_Zpt100to200.skimEff = 1. #1.23
ZJetsToNuNu_Zpt100to200.sigma = 43.55
ZJetsToNuNu_Zpt100to200.color = ROOT.kYellow -9
ZJetsToNuNu_Zpt100to200.style = 1
ZJetsToNuNu_Zpt100to200.fill = 1001
ZJetsToNuNu_Zpt100to200.leglabel = "ZJetsHT"
ZJetsToNuNu_Zpt100to200.label = "ZJetsToNuNu_Zpt100to200"

ZJetsToNuNu_Zpt200toInf = sample()
ZJetsToNuNu_Zpt200toInf.files = outlist (d,"ZJetsToNuNu_Zpt-200toInf")
ZJetsToNuNu_Zpt200toInf.jpref = jetLabel 
ZJetsToNuNu_Zpt200toInf.jp = jetLabel 
ZJetsToNuNu_Zpt200toInf.sf = 1. #5.28654
ZJetsToNuNu_Zpt200toInf.skimEff = 1. #1.23
ZJetsToNuNu_Zpt200toInf.sigma = 5.287
ZJetsToNuNu_Zpt200toInf.color = ROOT.kYellow -9
ZJetsToNuNu_Zpt200toInf.style = 1
ZJetsToNuNu_Zpt200toInf.fill = 1001
ZJetsToNuNu_Zpt200toInf.leglabel = "ZJetsHT"
ZJetsToNuNu_Zpt200toInf.label = "ZJetsToNuNu_Zpt200toInf"

ZJets = sample()
ZJets.color = 881
ZJets.style = 1
ZJets.fill = 1001
ZJets.leglabel = "Z + jets"
ZJets.label = "ZJets"
ZJets.components = [ZJetsToNuNu_Zpt100to200, ZJetsToNuNu_Zpt200toInf]
#ZJets.components = [ZJetsToNuNu_Zpt200toInf]

