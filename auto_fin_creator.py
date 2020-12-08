#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import os

import pdfplumber
import pandas as pd
from collections import namedtuple


# In[2]:


Line = namedtuple('Line','t_date description amount')
line_re = re.compile(r"^\d{2}\D{3}")
transaction_line = re.compile("(^\d{2}\D{3}) ([\D\d/./-/*]*) ([\d,]+\.\d{2}[\D{2}]*) ([\d,]+\.\d{2}\D{2})")


# In[3]:


file = os.path.join(os.path.expanduser('~'),'Dropbox','Apperly','Finances','Financial_Statements','62681375004 2019-01-07.pdf')


# In[4]:


output_file = os.path.join(os.path.expanduser('~'),'Dropbox','Apperly','Finances','Financial_Statements','62681375004 2019-01-07.csv')


# In[ ]:





# In[5]:


lines = []
total_check = 0
count =0

with pdfplumber.open(file) as pdf: 
    pages = pdf.pages
    for page in pdf.pages:
        text = page.extract_text()
        #print(text)
        for line in text.split('\n'):
            #print(line)
            if line_re.search(line):
                cl = transaction_line.search(line)
                if cl:
                    
                    print(cl.group(1), cl.group(2), cl.group(3))
                    lines.append(Line(cl.group(1), cl.group(2), cl.group(3)))
                    count = count +1 
                    
print("Count = ",count)
        
           


# In[ ]:





# In[6]:


df = pd.DataFrame(lines)
df.head()


# In[7]:


df.to_csv(output_file, index=True)


# In[ ]:




