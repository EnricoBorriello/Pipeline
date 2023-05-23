# Code for Customer Detail


from datetime import datetime, timedelta
from utils_dates import find_date_range, extract_date
import pandas as pd


def customer_detail(df,owner):

    # select the data you need:
    df0 = df[df['Opportunity Owner']==owner]
    df1 = df0.dropna(subset=['Expected FTB Date'])
    df2 = df1[['Account Name','Expected FTB Date','Annual hotel spend']]
    
    # Define the range using the first and second dates
    start_date_str = find_date_range(df2['Expected FTB Date'])[0]
    end_date_str = find_date_range(df2['Expected FTB Date'])[1]

    # Convert the start and end dates to datetime objects
    start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
    end_date = datetime.strptime(end_date_str, "%m/%d/%Y")

    # Add one year to the end date
    end_date_plus_one_year = end_date + timedelta(days=365)

    # Iterate through the months and print the abbreviated month and year

    col = [0 for i in range(len(df2))]

    current_date = start_date
    while current_date < end_date_plus_one_year:
        #print(current_date.strftime("%b %Y"))
        df2[str(current_date.strftime("%b %Y"))] = col
        current_date += timedelta(days=30) 
    
    for i in range(len(df2)): # loop over accounts for given owner
        start_date = df2.at[df2.index[i],'Expected FTB Date']
        spend = df2.at[df2.index[i],'Annual hotel spend']
        # Convert the date string to a datetime object
        date = datetime.strptime(start_date, "%m/%d/%Y")
        # loop over the following 12 months
        for j in range(12):
            label = date.strftime("%b %Y")  # Format the date as "Abbreviated Month Year"
            df2.at[df2.index[i],label] = round(spend/12)
            # Add 30 days to the date for the next month
            date += timedelta(days=30)
        # to make sure empty months don't return NaN when divided by zero:
        df2.fillna(int(0), inplace=True, downcast='infer')     


    # This reproduces the content of "Prospect (Pre-FTB) detail"
    # Now I need to reproduce "Customers (Post-FTB) Detail"
    # and "Pipeline Summary"

    sorted_df2 = df2.sort_values(by='Annual hotel spend',ascending=False)
    
    return sorted_df2


def partial_pipeline_summary( detail , detail_type ):
    # detail type can be either 'pre' or 'post'
    
    numeric_columns = detail.select_dtypes(include='number')
    cols = numeric_columns.columns

    # Here are the first two lines of "Pipeline Summary":

    numeric_columns = detail.select_dtypes(include='number')
    df1exp = (pd.DataFrame(numeric_columns.sum()))
    df2exp = pd.DataFrame((detail[cols] != 0).sum())

    if detail_type == 'pre':
        label1 = '$ Expected FTB Booking'
        label2 = '# Expected FTB Accounts'
    if detail_type == 'post':
        label1 = '$ Confirmed Pipeline Bookings'
        label2 = '# Confirmed Pipeline Accounts'

    df1exp.rename(columns={0: label1}, inplace=True)
    df2exp.rename(columns={0: label2}, inplace=True)

    df_exp = (pd.concat([df1exp, df2exp], axis=1)[1:]).transpose()

    return df_exp