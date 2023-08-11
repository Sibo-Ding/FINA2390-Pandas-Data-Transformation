# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:23:32 2023

@author: Sibo Ding
"""

import pandas as pd

df = pd.read_csv('simplified.csv')

a = pd.melt(df, 
            id_vars=['id', 'name'], 
            value_vars=['quarter__12', 'quarter__9', 'quarter', 'quarter_7',
                        'quarter_10', 'Con_Mon__12', 'Con_Mon__9', 'Con_Mon',
                        'Con_Mon_7', 'Con_Mon_10'])

# Split variable names and quarters
a['quarter_to'] = [-12, -12, -12, -9, -9, -9, 0, 0, 0, 7, 7, 7, 10, 10, 10,
                -12, -12, -12, -9, -9, -9, 0, 0, 0, 7, 7, 7, 10, 10, 10]
a['variable'] = ['quarter', 'quarter', 'quarter', 'quarter', 'quarter',
                 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 
                 'quarter', 'quarter', 'quarter', 'quarter', 'quarter', 
                 'Con_Mon', 'Con_Mon', 'Con_Mon', 'Con_Mon', 'Con_Mon', 
                 'Con_Mon', 'Con_Mon', 'Con_Mon', 'Con_Mon', 'Con_Mon', 
                 'Con_Mon', 'Con_Mon', 'Con_Mon', 'Con_Mon', 'Con_Mon']

# Add `quarter_to` to index
b = pd.pivot(a, index=['id', 'name', 'quarter_to'], columns='variable', values='value')
