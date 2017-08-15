# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:59:36 2017

@author: jonatha
"""
from avro import schema, datafile, io
import json 
import pprint 

OUTFILE_NAME= 'part_00000_of_01862.avro'
rec_reader= io.DatumReader()

df_reader = datafile.DataFileReader(
    open(OUTFILE_NAME),
    rec_reader
)

pp = pprint.PrettyPrinter()

for record in df_reader:
        pp.pprint(record)
        
        
aux = json.loads(df_reader)