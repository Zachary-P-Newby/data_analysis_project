"""Final analysis file - contains all code used in final presentation to demonstrate I met the requirements """
import pandas as pd
import matplotlib.pyplot as plt

""" You must demonstrate the ability to do one or more of the following to achieve each answer:
filter, sort, aggregate (sum, average, count), or data conversion. """

#Set this to global since we will be using it in multiple functions and not modifying it.
global penguins 
penguins = pd.read_csv("penguins.csv")

def calc_population_totals():
    """ Calculate total penguin populations and return a dict containing the total population of each island and species 
The result should be: {'Torgersen': 52, 'Dream': 124, 'Biscoe': 168, 'Adelie': 152, 'Chinstrap': 68, 'Gentoo': 124}
    """
    totals = {"Torgersen":0, "Dream":0,"Biscoe":0,"Adelie":0,"Chinstrap":0,"Gentoo":0}

    for i in penguins["island"]:
        totals[i] += 1

    for j in penguins["species"]:
        if j in totals:
            totals[j] += 1

    return totals

def graph_populations():
    "Graphs populations of all islands and species, calls calc_population_totals for data if none is provided"    
    pop_total = calc_population_totals()
    
    pops = []
    for k in pop_total:
        pops.append(pop_total[k])
    
    catagories = []
    for i in pop_total:
        catagories.append(i)

    fig, ax = plt.subplots(2,figsize=(5,5),layout="constrained")

    #total island populations
    island_pops = ax[0].bar(catagories[0:3],pops[0:3],color="#59a5d8")
    ax[0].bar_label(island_pops,label_type="center")
    ax[0].set_title("Total Island Populations:")

    species_pops = ax[1].bar(catagories[3::],pops[3::],color="#cf5c36")
    ax[1].bar_label(species_pops,label_type="center")
    ax[1].set_title("Total Species Populations:")
    
    plt.show()

def answer_question_1():
    """
Generates answers for question 1: 
    1. On which of the three islands (Dream, Biscoe, and Torgenson) were adelie penguins with long flippers
    (greater than the average length of the species) most common?

For our purposes, a long flipper is above the average (median) length for the species.

create 3 plots detailing the flipper length and number of adelie penguins with long flippers for each island"""


    #Sub functions__________________________________________________________
    def _calculate_median_flipper_lengths():
        """ Calculates the median flipper lengths of each species and saves them to a dictionary.
        These will be used for determining if a penguin has a long flipper, for our purposes, a long flipper is above the average (median) length for the species.
        All species average flipper lengths are recorded for reference purposes."""
        median_flipper_lengths = dict()
        #Get median flipper length of each species and save to dict
        median_flipper_lengths["adelie_median_flipper_length"] = penguins[penguins["species"] == "Adelie"]["flipper_length_mm"].median()
        median_flipper_lengths["chinstrap_median_flipper_length"] = penguins[penguins["species"] == "Chinstrap"]["flipper_length_mm"].median()
        median_flipper_lengths["gentoo_median_flipper_length"] = penguins[penguins["species"] == "Gentoo"]["flipper_length_mm"].median()

        return median_flipper_lengths

    def _graph_long_flipper_adelies_pops(adelie_with_long_flippers):
        """ Counts up the number of adelie penguins with long flippers for each island and
        displays them in a bar chart, code from calc_population_totals() and graph_populations()
        is reused"""
        
        #graph island totals
        totals = {"Torgersen":0, "Dream":0,"Biscoe":0}

        for i in adelie_with_long_flippers["island"]:
            totals[i] += 1

        pops = []
        for k in totals:
            pops.append(totals[k])

        fig, ax = plt.subplots(figsize=(5,3),layout="constrained",)

        graph = ax.bar(totals.keys(),pops,color=["#efc88b","#59a5d8","#cf5c36"])
        ax.bar_label(graph,label_type="center")
        ax.set_title("Number of Adelie penguins with long flippers per island:")
        plt.show()
        pass
    
    def _graph_adelies_per_island():
        """ Creates graphs displaying the flipper lengths for adelie penguins on each island """
        #Isolate Adelie penguins
        adelies = penguins[penguins["species"] == "Adelie"]

        #create graph with 3 scatterplots
        fig, ax = plt.subplots(3, figsize=(8,5),layout="constrained")

        ax[0].scatter(adelies[adelies["island"] == "Dream"]["flipper_length_mm"],range(len(adelies[adelies["island"] == "Dream"])),color="#59a5d8")
        ax[1].scatter(adelies[adelies["island"] == "Biscoe"]["flipper_length_mm"],range(len(adelies[adelies["island"] == "Biscoe"])),color="#efc88b")
        ax[2].scatter(adelies[adelies["island"] == "Torgersen"]["flipper_length_mm"],range(len(adelies[adelies["island"] == "Torgersen"])),color="#59a5d8")

        ax[0].set_ylabel("Penguin ID")
        ax[0].set_xlabel("Flipper Length (mm)")
        ax[1].set_ylabel("Penguin ID")
        ax[1].set_xlabel("Flipper Length (mm)")
        ax[2].set_ylabel("Penguin ID")
        ax[2].set_xlabel("Flipper Length (mm)")

        ax[0].set_title("Dream Island Adelie Flipper Lengths")
        ax[1].set_title("Biscoe Island Adelie Flipper Lengths")
        ax[2].set_title("Torgersen Island Flipper Lengths")
        #Mark average flipper length on graph
        ax[0].axvline(x=190,alpha=.5,color="r")
        ax[1].axvline(x=190,alpha=.5,color="r")
        ax[2].axvline(x=190,alpha=.5,color="r")

        plt.show()
    
    #Calculations and graphing_____________________________________________________________
    median_flipper_lengths = _calculate_median_flipper_lengths()
    #Isolate adelie penguins with long flippers, and save to a seperate dataframe
    adelie_with_long_flippers = penguins[(penguins["species"] == "Adelie") & (penguins["flipper_length_mm"] > median_flipper_lengths["adelie_median_flipper_length"])]

    #for demonstrational purposes, the penguins are sorted by flipper length and the indexes are reset to match the ascending order of flipper lengths
    adelie_with_long_flippers = adelie_with_long_flippers.sort_values("flipper_length_mm")
    adelie_with_long_flippers.set_index(pd.Series(range(0,len(adelie_with_long_flippers))), inplace=True)

    _graph_long_flipper_adelies_pops(adelie_with_long_flippers)
    _graph_adelies_per_island()
    
    """ Conclusion Adelie penguins with long (greater than average length) flippers are found most often on Torgersen Island with 26 penguins, and least often on Biscoe. """
    pass


def answer_question_2():
    """ Answers Question 2: ?Is there a relationship (correlation) between bill length and depth? If so, what kind of relationship is it? (ie. direct correlation or indirect).
    If not, do any factors correlate to either"""
    
    #re-use _calculate_median_flipper_lengths from question one to get the median bill length and depths for each species
    def _calculate_median_bill_lengths_lengths():
        """ Calculates the median flipper lengths of each species and saves them to a dictionary.
        These will be used for determinining if a penguin has a long flipper, for our purposes, a long flipper is above the average (median) length for the species.
        All species average flipper lenghts are recorded for reference purposes."""
        median_flipper_lengths = dict()
        #Get medain flipper length of each species and save to dict
        median_flipper_lengths["adelie_median_flipper_length"] = penguins[penguins["species"] == "Adelie"]["bill_length_mm"].median()
        median_flipper_lengths["chinstrap_median_flipper_length"] = penguins[penguins["species"] == "Chinstrap"]["bill_length_mm"].median()
        median_flipper_lengths["gentoo_median_flipper_length"] = penguins[penguins["species"] == "Gentoo"]["bill_length_mm"].median()

        return median_flipper_lengths

    def _calculate_median_flipper_lengths():
        """ Calculates the median flipper lengths of each species and saves them to a dictionary.
        These will be used for determinining if a penguin has a long flipper, for our purposes, a long flipper is above the average (median) length for the species.
        All species average flipper lenghts are recorded for reference purposes."""
        median_flipper_lengths = dict()
        #Get medain flipper length of each species and save to dict
        median_flipper_lengths["adelie_median_flipper_length"] = penguins[penguins["species"] == "Adelie"]["flipper_length_mm"].median()
        median_flipper_lengths["chinstrap_median_flipper_length"] = penguins[penguins["species"] == "Chinstrap"]["flipper_length_mm"].median()
        median_flipper_lengths["gentoo_median_flipper_length"] = penguins[penguins["species"] == "Gentoo"]["flipper_length_mm"].median()

        return median_flipper_lengths




    #scatterplot of all penguins comparing bill length to depth
    penguins.plot.scatter(x="bill_length_mm",y="bill_depth_mm",title="Penguin Bill Lengths and Depths")
    
    """ While the the bill length do not appear to have either a positive or negative correlation to eachother, as their is no clear trendline. However, one can see three clusters of similar bill length and depths,
    representing the three species in the dataset. Let's try isolating each species to view it in greater detail"""
    
    #scatterplot of all adelie penguins comparing bill length to depth
    penguins[penguins["species"] == "Adelie"].plot.scatter(x="bill_length_mm",y="bill_depth_mm",title="Adelie Penguin Bill Lengths and Depths")
    
    """ Adelie bills are usually between 16.5 and 19.5 mm deep and between 35 and 42 mm long. There does not appear to be a correlation or trendline with the adelie penguins, just a general range."""
    
    #scatterplot of all gentoo penguins comparing bill length to depth
    penguins[penguins["species"] == "Gentoo"].plot.scatter(x="bill_length_mm",y="bill_depth_mm",title="Gentoo Penguin Bill Lengths and Depths")
    
    """ In Gentoos however, one can see a clear trendline, the longer the bill, the deeper it is. Most bills are between 42 and 51 mm long and between 13.5 and 16.5 mm deep, with a postive correlation between the two.
    It almost looks as if there are two trendlines. If we graph male and female gentoos seperately,  we can see both genders have their own trendlines, with the males being slightly deeper (hihger on the y-axis which is bill depth)
    than the females"""
    penguins[(penguins["species"] == "Gentoo") & (penguins["sex"] == "male")].plot.scatter(x="bill_length_mm",y="bill_depth_mm",title="Male Gentoo Penguin Bill Lengths and Depths")
    penguins[(penguins["species"] == "Gentoo") & (penguins["sex"] == "female")].plot.scatter(x="bill_length_mm",y="bill_depth_mm",title="Female Gentoo Penguin Bill Lengths and Depths")
    
    
    #scatterplot of all Chinstrap penguins comparing bill length to depth
    penguins[penguins["species"] == "Chinstrap"].plot.scatter(x="bill_length_mm",y="bill_depth_mm",title="Chinstrap Penguin Bill Lengths and Depths")
    
    """ Chinstraps have their own trendline, with most bills being between 45 and 52 mm long, and 17 and 20 mm deep. There does not appear to be two seperalte trendlines between sexes though. This may be a result of the chinstraps having a smaller population """

    #Look for correlation between bill and flipper length and between bill depth and flipper length 
    penguins.plot.scatter(x="bill_length_mm",y="flipper_length_mm",title="Bill Length compared to Flipper Length")
    penguins.plot.scatter(x="bill_depth_mm",y="flipper_length_mm",title="Bill Depth compared to Flipper Length")
    """ While I will not go into further detail (as bill length and depth are correlated), bill length and depth to both seem to be correlated to flipper length, and exhibit the clumping behavior as seen in the all penguins length and depth graph,
    This gives evidence for other penguin characterisitics having a correlations between bill length and depth."""

    """ Conclusion: Bill length and deep are postively correlated in gentoo and chinstrap penguins, with gentoos having two seperate trendlines for each gender,
    while no direct correlation can be found for the adelies. Each species has its own general range of bill length and depth.
    Flipper length appears to have direct, positive correlatioins between bill length and bill depth.
    While age is not recorded within the dataset, it likely has a correlation to bill length and depth as penguin bills grow with age."""

    plt.show()
    pass

print(penguins)

graph_populations()

answer_question_1()

answer_question_2()