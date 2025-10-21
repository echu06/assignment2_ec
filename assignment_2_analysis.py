import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

penguins = pd.read_csv('penguins.csv')

'''
There are multiple columns here, the columns being:

- species, 
- island, 
- bill length of a penguin (length of their beak) in millimeters
- bill depth of a penguin (how deep their beak is) in millimeters
- flipper length in millimeters
- body mass in grams
- sex
- year this observation was recorded. 
'''

'''
Primary Question: How does the interaction of time and island 
influence the different penguin's body mass? 
'''



'''
Descriptive Statistics Section: Creating bivariate graphs
'''


# To graph it use the following steps:


# First, define the type of plot style you want to use:
plot.style.use('seaborn-v0_8-pastel')   

# Next the font that you want to have:
plot.rcParams.update({'font.family': 'serif'})
 

# receive frequencies of different combinations
table = penguins[['island', 'species']].value_counts()
# push the table into the plot function of matplot. 
# set it as an object to manipulate it later for use:
ax  = table.unstack().plot(kind='bar')

# Then add on title, x label, y label features:
ax.set_title('Penguin Species Count by Island', fontsize=16, 
             fontweight='bold', pad=15)
ax.set_xlabel('Island', fontsize=13, labelpad=10)
ax.set_ylabel('Count', fontsize=13, labelpad=10)

ax.legend(title='Species', title_fontsize=12, 
          fontsize=10, frameon=True)

ax.grid(axis='y', linestyle='--', alpha=0.7)
plot.tight_layout()
plot.show()


'''
Making frequency plots of the penguin's body mass per species
'''

# Use histogram function instead and specify bins and optimal layout. 
# layout = (1,3) indicates you want a layout of one row 3 columns. 

ax = penguins['body_mass_g'].hist(by = penguins['species'], bins = 20, 
                                  layout= (1,3))

# Since we have an array of items now due to several graphs, we need to now loop over them:

for ax in ax.flatten():  
    ax.grid(axis='y', linestyle='--', alpha=0.7) # these change the lines for each graph

plot.tight_layout(rect = [0.1,0.1,1,0.90]) # alter arguments to make sure plot has x and y axis labels
plot.suptitle('Penguin Body Mass Distribution \n for Each Species', fontsize = 14) # set the title
fig = plot.gcf()
fig.supylabel('Frequency', x = 0.03)
fig.supxlabel('Body Mass (g)', y =0.03)
plot.show()

'''
Now observing this over the different time periods, 
we have the means of the different species per year:
'''


averages = penguins['body_mass_g'].groupby([penguins['species'], penguins['year']]).mean()
av = averages.unstack().plot(kind = 'bar')
av.set_title('Average Body Mass in Grams Per Species for Each Year')
av.set_xlabel('Species')
av.set_ylabel('Body Mass in Grams')
av.legend(title='Year', title_fontsize=12, 
          fontsize=10, frameon=True)

av.grid(axis='y', linestyle='--', alpha=0.7)
plot.tight_layout()
plot.show()


# Now saving the plots as a pdf
with PdfPages('descriptive_plots.pdf') as pdf:

    # The first plot:
    averages = penguins['body_mass_g'].groupby([penguins['species'], penguins['year']]).mean()
    av = averages.unstack().plot(kind = 'bar')
    av.set_title('Average Body Mass in Grams Per Species for Each Year')
    av.set_xlabel('Species')
    av.set_ylabel('Body Mass in Grams')
    av.legend(title='Year', title_fontsize=12, 
            fontsize=10, frameon=True)

    av.grid(axis='y', linestyle='--', alpha=0.7)
    plot.tight_layout()
    pdf.savefig() # saving the first figure
    plot.close()

    # The second plot:
    ax = penguins['body_mass_g'].hist(by = penguins['species'], bins = 20, 
                                    layout= (1,3))
    for ax in ax.flatten():  
        ax.grid(axis='y', linestyle='--', alpha=0.7) 
    plot.tight_layout(rect = [0.1,0.1,1,0.90])
    plot.suptitle('Penguin Body Mass Distribution \n for Each Species', 
                  fontsize = 14) 
    fig = plot.gcf()
    fig.supylabel('Frequency', x = 0.03)
    fig.supxlabel('Body Mass (g)', y = 0.03)
    pdf.savefig()
    plot.close()

    # The third plot:
    ax  = table.unstack().plot(kind='bar')
    ax.set_title('Penguin Species Count by Island', fontsize=16, 
                fontweight='bold', pad=15)
    ax.set_xlabel('Island', fontsize=13, labelpad=10)
    ax.set_ylabel('Count', fontsize=13, labelpad=10)

    ax.legend(title='Species', title_fontsize=12, 
            fontsize=10, frameon=True)

    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plot.tight_layout()
    pdf.savefig()
    plot.close()

