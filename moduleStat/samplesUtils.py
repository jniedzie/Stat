

cross_sections = {
    "QCD_Pt_80to120": 2762530,
    "QCD_Pt_120to170": 471100,
    "QCD_Pt_170to300": 117276,
    "QCD_Pt_300to470": 7823,
    "QCD_Pt_470to600": 648.2,
    "QCD_Pt_600to800": 186.9,
    "QCD_Pt_800to1000": 32.293,
    "QCD_Pt_1000to1400": 9.4183,
    "QCD_Pt_1400to1800": 0.84265,
    "QCD_Pt_1800to2400": 0.114943,
    "QCD_Pt_2400to3200": 0.00682981,
    "QCD_Pt_3200toInf": 0.000165445,
    
    "TTJets_DiLept": 88.34,
    "TTJets_DiLept_genMET150": 3.666,
    "TTJets_SingleLeptFromT": 182.72,
    "TTJets_SingleLeptFromTbar": 182.72,
    
    "TTJets_SingleLeptFromT_genMET150": 5.979,
    "TTJets_SingleLeptFromTbar_genMET150": 5.936,
    
    "TTJets_HT600to800": 2.7343862,
    "TTJets_HT800to1200": 1.12075054,
    "TTJets_HT1200to2500": 0.1979159,
    "TTJets_HT2500toInf": 0.002368366,
    "TTJets": 831.76,
    
    "WJetsToLNu_HT100to200": 1627.45,
    "WJetsToLNu_HT200to400": 435.24,
    "WJetsToLNu_HT400to600": 59.18,
    "WJetsToLNu_HT600to800": 14.58,
    "WJetsToLNu_HT800to1200": 6.66,
    "WJetsToLNu_HT1200to2500": 1.608,
    "WJetsToLNu_HT2500toInf": 0.03891,

    "ZJetsToNuNu_HT100to200":  344.8305,
    "ZJetsToNuNu_HT200to400": 95.5341,
    "ZJetsToNuNu_HT400to600": 13.1979,
    "ZJetsToNuNu_HT600to800": 3.14757,
    "ZJetsToNuNu_HT800to1200": 1.450908,
    "ZJetsToNuNu_HT1200to2500": 0.3546459,
    "ZJetsToNuNu_HT2500toInf": 0.00854235,
    
}

# cross sections by Z' mass
SVJ_cross_sections = {
    500: 71.73,
    600: 33.22,
    700: 18.17,
    800: 10.75,
    900: 7.04,
    1000: 4.612,
    1100: 3.021,
    1200: 2.039,
    1300: 1.459,
    1400: 1.057,
    1500: 0.77,
    1600: 0.5667,
    1700: 0.4327,
    1800: 0.3304,
    1900: 0.2479,
    2000: 0.1849,
    2100: 0.1384,
    2200: 0.1044,
    2300: 0.08124,
    2400: 0.06361,
    2500: 0.04977,
    2600: 0.03891,
    2700: 0.03042,
    2800: 0.02447,
    2900: 0.01969,
    3000: 0.0155,
    3100: 0.01209,
    3200: 0.009518,
    3300: 0.007494,
    3400: 0.006148,
    3500: 0.005036,
    3600: 0.004047,
    3700: 0.003252,
    3800: 0.002613,
    3900: 0.0021,
    4000: 0.001688,
    4100: 0.001356,
    4200: 0.00109,
    4300: 0.0008757,
    4400: 0.0007037,
    4500: 0.0005655,
}


def get_SVJ_cross_section(mZprime):
    return SVJ_cross_sections[mZprime]
























































































