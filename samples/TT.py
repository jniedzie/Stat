#FROM SVJ.MAKEPLOT.SAMPLES.SAMPLE IMPORT *
from samples.utils import *

TTJets_DiLept = sample()
TTJets_DiLept.files = outlist (d,"TTJets_DiLept")
TTJets_DiLept.sigma = 88.34
TTJets_DiLept.color = 798
TTJets_DiLept.style = 1
TTJets_DiLept.fill = 1001
TTJets_DiLept.leglabel = "t#bar{t}"
TTJets_DiLept.label = "TTJets_DiLept"


TTJets_DiLept_genMET150 = sample()
TTJets_DiLept_genMET150.files = outlist (d,"TTJets_DiLept_genMET150")
TTJets_DiLept_genMET150.sigma = 3.666
TTJets_DiLept_genMET150.color = 798
TTJets_DiLept_genMET150.style = 1
TTJets_DiLept_genMET150.fill = 1001
TTJets_DiLept_genMET150.leglabel = "t#bar{t}"
TTJets_DiLept_genMET150.label = "TTJets_DiLept_genMET150"

TTJets_SingleLeptFromT = sample()
TTJets_SingleLeptFromT.files = outlist (d,"TTJets_SingleLeptFromT")
TTJets_SingleLeptFromT.sigma = 182.72
TTJets_SingleLeptFromT.color = 798
TTJets_SingleLeptFromT.style = 1
TTJets_SingleLeptFromT.fill = 1001
TTJets_SingleLeptFromT.leglabel = "t#bar{t}"
TTJets_SingleLeptFromT.label = "TTJets_SingleLeptFromT"

TTJets_SingleLeptFromT_genMET150 = sample()
TTJets_SingleLeptFromT_genMET150.files = outlist (d,"TTJets_SingleLeptFromT_genMET150")
TTJets_SingleLeptFromT_genMET150.sigma = 5.979
TTJets_SingleLeptFromT_genMET150.color = 798
TTJets_SingleLeptFromT_genMET150.style = 1
TTJets_SingleLeptFromT_genMET150.fill = 1001
TTJets_SingleLeptFromT_genMET150.leglabel = "t#bar{t}"
TTJets_SingleLeptFromT_genMET150.label = "TTJets_SingleLeptFromT_genMET150"

TTJets_SingleLeptFromTbar = sample()
TTJets_SingleLeptFromTbar.files = outlist (d,"TTJets_SingleLeptFromTbar")
TTJets_SingleLeptFromTbar.sigma = 182.72
TTJets_SingleLeptFromTbar.color = 798
TTJets_SingleLeptFromTbar.style = 1
TTJets_SingleLeptFromTbar.fill = 1001
TTJets_SingleLeptFromTbar.leglabel = "t#bar{t}"
TTJets_SingleLeptFromTbar.label = "TTJets_SingleLeptFromTbar"

TTJets_SingleLeptFromTbar_genMET150 = sample()
TTJets_SingleLeptFromTbar_genMET150.files = outlist (d,"TTJets_SingleLeptFromTbar_genMET150")
TTJets_SingleLeptFromTbar_genMET150.sigma = 5.936
TTJets_SingleLeptFromTbar_genMET150.color = 798
TTJets_SingleLeptFromTbar_genMET150.style = 1
TTJets_SingleLeptFromTbar_genMET150.fill = 1001
TTJets_SingleLeptFromTbar_genMET150.leglabel = "t#bar_genMET150{t}"
TTJets_SingleLeptFromTbar_genMET150.label = "TTJets_SingleLeptFromTbar_genMET150"

TTJets_HT600to800 = sample()
TTJets_HT600to800.files = outlist (d,"TTJets_HT600to800")
TTJets_HT600to800.sigma = 2.7343862
TTJets_HT600to800.color = 798
TTJets_HT600to800.style = 1
TTJets_HT600to800.fill = 1001
TTJets_HT600to800.leglabel = "t#bar{t}"
TTJets_HT600to800.label = "TTJets_HT600to800"

TTJets_HT800to1200 = sample()
TTJets_HT800to1200.files = outlist (d,"TTJets_HT800to1200")
TTJets_HT800to1200.sigma = 1.12075054
TTJets_HT800to1200.color = 798
TTJets_HT800to1200.style = 1
TTJets_HT800to1200.fill = 1001
TTJets_HT800to1200.leglabel = "t#bar{t}"
TTJets_HT800to1200.label = "TTJets_HT800to1200"

TTJets_HT1200to2500 = sample()
TTJets_HT1200to2500.files = outlist (d,"TTJets_HT1200to2500")
TTJets_HT1200to2500.sigma = 0.1979159
TTJets_HT1200to2500.color = 798
TTJets_HT1200to2500.style = 1
TTJets_HT1200to2500.fill = 1001
TTJets_HT1200to2500.leglabel = "t#bar{t}"
TTJets_HT1200to2500.label = "TTJets_HT1200to2500"

TTJets_HT2500toInf = sample()
TTJets_HT2500toInf.files = outlist (d,"TTJets_HT2500toInf")
TTJets_HT2500toInf.sigma = 0.002368366
TTJets_HT2500toInf.color = 798
TTJets_HT2500toInf.style = 1
TTJets_HT2500toInf.fill = 1001
TTJets_HT2500toInf.leglabel = "t#bar{t}"
TTJets_HT2500toInf.label = "TTJets_HT2500toInf"

TTJets = sample()
TTJets.files = outlist (d,"TTJets")
TTJets.sigma = 831.76
TTJets.color = 798
TTJets.style = 1
TTJets.fill = 1001
TTJets.leglabel = "t#bar{t}"
TTJets.label = "TTJets"


TT = sample()
TT.color = 798
TT.style = 1
TT.fill = 1001
TT.leglabel = "t#bar{t}"
TT.label = "TT"
#TT.components = [TTJets, TTJets_HT600to800, TTJets_HT800to1200, TTJets_HT1200to2500, TTJets_HT2500toInf, TTJets_SingleLeptFromTbar_genMET150, TTJets_SingleLeptFromTbar, TTJets_SingleLeptFromT_genMET150, TTJets_SingleLeptFromT, TTJets_DiLept_genMET150, TTJets_DiLept]
TT.components = [TTJets, TTJets_HT600to800, TTJets_HT800to1200, TTJets_HT1200to2500, TTJets_HT2500toInf,  TTJets_SingleLeptFromTbar,  TTJets_SingleLeptFromT, TTJets_DiLept]


