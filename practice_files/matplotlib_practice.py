""" File for expirimenting with matplotlib non-dataframe graphing """
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

penguins = pd.read_csv("penguins.csv")

def calc_population_totals():
    """ Calculate total penguin populations and return a dict containing the total population of each island and species 
The result should be: {'Torgersen': 52, 'Dream': 124, 'Biscoe': 168, 'Adelie': 152, 'Chinstrap': 68, 'Gentoo': 124}
    """
    totals = {"Torgersen":0, "Dream":0,"Biscoe":0,"Adelie":0,"Chinstrap":0,"Gentoo":0}

    for i in penguins["island"]:
        if i in totals:
            totals[i] += 1

    for j in penguins["species"]:
        if j in totals:
            totals[j] += 1

    return totals

""" pop_total = calc_population_totals()

catagories = ["Torgersen", "Dream","Biscoe","Adelie","Chinstrap","Gentoo"]

pops = [pop_total["Torgersen"],pop_total["Dream"],pop_total["Biscoe"],pop_total["Adelie"],pop_total["Chinstrap"],pop_total["Gentoo"]]
 """
#single axes = fig, ax = plt.subplots()

def graph_populations(pop_total = calc_population_totals()):
    "Graphs populations of all sialds and species, calls calc_population_totals for data if none is provided"

    catagories = []
    for k in pop_total:
        catagories.append(k)
    
    pops = []
    for k in pop_total:
        pops.append(pop_total[k])

    fig, ax = plt.subplots(figsize=(5,3),layout="constrained")

    ax.bar(catagories,pops)

    plt.show()


pop_total = calc_population_totals()



#fig, ax =plt.subplots(2,2)

#fig = plt.figure(figsize=(5.5,4), layout="constrained")
""" fig.add_gridspec(3,4) """

""" ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,4,3) """

#fig, ax = plt.subplots(3,figsize=(3,4),layout="constrained") - use to create graphs for each island

fig, ax = plt.subplots(3,figsize=(3,4),layout="constrained",)
#graph one of the sub plots
ax[0].plot([1,2,5,4],[5,4,2,1])

ax[1].plot.bar()
plt.show()