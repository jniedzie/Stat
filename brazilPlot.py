from moduleStat.settings import *
from moduleStat.limitsUtils import Limit
from moduleStat.samplesUtils import get_SVJ_cross_section

import ROOT
import optparse

from array import array


def set_root_options():
    ROOT.gROOT.Reset()
    ROOT.gROOT.SetStyle('Plain')
    ROOT.gStyle.SetPalette(1)
    ROOT.gStyle.SetOptStat(0)
    ROOT.gROOT.SetBatch()        # don't pop up canvases
    ROOT.TH1.AddDirectory(False)


def read_file(file_name, cat):

    read_limits = []
    
    print("Reading ", file_name)
    input_file = open(file_name)

    first_line = True

    for line in input_file.readlines():

        if line.strip() == "":
            continue
        
        l_split = line.split()
        
        if first_line:
            read_limits = [Limit() for i in range(len(l_split)-1)]
            first_line = False
            
        for label, arg_name in Limit.label_to_attr_name.items():
            if line.startswith(label + "_" + cat):
                for i in range(0, len(l_split)-1):
                    setattr(read_limits[i], arg_name, float(l_split[i+1]))

    return read_limits

usage = 'usage: %prog --method method'
parser = optparse.OptionParser(usage)
parser.add_option("-r","--ratio",dest="ratio",action='store_true', default=False)
parser.add_option('-m', '--method', dest='method', type='string', default = 'hist', help='Run a single method (all, hist, template)')
parser.add_option('-y', '--year', dest='year', type='string', default = 'all', help='Run a single method (Run2, 2016, 2017, 2016_2017)')
parser.add_option('-v', '--variable', dest='variable', type='string', default = 'mZprime', help='Plot limit against variable v (mZPrime, mDark, rinv, alpha)')
parser.add_option("-u","--unblind",dest="unblind",action='store_true', default=False)
parser.add_option("-c","--cat",dest="cat",type="string",default="",help="Indicate channels of interest. Default is all")
parser.add_option("","--rInv",dest="r_inv",type="string",default="",help="For which r_inv should limits be drawn")
(opt, args) = parser.parse_args()

unblind = opt.unblind
theo = not opt.ratio

r_inv = ""

if opt.r_inv != "":
    r_inv = "_rinv{}".format(opt.r_inv)
    

if opt.cat!="":
    filename = "data/limit%s_%s_%s.txt" % (r_inv, opt.cat, opt.method)
    cat ="%s_%s"% (opt.cat, opt.method)
else:
    filename = "data/limit%s_%s.txt" % (r_inv, opt.method)
    cat = opt.method    


limits = read_file(filename, cat)

print("Loaded limits:")
for limit in limits:
    limit.print()

n_limits = len(limits)

ebar_u1 = [limits[i].points_up_1_sigma - limits[i].value for i in range(n_limits)]
ebar_u2 = [limits[i].points_up_2_sigma - limits[i].value for i in range(n_limits)]
ebar_d1 = [limits[i].value - limits[i].points_down_1_sigma for i in range(n_limits)]
ebar_d2 = [limits[i].value - limits[i].points_down_2_sigma for i in range(n_limits)]


expected_values = array('f', [l.value for l in limits])
observed_values = array('f', [l.observed for l in limits])

x_values = array('f', [l.mass for l in limits])

if opt.variable == "mDark":
    pass
elif opt.variable == "rinv":
    pass
elif opt.variable == "alpha":
    pass


print("XVALUES: ", x_values)
print("MEDVALUES: ", expected_values)

y_theo = {str(mass): get_SVJ_cross_section(mass) for mass in x_values }


y_th_xsec = collections.OrderedDict(sorted(y_theo.items()))
y_xsec_vals = array('f', [limits[i].value * list(y_th_xsec.values())[i] for i in range(n_limits)])
y_xsec_obs_vals = array('f', [limits[i].observed * list(y_th_xsec.values())[i] for i in range(n_limits)])
y_th_xsec_vals = array('f', [th for th in y_th_xsec.values()])

y_bars_d1 =  array('f', ebar_d1)
y_bars_d2 =  array('f', ebar_d2)
y_bars_u1 =  array('f', ebar_u1)
y_bars_u2 =  array('f', ebar_u2)

if theo:
    y_bars_d1 =  array('f', [ebar_d1[i] * list(y_th_xsec.values())[i] for i in range(n_limits)])
    y_bars_d2 =  array('f', [ebar_d2[i] * list(y_th_xsec.values())[i] for i in range(n_limits)])
    y_bars_u1 =  array('f', [ebar_u1[i] * list(y_th_xsec.values())[i] for i in range(n_limits)])
    y_bars_u2 =  array('f', [ebar_u2[i] * list(y_th_xsec.values())[i] for i in range(n_limits)])


x_bars_1 = array('f', [0] * n_limits)
x_bars_2 = array('f', [0] * n_limits)


median = ROOT.TGraph(n_limits, x_values, expected_values)
if theo:
    median = ROOT.TGraph(n_limits, x_values, y_xsec_vals)
    
median.SetLineWidth(2)
median.SetLineStyle(2)
median.SetLineColor(ROOT.kBlue)
median.SetFillColor(0)
median.GetXaxis().SetRangeUser(110, 150)

obs = ROOT.TGraph(n_limits, x_values, observed_values)
if theo: obs = ROOT.TGraph(n_limits, x_values, y_xsec_obs_vals)
obs.SetLineWidth(2)
obs.SetLineStyle(1)
obs.SetLineColor(ROOT.kBlue)
obs.SetFillColor(0)
obs.GetXaxis().SetRangeUser(110, 150)

theory = ROOT.TGraph(n_limits, x_values, y_th_xsec_vals)
theory.SetLineWidth(2)
theory.SetLineStyle(1)
theory.SetLineColor(ROOT.kRed)
theory.SetFillColor(ROOT.kWhite)

band_1sigma = ROOT.TGraphAsymmErrors(n_limits, x_values, expected_values, x_bars_1, x_bars_2, y_bars_d1, y_bars_u1)
if theo:
    band_1sigma = ROOT.TGraphAsymmErrors(n_limits, x_values, y_xsec_vals, x_bars_1, x_bars_2, y_bars_d1, y_bars_u1)
band_1sigma.SetFillColor(ROOT.kGreen + 1)
band_1sigma.SetLineColor(ROOT.kGreen + 1)
band_1sigma.SetMarkerColor(ROOT.kGreen + 1)

band_2sigma = ROOT.TGraphAsymmErrors(n_limits, x_values, expected_values, x_bars_1, x_bars_2, y_bars_d2, y_bars_u2)

if theo:
    band_2sigma = ROOT.TGraphAsymmErrors(n_limits, x_values, y_xsec_vals, x_bars_1, x_bars_2, y_bars_d2, y_bars_u2)

band_2sigma.SetTitle("")
band_2sigma.SetFillColor(ROOT.kOrange)
band_2sigma.SetLineColor(ROOT.kOrange)
band_2sigma.SetMarkerColor(ROOT.kOrange)
band_2sigma.GetXaxis().SetTitle("#it{m}_{Z'} [GeV]")
band_2sigma.GetXaxis().SetTitleOffset(0.80)
band_2sigma.GetXaxis().SetLabelSize(0.037)
band_2sigma.GetXaxis().SetTitleSize(0.049)

band_2sigma.GetYaxis().SetTitle("#sigma #times BR [pb]")
band_2sigma.GetYaxis().SetTitleOffset(0.75)
band_2sigma.GetYaxis().SetTitleSize(0.054)
band_2sigma.GetYaxis().SetLabelSize(0.041)
band_2sigma.GetYaxis().SetTitleFont(42)


legend = ROOT.TLegend(0.485,0.5,0.93,0.90)
legend.SetTextSize(0.039)
legend.SetFillStyle(0)
legend.SetBorderSize(0)
legend.SetHeader("95% CL upper limits")


if unblind:
    legend.AddEntry(obs,"Median observed")

legend.AddEntry(median,"Median expected")
legend.AddEntry(band_1sigma,"68% expected")
legend.AddEntry(band_2sigma,"95% expected")
legend.AddEntry(theory, "Theoretical")
# m_legend.AddEntry(theo, "Theoretical #sigma")
legend.SetEntrySeparation(0.3)
legend.SetFillColor(0)

c1 = ROOT.TCanvas()
ROOT.SetOwnership(c1, False)
c1.cd()
c1.SetGrid() 
c1.SetLogy(1)
band_2sigma.GetXaxis().SetRangeUser(600, 4400)
c1.Update()
band_2sigma.Draw("A3")
band_1sigma.Draw("3")
band_1sigma.SetMaximum(200)
median.Draw("L")

if unblind:
    obs.Draw("L")

theory.Draw("L same")
legend.Draw("Same")


def draw_labels():

    lumi_per_year = {
        "2016": "35.92 fb^{-1} (13 TeV)",
        "2017": "41.53 fb^{-1} (13 TeV)",
        "2018": "59.8 fb^{-1} (13 TeV)",
        "Run2": "137.19 fb^{-1} (13 TeV)",
    }

    label_lumi = ROOT.TLatex()
    label_cms = ROOT.TLatex()
    label_preliminary = ROOT.TLatex()
    
    label_lumi.SetNDC()
    label_cms.SetNDC()
    label_preliminary.SetNDC()
    
    label_lumi.SetTextFont(42)
    label_preliminary.SetTextFont(52)
    
    label_lumi.SetTextAlign(31)         # align right
    label_cms.SetTextAlign(11)          # align left
    label_preliminary.SetTextAlign(11)  # align left

    top_margin = ROOT.gPad.GetTopMargin()
    right_margin = ROOT.gPad.GetRightMargin()
    
    label_lumi.SetTextSize(0.33 * top_margin)
    label_cms.SetTextSize(0.48 * top_margin)
    label_preliminary.SetTextSize(0.39 * top_margin)

    label_text_offset = 0.2
    
    label_lumi.DrawLatex(1-right_margin, 1-top_margin+label_text_offset*top_margin, lumi_per_year[opt.year])
    label_cms.DrawLatex(0.15, 0.83,"CMS")
    label_preliminary.DrawLatex(0.17, 1-top_margin+label_text_offset*top_margin,"Work in progress")


draw_labels()


c1.Update()
c1.SaveAs("plots/test_limitPlot_%s_%s.pdf" % (opt.year, cat))
ROOT.gApplication.Run()
