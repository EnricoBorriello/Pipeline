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

  st.header('Monthly Pipeline Review')

  df_pre = pd.read_csv(uploaded_pre_file)
  df_post = pd.read_csv(uploaded_post_file)
  
  # replacing NaN with 0 
  # making 'Annual hotel spend' int
  df_pre['Annual hotel spend'] = df_pre['Annual hotel spend'].fillna(0).astype(int)
  df_post['Annual hotel spend'] = df_post['Annual hotel spend'].fillna(0).astype(int)

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
      ).rename(columns={'Account Name':'account','Annual hotel spend':'AHS'})
      #.set_index('Account Name'
      #).style.set_precision(0)

  accounts_post = df_post[df_post['Opportunity Owner']==owner][
    ['Account Name',
     #'Opportunity Name',
     #'Stage',
     #'FTB or Revival Date',
     'Annual hotel spend' #,
     #'Account: Last Activity'
     ]].sort_values(by=['Annual hotel spend'], ascending=False
      ).rename(columns={'Account Name':'account','Annual hotel spend':'AHS'})
      #.set_index('Account Name'
      #).style.set_precision(0)


  max_bars = 16

  with st.expander('Prospects (Pre-FTB) View Summary'):

    st.subheader('Prospects (Pre-FTB) View Summary')
    col1, col2 = st.columns([1,1])
  
    with col1:
      df0 = df_pre[df_pre['Opportunity Owner']==owner]
      df = df0.sort_values(by=['Annual hotel spend'],ascending = False).iloc[:max_bars]

      c = alt.Chart(df).mark_bar().encode(
        alt.X('Account Name',sort = None),
        alt.Y('Annual hotel spend', axis=alt.Axis(grid=False))
        ).properties(width=400,height=450).mark_bar(size=13)

      st.altair_chart(c, use_container_width=True)

    with col2:
      st.dataframe(accounts_pre)


  with st.expander('Customers (Post-FTB)'):

    st.subheader('Customers (Post-FTB)')
    col1, col2 = st.columns([1,1])
  
  
    with col1:
      df0 = df_post[df_post['Opportunity Owner']==owner]
      df = df0.sort_values(by=['Annual hotel spend'],ascending = False).iloc[:max_bars]
                     
      c = alt.Chart(df).mark_bar().encode(
        alt.X('Account Name',sort = None),
        alt.Y('Annual hotel spend', axis=alt.Axis(grid=False))
        ).properties(width=400,height=450).mark_bar(size=13)

      st.altair_chart(c, use_container_width=True)

    with col2:
      st.dataframe(accounts_post)

