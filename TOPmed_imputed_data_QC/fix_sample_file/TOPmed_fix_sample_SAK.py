# Upload this file to your project and provide it as an input to the swiss-army-knife app

from glob import glob
import os

files = [f for f in glob("/mnt/project/Bulk/Imputation/Imputation from genotype (TOPmed)/*.sample")]

for file in files:
    prefix = file.split('/')[-1].split('.')[0]
    sample = []
    with open(file) as f:
        for i, line in enumerate(f):
            if i == 1:
                sample.append('0 0 0 D\n')
            else:
                sample.append(line)
    filename = f'{prefix}.sample'
    with open(filename, 'w') as f:
        for line in sample:
            f.write(f'{line}')
