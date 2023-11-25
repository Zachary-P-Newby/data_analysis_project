"""Final analysis file - contains all code used in final presentation to demonstrate I met the requirements """
import pandas as pd
import matplotlib.pyplot as plt

""" You must demonstrate the ability to do one or more of the following to achieve each answer:
filter, sort, aggregate (sum, average, count), or data conversion. """

#Set this to global since we will be using it in multiple functiosn and not modifying it.
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

def graph_populations(pop_total = calc_population_totals()):
    "Graphs populations of all islands and species, calls calc_population_totals for data if none is provided"

    catagories = []
    for k in pop_total:
        catagories.append(k)
    
    pops = []
    for k in pop_total:
        pops.append(pop_total[k])

    fig, ax = plt.subplots(figsize=(5,3),layout="constrained")

    ax.bar(catagories,pops)
    plt.show()

def answer_question_1():
    """
Generates answers for question 1: 
    1. On which of the three islands (Dream, Biscoe, and Torgenson) were adeliepenguins with long flippers
    (greater than the average length for the species most common?

For our purposes, a long flipper is above the average (mean) length for the species.

create 3 plots detailing the flipper length and number of adelie penguins with long flippers for each island"""


    #Sub functions__________________________________________________________
    def _calculate_median_flipper_lengths():
        """ Calculates the median flipper lengths of each species and saves them to a dictionary.
        These will be used for determinining if a penguin has a long flipper, for our purposes, a long flipper is above the average (mean) length for the species.
        All species average flipper lenghts are recorded for reference purposes."""
        median_flipper_lengths = dict()
        #Get medain flipper length of each species and save to dict
        median_flipper_lengths["adelie_mean_flipper_length"] = penguins[penguins["species"] == "Adelie"]["flipper_length_mm"].median()
        median_flipper_lengths["chinstrap_mean_flipper_length"] = penguins[penguins["species"] == "Chinstrap"]["flipper_length_mm"].median()
        median_flipper_lengths["gentoo_mean_flipper_length"] = penguins[penguins["species"] == "Gentoo"]["flipper_length_mm"].median()

        return median_flipper_lengths

    def _graph_adelies(adelie_with_long_flippers):
        
        



        plt.show()
        pass



    #Calculations and graphing_____________________________________________________________
    median_flipper_lengths = _calculate_median_flipper_lengths()
    #Isolate adelie penguins with long flippers, and save to a seperate dataframe
    adelie_with_long_flippers = penguins[(penguins["species"] == "Adelie") & (penguins["flipper_length_mm"] > median_flipper_lengths["adelie_mean_flipper_length"])]

    #for demonstrational purposes, the penguins are sorted by flipper length and the indexes are reset to match the ascending order of flipper lengths
    adelie_with_long_flippers = adelie_with_long_flippers.sort_values("flipper_length_mm")
    adelie_with_long_flippers.set_index(pd.Series(range(0,len(adelie_with_long_flippers))), inplace=True)

    _graph_adelies(adelie_with_long_flippers)
