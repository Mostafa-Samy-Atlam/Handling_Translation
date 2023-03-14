# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 10:53:45 2023

@author: mostafa
"""
# Importing Libraries
from deep_translator import GoogleTranslator
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re    
import pandas as pd

# Open Excel sheet that ccontains all html files locations.
data=pd.read_excel(io='data.xlsx' ,dtype={'file_location':object})

# Convert dataframe that contains the files locations into a list.
col_list = data["file_location"].values.tolist()

# A function to translate string and text in HTML files into Hindi. 
def trans_fun(x):
    translated = GoogleTranslator(source='auto', target='hi').translate(x)
    return translated

# A funtion that replaces English String with Hindi String.
def replacement_function(soup):
    x = [tag for tag in soup.find_all(string=True)]
    for i in x:
        try:
            translated = trans_fun(i.string)
            i.string.replace_with(f"{translated}")
        except Exception as ex:
            pass
    return soup    

# For loop to pass through all pathes of HTML files.
for i in col_list:
    raw_s = r'{}'.format(i)
    with open(raw_s, encoding="utf8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    # Call functions    
    after_modification = replacement_function(soup)
        
    with open(raw_s, "w", encoding="utf-8") as f:
        f.write(str(soup))
    
    