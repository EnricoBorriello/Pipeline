import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

import math
import numpy as np

import altair as alt

from PIL import Image




# ---------------------



# ---------------------

logo = Image.open('HE_Logo_Black.jpg')
st.image(logo)

# ---------------------


st.header('Monthly Pipeline Review')
#st.write('**contact:** enrico.borriello@asu.edu - **Latest update:** Apr 11, 2023')


#f = open('email.txt', 'r')
#content = f.read()
#with st.expander("Shade's email"):
#    st.write(content)

# IMPUT FILE
st.sidebar.subheader('Input CSV files')
uploaded_pre_file = st.sidebar.file_uploader("Choose a file (Pre-FTB Report)",key=0)
uploaded_post_file = st.sidebar.file_uploader("Choose a file (Post-FTB Report)",key=1)


col1, col2 = st.columns([1,1])

features_columns = ['triad_'+("%02d" % (number,)) for number in range(1,14)]




if uploaded_pre_file is not None and uploaded_post_file is not None:

  df_pre = pd.read_csv(uploaded_pre_file)
  df_post = pd.read_csv(uploaded_post_file)
    
  pre_owners = np.sort(np.array(df_pre['Opportunity Owner'].unique()))
  post_owners = np.sort(np.array(df_post['Opportunity Owner'].unique()))

  owner = st.selectbox(
    'Account Executive:',
    pre_owners)

  accounts_pre = df_pre[df_pre['Opportunity Owner']==owner][
    ['Account Name',
     #'Opportunity Name',
     #'Stage',
     #'Expected FTB Date',
     'Annual hotel spend'  #,
     #'Account: Last Activity'
     ]].sort_values(by=['Annual hotel spend'], ascending=False
      ).set_index('Account Name'
      )#.style.set_precision(0)

  accounts_post = df_post[df_post['Opportunity Owner']==owner][
    ['Account Name',
     #'Opportunity Name',
     #'Stage',
     #'FTB or Revival Date',
     'Annual hotel spend' #,
     #'Account: Last Activity'
     ]].sort_values(by=['Annual hotel spend'], ascending=False
      ).set_index('Account Name'
      )#.style.set_precision(0)



  st.subheader('Prospects (Pre-FTB) View Summary')
  st.dataframe(accounts_pre)

  st.subheader('Customers (Post-FTB)')
  st.dataframe(accounts_post)



