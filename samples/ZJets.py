######################################
#
# Annapaola de Cosa, January 2015
#
######################################

from utils import *

ZJetsToNuNu_HT100to200 = sample()
ZJetsToNuNu_HT100to200.files = outlist (d,"ZJetsToNuNu_HT-100to200")
ZJetsToNuNu_HT100to200.skimEff = 1.23
ZJetsToNuNu_HT100to200.sigma =  344.8305
ZJetsToNuNu_HT100to200.jpref = jetLabel 
ZJetsToNuNu_HT100to200.jp = jetLabel
ZJetsToNuNu_HT100to200.color = ROOT.kYellow -7
ZJetsToNuNu_HT100to200.style = 1
ZJetsToNuNu_HT100to200.fill = 1001
ZJetsToNuNu_HT100to200.leglabel = "ZJetsHT"
ZJetsToNuNu_HT100to200.label = "ZJetsToNuNu_HT100to200"

ZJetsToNuNu_HT200to400 = sample()
ZJetsToNuNu_HT200to400.files = outlist (d,"ZJetsToNuNu_HT-200to400")
ZJetsToNuNu_HT200to400.skimEff = 1.23
ZJetsToNuNu_HT200to400.sigma = 95.5341
ZJetsToNuNu_HT200to400.jpref = jetLabel 
ZJetsToNuNu_HT200to400.jp = jetLabel
ZJetsToNuNu_HT200to400.color = ROOT.kYellow -7
ZJetsToNuNu_HT200to400.style = 1
ZJetsToNuNu_HT200to400.fill = 1001
ZJetsToNuNu_HT200to400.leglabel = "ZJetsHT"
ZJetsToNuNu_HT200to400.label = "ZJetsToNuNu_HT200to400"

ZJetsToNuNu_HT400to600 = sample()
ZJetsToNuNu_HT400to600.files = outlist (d,"ZJetsToNuNu_HT-400to600")
ZJetsToNuNu_HT400to600.skimEff = 1.23
ZJetsToNuNu_HT400to600.sigma = 13.1979
ZJetsToNuNu_HT400to600.jpref = jetLabel 
ZJetsToNuNu_HT400to600.jp = jetLabel
ZJetsToNuNu_HT400to600.color = ROOT.kYellow -7
ZJetsToNuNu_HT400to600.style = 1
ZJetsToNuNu_HT400to600.fill = 1001
ZJetsToNuNu_HT400to600.leglabel = "ZJetsHT"
ZJetsToNuNu_HT400to600.label = "ZJetsToNuNu_HT400to600"

ZJetsToNuNu_HT600to800 = sample()
ZJetsToNuNu_HT600to800.files = outlist (d,"ZJetsToNuNu_HT-600to800")
ZJetsToNuNu_HT600to800.skimEff = 1.23
ZJetsToNuNu_HT600to800.sigma = 3.14757
ZJetsToNuNu_HT600to800.jpref = jetLabel 
ZJetsToNuNu_HT600to800.jp = jetLabel
ZJetsToNuNu_HT600to800.color = ROOT.kYellow -7
ZJetsToNuNu_HT600to800.style = 1
ZJetsToNuNu_HT600to800.fill = 1001
ZJetsToNuNu_HT600to800.leglabel = "ZJetsHT"
ZJetsToNuNu_HT600to800.label = "ZJetsToNuNu_HT600to800"

ZJetsToNuNu_HT800to1200 = sample()
ZJetsToNuNu_HT800to1200.files = outlist (d,"ZJetsToNuNu_HT-800to1200")
ZJetsToNuNu_HT800to1200.skimEff = 1.23
ZJetsToNuNu_HT800to1200.sigma = 1.450908
ZJetsToNuNu_HT800to1200.jpref = jetLabel 
ZJetsToNuNu_HT800to1200.jp = jetLabel
ZJetsToNuNu_HT800to1200.color = ROOT.kYellow -7
ZJetsToNuNu_HT800to1200.style = 1
ZJetsToNuNu_HT800to1200.fill = 1001
ZJetsToNuNu_HT800to1200.leglabel = "ZJetsHT"
ZJetsToNuNu_HT800to1200.label = "ZJetsToNuNu_HT800to1200"

ZJetsToNuNu_HT1200to2500 = sample()
ZJetsToNuNu_HT1200to2500.files = outlist (d,"ZJetsToNuNu_HT-1200to2500")
ZJetsToNuNu_HT1200to2500.skimEff = 1.23
ZJetsToNuNu_HT1200to2500.sigma = 0.3546459
ZJetsToNuNu_HT1200to2500.jpref = jetLabel 
ZJetsToNuNu_HT1200to2500.jp = jetLabel
ZJetsToNuNu_HT1200to2500.color = ROOT.kYellow -7
ZJetsToNuNu_HT1200to2500.style = 1
ZJetsToNuNu_HT1200to2500.fill = 1001
ZJetsToNuNu_HT1200to2500.leglabel = "ZJetsHT"
ZJetsToNuNu_HT1200to2500.label = "ZJetsToNuNu_HT1200to2500"

ZJetsToNuNu_HT2500toInf = sample()
ZJetsToNuNu_HT2500toInf.files = outlist (d,"ZJetsToNuNu_HT-2500toInf")
ZJetsToNuNu_HT2500toInf.skimEff = 1.23
ZJetsToNuNu_HT2500toInf.sigma = 0.00854235
ZJetsToNuNu_HT2500toInf.jpref = jetLabel 
ZJetsToNuNu_HT2500toInf.jp = jetLabel
ZJetsToNuNu_HT2500toInf.color = ROOT.kYellow -7
ZJetsToNuNu_HT2500toInf.style = 1
ZJetsToNuNu_HT2500toInf.fill = 1001
ZJetsToNuNu_HT2500toInf.leglabel = "ZJetsHT"
ZJetsToNuNu_HT2500toInf.label = "ZJetsToNuNu_HT2500toInf"

ZJets = sample()
ZJets.color = 881
ZJets.style = 1
ZJets.fill = 1001
ZJets.leglabel = "Z + jets"
ZJets.label = "ZJets"
#ZJets.components = [ZJetsToNuNu_HT100to200, ZJetsToNuNu_HT200to400, ZJetsToNuNu_HT400to600, ZJetsToNuNu_HT600to800, ZJetsToNuNu_HT800to1200,  ZJetsToNuNu_HT1200to2500, ZJetsToNuNu_HT2500toInf]
ZJets.components = [ZJetsToNuNu_HT400to600, ZJetsToNuNu_HT600to800, ZJetsToNuNu_HT800to1200,  ZJetsToNuNu_HT1200to2500, ZJetsToNuNu_HT2500toInf]






