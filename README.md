# sim-low-input
A tool for simulating PacBio Low DNA Input HiFi Data. This tool requires standard HiFi data and simulates reads with the length distribution of low DNA input libraries.

## Usage
`usage: simulate_lowInputHiFi.py [-h] infastq total hist

Simulate desired read length distribution from hifi fastq

positional arguments:
  infastq     input fastq file
  total       total desired data in Gb
  hist        csv read length histogram in 1kb bins

optional arguments:
  -h, --help  show this help message and exit`

### Example
`simulate_lowinput_readlengths.py std_hifi.fastq 0.0001 low-input.hist.csv`

## Input
1. Standard PacBio HiFi library fastq
2. Histogram of read lengths
3. Total Gb of data desired

## Output
Fasta of HiFi reads with desired read length distribution 

## Dependencies
python 3 libraries `os` `seqio` `argparse` `numpy`

