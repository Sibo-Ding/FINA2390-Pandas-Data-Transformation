# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:02:13 2023

@author: Sibo Ding
"""

import pandas as pd

df = pd.read_csv('simplified.csv')

df = df.set_index(['id', 'name'])

# Split variable names and quarters
arrays = [
    ['quarter', 'quarter', 'quarter', 'quarter', 'quarter', 
     'Con_Mon', 'Con_Mon', 'Con_Mon', 'Con_Mon', 'Con_Mon'],
    [-12, -9, 0, 7, 10, -12, -9, 0, 7, 10]]
tuples = list(zip(*arrays))
df.columns = pd.MultiIndex.from_tuples(tuples)

ab = df.stack()
