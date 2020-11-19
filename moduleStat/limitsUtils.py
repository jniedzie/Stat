import sys
import os
import subprocess
import string
import optparse

from moduleStat.settings import *


class Limit(object):
    combine_label_to_arg_name = {
        "Expected 50.0%": "value",
        "Observed": "observed",
        "Expected 84.0%": "points_up_1_sigma",
        "Expected 97.5%": "points_up_2_sigma",
        "Expected 16.0%": "points_down_1_sigma",
        "Expected  2.5%": "points_down_2_sigma",
    }

    label_to_attr_name = {
        "mass": "mass",
        "y_vals": "value",
        "y_observed": "observed",
        "y_up_points1": "points_up_1_sigma",
        "y_up_points2": "points_up_2_sigma",
        "y_down_points1": "points_down_1_sigma",
        "y_down_points2": "points_down_2_sigma",
    }
    
    def __init__(self):
        self.mass = 0.
        self.value = 0.
        self.observed = 0.
        self.points_up_1_sigma = 0.
        self.points_up_2_sigma = 0.
        self.points_down_1_sigma = 0.
        self.points_down_2_sigma = 0.

    def print(self):
        print("\n\nLimits:")
        print("Mass: ", self.mass)
        print("Values: ", self.value)
        print("Observed: ", self.observed)
       

def get_limit_from_combine_log(log_path):
    input_file = open(log_path)
    print("Reading ", log_path)

    limit = Limit()
   
    for line in input_file.readlines():
        if line.strip() == "":
            continue
        
        l_split = line.split()
        
        for label, arg_name in limit.combine_label_to_arg_name.items():
            if line.startswith(label):
                setattr(limit, arg_name, l_split[4])
            
    return limit


def writeFile(limits, suffix, outname):
    
    lines = {}
    
    for label, attr_name in Limit.label_to_attr_name.items():
        lines[label] = "{}{}\t".format(label, suffix)
    
    limits_ordered_by_mass = collections.OrderedDict(sorted(limits.items()))
    
    for mass, limit in limits_ordered_by_mass.items():
        for label, attr_name in Limit.label_to_attr_name.items():
            lines[label] += "{}\t".format(getattr(limit, attr_name))
    
    output_string = ""
    
    for line in lines.values():
        output_string += "{}\n".format(line)
    
    print("\n", output_string)
    
    limits_file = open(outname, 'w')
    limits_file.write(output_string)
    limits_file.close()


def get_limits(base_path, suffix):
    limits = {}
    
    if not os.path.isdir("data/"):
        os.system('mkdir data/')
    
    r_invs = set()
    
    for item in sigpoints:
        mZprime = item[0]
        mDark = item[1]
        rinv = item[2]
        alpha = item[3]
        
        sample_base_name = "mZprime{}_mDark{}_rinv{}_alpha{}".format(mZprime, mDark, rinv, alpha)
        
        file_name = "{}/".format(base_path)
        file_name += "SVJ_{}/".format(sample_base_name)
        file_name += "asymptotic_{}{}.log".format(sample_base_name, suffix)
        
        r_invs.add(rinv)
        
        print("r_inv: ", rinv, "\tmZ: ", mZprime)
        
        if rinv not in limits:
            limits[rinv] = {}
        
        limits[rinv][float(mZprime)] = get_limit_from_combine_log(file_name)
        limits[rinv][float(mZprime)].mass = float(mZprime)
    
    for r_inv in r_invs:
        writeFile(limits[r_inv], suffix, "data/limit_rinv" + r_inv + suffix + ".txt")
