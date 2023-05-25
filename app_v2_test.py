import streamlit as st
# Set the width of the Streamlit application
st.set_page_config(layout="wide")

from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker
from datetime import datetime, timedelta

# custom packages
from utils_dates import find_date_range, extract_date
from utils_analysis import customer_detail, partial_pipeline_summary
from utils_visualizations_v2 import vialualize_partial_pipeline, vialualize_total_pipeline


# Custom settings: Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Custom settings: Filter or ignore the warning
#import warnings
#warnings.filterwarnings("ignore", category=pd.core.common.SettingWithCopyWarning)



# ---------------------

# IMPUT FILES
st.sidebar.subheader('Input CSV files')
uploaded_pre_file = st.sidebar.file_uploader("Choose a file (Pre-FTB Report)",key=0)
uploaded_post_file = st.sidebar.file_uploader("Choose a file (Post-FTB Report)",key=1)

# ---------------------

if uploaded_pre_file is not None and uploaded_post_file is not None:

  df_pre = pd.read_csv(uploaded_pre_file)
  df_post = pd.read_csv(uploaded_post_file)

  df_pre['Annual hotel spend'] = df_pre['Annual hotel spend'].fillna(0).astype(int)
  df_post['Annual hotel spend'] = df_post['Annual hotel spend'].fillna(0).astype(int)


  # difference in the input files from pre to post
  # the FTB includes both date and time
  #  we just need the date
  df_post['Expected FTB Date'] = [extract_date(date_time) for date_time in df_post['FTB or Revival Date'] ]
  df_post = df_post.drop('FTB or Revival Date', axis=1)

# ---------------------

# OWNERS
if uploaded_pre_file is not None and uploaded_post_file is not None:

  pre_owners = np.sort(np.array(df_pre['Opportunity Owner'].unique()))
  post_owners = np.sort(np.array(df_post['Opportunity Owner'].unique()))

  missing_owners = [owner for owner in pre_owners if owner not in post_owners]

  # I will only keep owners that are in both pre and post reports

  # Convert arrays to sets
  set1 = set(pre_owners)
  set2 = set(post_owners)

  # Find the intersection of the sets
  common_elements = set1.intersection(set2)

  # Convert the common elements set back to a list
  names = list(common_elements)

  # sort it alphabetically by family name
  owners_list = sorted(names, key=lambda x: x.split()[1])

# ---------------------


if uploaded_pre_file is not None and uploaded_post_file is not None:

  col1, col2 = st.columns(2)
  with col1:
    # LOGO
    logo = Image.open('HE_Logo_Black.jpg')
    st.image(logo,width=600)
  with col2:
    st.empty()


  st.header('Monthly Pipeline Review')
  # SELECT OWNER
  col1, col2 = st.columns([1,1])
  with col1:
    owner = st.selectbox(
    'Account Executive:',
    owners_list)
  with col2: 
    st.empty() # or:
    #option = st.selectbox(
    #'Some other option:',
    #['option '+str(i) for i in range(1,5)]   )

# DETAIL DATA
  detail_pre = customer_detail(df_pre,owner)
  detail_post = customer_detail(df_post,owner)
  detail_pre.set_index('Account Name', inplace=True)
  detail_post.set_index('Account Name', inplace=True)






# ...








# Prospects (PRE-FTB) DETAIL
  with st.expander('Prospects (Pre-FTB) Detail'):
    col1, col2 = st.columns(2)
    with col1:
      st.subheader('Prospects (Pre-FTB) Detail')
      vialualize_partial_pipeline (detail_pre,detail_type='pre')
      st.pyplot(plt)
    with col2:
      st.empty()
    st.dataframe(detail_pre)


# Customers (POST-FTB) DETAIL
  with st.expander('Customers (Post-FTB) Detail'):
    col1, col2 = st.columns(2)
    with col1:
      st.subheader('Prospects (Pre-FTB) Detail')
      vialualize_partial_pipeline (detail_post,detail_type='post')
      st.pyplot(plt)
    with col2:
      st.empty()
    st.dataframe(detail_post)