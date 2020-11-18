######################################
#
# Deborah Pinna, August 2015
#
######################################


from utils import *

Run2016B = sample()
Run2016B.files = outlist (d,"Run2016B")
Run2016B.skimEff = 1
Run2016B.sigma = 1
Run2016B.color = ROOT.kBlack
Run2016B.jpref = jetLabel 
Run2016B.jp = jetLabel
Run2016B.style = 1
Run2016B.fill = 1001
Run2016B.leglabel = "Run2016B"
Run2016B.label = "Run2016B"

Run2016C = sample()
Run2016C.files = outlist (d,"Run2016C")
Run2016C.skimEff = 1
Run2016C.sigma = 1
Run2016C.color = ROOT.kBlack
Run2016C.jpref = jetLabel
Run2016C.jp = jetLabel
Run2016C.style = 1
Run2016C.fill = 1001
Run2016C.leglabel = "Run2016C"
Run2016C.label = "Run2016C"

Run2016D = sample()
Run2016D.files = outlist (d,"Run2016D")
Run2016D.skimEff = 1
Run2016D.sigma = 1
Run2016D.color = ROOT.kBlack
Run2016D.jpref = jetLabel
Run2016D.jp = jetLabel
Run2016D.style = 1
Run2016D.fill = 1001
Run2016D.leglabel = "Run2016D"
Run2016D.label = "Run2016D"

Run2016E = sample()
Run2016E.files = outlist (d,"Run2016E")
Run2016E.skimEff = 1
Run2016E.sigma = 1
Run2016E.color = ROOT.kBlack
Run2016E.jpref = jetLabel
Run2016E.jp = jetLabel
Run2016E.style = 1
Run2016E.fill = 1001
Run2016E.leglabel = "Run2016E"
Run2016E.label = "Run2016E"

Run2016F = sample()
Run2016F.files = outlist (d,"Run2016F")
Run2016F.skimEff = 1
Run2016F.sigma = 1
Run2016F.color = ROOT.kBlack
Run2016F.jpref = jetLabel
Run2016F.jp = jetLabel
Run2016F.style = 1
Run2016F.fill = 1001
Run2016F.leglabel = "Run2016F"
Run2016F.label = "Run2016F"

Run2016G = sample()
Run2016G.files = outlist (d,"Run2016G")
Run2016G.skimEff = 1
Run2016G.sigma = 1
Run2016G.color = ROOT.kBlack
Run2016G.jpref = jetLabel
Run2016G.jp = jetLabel
Run2016G.style = 1
Run2016G.fill = 1001
Run2016G.leglabel = "Run2016G"
Run2016G.label = "Run2016G"

Run2016H = sample()
Run2016H.files = outlist (d,"Run2016H")
Run2016H.skimEff = 1
Run2016H.sigma = 1
Run2016H.color = ROOT.kBlack
Run2016H.jpref = jetLabel
Run2016H.jp = jetLabel
Run2016H.style = 1
Run2016H.fill = 1001
Run2016H.leglabel = "Run2016H"
Run2016H.label = "Run2016H"


Run2017B = sample()
Run2017B.files = outlist (d,"Run2017B")
Run2017B.skimEff = 1
Run2017B.sigma = 1
Run2017B.color = ROOT.kBlack
Run2017B.jpref = jetLabel
Run2017B.jp = jetLabel
Run2017B.style = 1
Run2017B.fill = 1001
Run2017B.leglabel = "Run2017B"
Run2017B.label = "Run2017B"


Run2017C = sample()
Run2017C.files = outlist (d,"Run2017C")
Run2017C.skimEff = 1
Run2017C.sigma = 1
Run2017C.color = ROOT.kBlack
Run2017C.jpref = jetLabel
Run2017C.jp = jetLabel
Run2017C.style = 1
Run2017C.fill = 1001
Run2017C.leglabel = "Run2017C"
Run2017C.label = "Run2017C"

Run2017D = sample()
Run2017D.files = outlist (d,"Run2017D")
Run2017D.skimEff = 1
Run2017D.sigma = 1
Run2017D.color = ROOT.kBlack
Run2017D.jpref = jetLabel
Run2017D.jp = jetLabel
Run2017D.style = 1
Run2017D.fill = 1001
Run2017D.leglabel = "Run2017D"
Run2017D.label = "Run2017D"

Run2017E = sample()
Run2017E.files = outlist (d,"Run2017E")
Run2017E.skimEff = 1
Run2017E.sigma = 1
Run2017E.color = ROOT.kBlack
Run2017E.jpref = jetLabel
Run2017E.jp = jetLabel
Run2017E.style = 1
Run2017E.fill = 1001
Run2017E.leglabel = "Run2017E"
Run2017E.label = "Run2017E"

Run2017F = sample()
Run2017F.files = outlist (d,"Run2017F")
Run2017F.skimEff = 1
Run2017F.sigma = 1
Run2017F.color = ROOT.kBlack
Run2017F.jpref = jetLabel
Run2017F.jp = jetLabel
Run2017F.style = 1
Run2017F.fill = 1001
Run2017F.leglabel = "Run2017F"
Run2017F.label = "Run2017F"


Data = sample()
Data.color = ROOT.kBlack
Data.style = 1
Data.fill = 1001
Data.leglabel = "Data"
Data.label = "Data"

#Data.components = [Run2016B, Run2016C, Run2016D, Run2016E, Run2016F, Run2016G, Run2016H]
Data.components = [Run2017B, Run2017C, Run2017D, Run2017E, Run2017F]
#Data.components = [Run2016B, Run2016C, Run2016D, Run2016E, Run2016F, Run2016H, Run2017B, Run2017C, Run2017D, Run2017E, Run2017F]


