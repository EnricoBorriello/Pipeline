# Code to visualize the Pipeline


from utils_analysis import customer_detail, partial_pipeline_summary
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def visualize_partial_pipeline (detail,detail_type):

    if detail_type == 'pre':
        label1 = '$ Expected FTB Bookings'
        label2 = '# Expected FTB Accounts'
        color = 'C1'
    if detail_type == 'post':
        label1 = '$ Confirmed Pipeline Bookings'
        label2 = '# Confirmed Pipeline Accounts'
        color = 'C0'

    df_exp = partial_pipeline_summary( detail , detail_type)


    ax = (df_exp.T).plot(kind='bar',
                    y=label1,
                    rot=90, width=0.8, edgecolor='black',
                    legend=False,
                    title=label1,
                    color = color);
    ax.set_axisbelow(True)
    ax.yaxis.grid(True)
    ax.spines['left'].set_linewidth(1.2)   # Left spine
    ax.spines['bottom'].set_linewidth(1.2) # Bottom spine
    ax.spines['right'].set_visible(False) # Right spine
    ax.spines['top'].set_visible(False)   # Top spine

    # Format y-axis tick labels
    ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.0f}'))
    #plt.legend()
    
    # Display the plot and then close it
    plt.show()
    
    #Otherwise
    #return plt;


def visalualize_total_pipeline (df_total,df_expected):

    ax = (df_total.T).plot(kind='bar',
                    y='$ Total Pipeline',
                    rot=90, width=0.8, edgecolor='black',
                    legend=False,
                    title='Total Pipeline',
                    color = 'C0');
    ax.set_axisbelow(True)
    ax.yaxis.grid(True)
    ax.spines['left'].set_linewidth(1.2)   # Left spine
    ax.spines['bottom'].set_linewidth(1.2) # Bottom spine
    ax.spines['right'].set_visible(False) # Right spine
    ax.spines['top'].set_visible(False)   # Top spine

    ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.0f}'))


    ax = (df_expected.T).plot(kind='bar',
                    figsize=(10, 3),
                    y='$ Total Pipeline',
                    rot=90, width=0.5, edgecolor='black',
                    legend=False,
                    #title=label1,
                    color = 'C1');
    ax.set_axisbelow(True)
    ax.yaxis.grid(True)
    ax.spines['left'].set_linewidth(1.2)   # Left spine
    ax.spines['bottom'].set_linewidth(1.2) # Bottom spine
    ax.spines['right'].set_visible(False) # Right spine
    ax.spines['top'].set_visible(False)   # Top spine

    ax.yaxis.set_major_formatter(mticker.StrMethodFormatter('${x:,.0f}'))

    #ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

    legend_labels = ['Confirmed Pipeline Bookings','Expected FTB Bookings']
    ax.legend(legend_labels, loc='lower left', bbox_to_anchor=(0.7, 0.8))

    # Display the plot and then close it
    plt.show()