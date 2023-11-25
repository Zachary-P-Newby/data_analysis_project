""" File for creating functions to answer questions and graph data"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

""" 1. On which of the three islands (Dream, Biscoe, and Torgenson) were penguins with long flippers (greater than the average length for the species_
(chinstrap, gentoo, and adelie) most common?

2. Is there a correlation between penguin bill length and depth? And if so, what species and island had the penguins with the largest bills? (Bills that are both deep and long) """

""" You must demonstrate the ability to do one or more of the following to achieve each answer: filter, sort, aggregate (sum, average, count), or data conversion. """

global penguins 
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
#print(pop_total)

pop_array = []
for k in pop_total:
    pop_array.append(pop_total[k]) """


""" plt.show() """


#Question 1 expiriments

#print(type(penguins["flipper_length_mm"])) = series

#print(penguins[penguins["species"] == "Adelie"]) - this species only

#get median flipper length of all adelie penguins
#adelie_mean_flipper_length = penguins[penguins["species"] == "Adelie"]["flipper_length_mm"].median()

#Get medain dlipper length of each species
""" adelie_mean_flipper_length = penguins[penguins["species"] == "Adelie"]["flipper_length_mm"].median()
chinstrap_mean_flipper_length = penguins[penguins["species"] == "Chinstrap"]["flipper_length_mm"].median()
gentoo_mean_flipper_length = penguins[penguins["species"] == "Gentoo"]["flipper_length_mm"].median()

print(f"Adelie Penguin medain flipper length: {adelie_mean_flipper_length} mm")
print(f"Chinstrap Penguin medain flipper length: {chinstrap_mean_flipper_length} mm")
print(f"Gentoo Penguin medain flipper length: {gentoo_mean_flipper_length} mm") """

def _calculate_median_flipper_lengths():
    """ Calculates the median flipper lengths of each species and saves them to a dictionary.
    These will be used for determinining if a penguin has a long flipper, for our purposes, a long flipper is above the average (mean) length for the species."""
    median_flipper_lengths = dict()
    #Get medain dlipper length of each species and save to dict
    median_flipper_lengths["adelie_mean_flipper_length"] = penguins[penguins["species"] == "Adelie"]["flipper_length_mm"].median()
    median_flipper_lengths["chinstrap_mean_flipper_length"] = penguins[penguins["species"] == "Chinstrap"]["flipper_length_mm"].median()
    median_flipper_lengths["gentoo_mean_flipper_length"] = penguins[penguins["species"] == "Gentoo"]["flipper_length_mm"].median()
    return median_flipper_lengths

median_flipper_lengths = _calculate_median_flipper_lengths()

#Filter out penguins with flippers longer than average
""" print(f"\nAdelie Penguin medain flipper length: {median_flipper_lengths["adelie_mean_flipper_length"]} mm")
adelie_long_flippers = penguins[(penguins["species"] == "Adelie") & (penguins["flipper_length_mm"] >= median_flipper_lengths["adelie_mean_flipper_length"])] 

print(adelie_long_flippers)

print(f"\nGentoo Penguin medain flipper length: {median_flipper_lengths["gentoo_mean_flipper_length"]} mm")
gentoo_long_flippers = penguins[(penguins["species"] == "Gentoo") & (penguins["flipper_length_mm"] >= median_flipper_lengths["gentoo_mean_flipper_length"])] 

print(gentoo_long_flippers)


print(f"\nChinstrap Penguin medain flipper length: {median_flipper_lengths["chinstrap_mean_flipper_length"]} mm")
chinstrap_long_flippers = penguins[(penguins["species"] == "Chinstrap") & (penguins["flipper_length_mm"] >= median_flipper_lengths["chinstrap_mean_flipper_length"])] 

print(chinstrap_long_flippers) """

""" print(f"\nAdelie Penguin medain flipper length: {median_flipper_lengths["adelie_mean_flipper_length"]} mm")
adelie_long_flippers = penguins[(penguins["species"] == "Adelie") & (penguins["flipper_length_mm"] >= median_flipper_lengths["adelie_mean_flipper_length"])] 
#print(adelie_long_flippers) #prints penguins in order of index
print(adelie_long_flippers)
adelie_long_flippers.sort_values(by="flipper_length_mm", inplace=True)#prints penguins in order of flipper length

print(adelie_long_flippers)
#print(adelie_long_flippers["flipper_length_mm"].sort_values())# sorts just flipper_length_mm coulumn - its a series
adelie_long_flippers["flipper_length_mm"].plot()
plt.show() """


""" Problem: Chinstrap penguins are only found on Dream island
print(penguins[(penguins["species"] == "Chinstrap") & (penguins["island"] == "Biscoe")]) - empty
print(penguins[(penguins["species"] == "Chinstrap") & (penguins["island"] == "Torgersen")]) - empty
print(penguins[(penguins["species"] == "Chinstrap") & (penguins["island"] == "Dream")]) """

#Adelie PEnguins are found on all three islands
""" print(penguins[(penguins["species"] == "Adelie") & (penguins["island"] == "Biscoe")])
print(penguins[(penguins["species"] == "Adelie") & (penguins["island"] == "Torgersen")])
print(penguins[(penguins["species"] == "Adelie") & (penguins["island"] == "Dream")]) """

#Gentoo penguins are only found in Biscoe Island
""" print(penguins[(penguins["species"] == "Gentoo") & (penguins["island"] == "Biscoe")])
print(penguins[(penguins["species"] == "Gentoo") & (penguins["island"] == "Torgersen")])
print(penguins[(penguins["species"] == "Gentoo") & (penguins["island"] == "Dream")]) """

def _graph_adelie(adelie_with_long_flippers):
    """ Creates graphs for adelie penguins with long flippers - code is reused from calc_population_totals() and graph_populations()"""

    """ 
    #shorten to data for easy typing while testing
    data = adelie_with_long_flippers

    data.plot.bar(x)

    plt.show() """
    #is dataframe
    #print(type(adelie_with_long_flippers))

    totals = {"Torgersen":0, "Dream":0,"Biscoe":0}

    for i in adelie_with_long_flippers["island"]:
        if i in totals:
            totals[i] += 1
 
    catagories = []
    for k in totals:
        catagories.append(k)
    
    pops = []
    for k in pop_total:
        pops.append(pop_total[k])

    fig, ax = plt.subplots(figsize=(5,3),layout="constrained")

    ax.bar(catagories,pops)
    plt.show()
    pass

median_flipper_lengths = _calculate_median_flipper_lengths()
    #Isolate adelie penguins with long flippers, and save to a seperate dataframe
adelie_with_long_flippers = penguins[(penguins["species"] == "Adelie") & (penguins["flipper_length_mm"] > median_flipper_lengths["adelie_mean_flipper_length"])]

#sort and reindex
""" print(f"\n{adelie_with_long_flippers.head(5)}\n")
adelie_with_long_flippers = adelie_with_long_flippers.sort_values("flipper_length_mm")
print(f"{adelie_with_long_flippers.head(5)}\n")
#renumber indexes once sorted
adelie_with_long_flippers.set_index(pd.Series(range(0,len(adelie_with_long_flippers))), inplace=True)
print(f"{adelie_with_long_flippers.head(5)}\n")"""

#Graph adelies using bar chart
_graph_adelie(adelie_with_long_flippers)


#Question 2

#penguins.plot.scatter(x="bill_length_mm",y="bill_depth_mm") - no clear connection

#penguins.plot.scatter(x="bill_length_mm",y="flipper_length_mm") - THere might actually be a corrleation between bill and flipper lengh

#penguins.plot.scatter(x="flipper_length_mm",y="bill_depth_mm") - couple areas where both have similar values

#penguins.plot.scatter(x="body_mass_g",y="bill_depth_mm") - couple areas where correlation may exsist

#penguins.plot.scatter(x="bill_length_mm",y="body_mass_g") - clear trendline, heavier penguin == longer bill

#penguins[penguins["species"] == "Adelie"].plot.scatter(x="bill_length_mm",y="bill_depth_mm") - Adelie bill length vs depth

#penguins[penguins["species"] == "Gentoo"].plot.scatter(x="bill_length_mm",y="bill_depth_mm") GEntoo bill length vs depth - clear tendline

#penguins[penguins["species"] == "Chinstrap"].plot.scatter(x="bill_length_mm",y="bill_depth_mm") Chinstrap bill vs length depth - clear tendline

#penguins[penguins["sex"] == "male"].plot.scatter(x="bill_length_mm",y="bill_depth_mm")   - gender has no clear affect on correlation
#penguins[penguins["sex"] == "female"].plot.scatter(x="bill_length_mm",y="bill_depth_mm") - gender has no clear affect on correlation
#plt.show()