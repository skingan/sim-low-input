#!/usr/bin/env python3

import os
from Bio import SeqIO
import csv
from argparse import ArgumentParser
import numpy as np
import matplotlib.pyplot as plt


# define command line arguments, program description, and help
desc ='''Simulate desired read length distribution from hifi fastq'''
parser = ArgumentParser(description=desc)
parser.add_argument("infastq", help="input fastq file")
parser.add_argument("total", help="total desired bases in Gb")
parser.add_argument("hist", help="csv read length histogram in 1kb bins")
args = parser.parse_args()

# get infiles and dir
cwd = os.getcwd()
infq = args.infastq
total = args.total
hist = args.hist


# get simulated read lengths

# read data
hist = hist
data = np.genfromtxt(hist, delimiter=',', names = True)
bin_upper = data['upper']
count = data['counts']

# made cdf
cdf = np.cumsum(count)
cdf = cdf / cdf[-1]

# simulate random read lengths
values = np.random.rand(3000000)
value_bins = np.searchsorted(cdf, values)
sim_lengths = list(bin_upper[value_bins])

bp = 0
total = float(total) * 1e9

#with open(infq, "r") as input_handle:
input_handle = open(infq, "r")
record_iterator = SeqIO.parse(input_handle, "fastq")
while (bp < total):
    record = next(record_iterator)
    read_length = int(sim_lengths.pop(0))
    # if read length is shorter than simulated length skip it to preserve distribution
    if (read_length > len(record.seq)):
#        read_length = len(record.seq) # this changes shape of read length hist
        continue
    print(">",record.id,sep="")
    print(record.seq[:read_length])
    bp = bp + read_length
input_handle.close()
    
