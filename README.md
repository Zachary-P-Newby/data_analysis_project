# Overview

This is a personal Python project, the goal of which is to gain expirence in data analysis and visualization using the pandas and matplotlib libraries. Since data science is a large and profitable field programmers work in, it makes sense for an apsiring programmer such as myself to gain expirence in it to increase my skill set and open up new career opportunities.

The Dataset is the [Palmer Penguins Dataset](https://www.kaggle.com/datasets/ashkhagan/palmer-penguins-datasetalternative-iris-dataset/) from [Kaggle.com](https://www.kaggle.com), it was compiled from research on Adelie, Chinstrap, and Gentoo penguins by Dr. Kristen Gorman and the Palmer Station and uploaded to Kaggle by [Ashwani Rathee](https://www.kaggle.com/ashkhagan) for data visualization and exploration purposes as an alternative to the Iris dataset. It consists of the basic characteristics studied by Dr. Gorman, consisting of species, the island they were found on, bill length (mm), bill depth(mm), flipper length(mm), body mass (g), and sex.


The purpose of this program is to answer these two questions and visulaize the associated data:

1. On which of the three islands (Dream, Biscoe, and Torgenson) were adelie penguins with long flippers (greater than the average length of the species) most common?

2. Is there a relationship (correlation) between bill length and depth? If so, what kind of relationship is it? (ie. direct correlation or indirect). If not, do any factors correlate to either?


[Software Demo Video](https://youtu.be/-9kYLgY3Aqw)

# Data Analysis Results

The purpose of this program is to answer these two questions and visulaize the associated data:

1. On which of the three islands (Dream, Biscoe, and Torgenson) were adelie penguins with long flippers (greater than the average length of the species) most common?

2. Is there a relationship (correlation) between bill length and depth? If so, what kind of relationship is it? (ie. direct correlation or indirect). If not, do any factors correlate to either?

data_analysis_presentation.pdf answers these question and shows the processes and graphs I used to come up with them, and analysis_presentation.py contains all the code used to create the answers, but I will put them here.

1. Adelie penguins with long (greater than average length) flippers are found most often on Torgersen Island with 26 penguins, and least often on Biscoe.

2. Bill length and depth are positively correlated in gentoo and chinstrap penguins, with gentoos having two separate trend lines for each gender, while no direct correlation can be found for the Adelies. Each species has its own general range of bill length and depth. Flipper length appears to have direct, positive correlations between bill length and bill depth. While age is not recorded within the dataset, I suspect it has a correlation to bill length and depth as penguin bills grow with age.

# Development Environment

For my development enviorment I used Microsoft Vscode

This program was created in the python programming language, and uses the pandas and matplotllib libraries

# Useful Websites

* [Palmer Penguin Dataset](https://www.kaggle.com/datasets/ashkhagan/palmer-penguins-datasetalternative-iris-dataset/)
[Ashwani Rathee](https://www.kaggle.com/ashkhagan)
* [Kaggle.com](https://www.kaggle.com)
* [Data Science — Wikipedia ](https://en.wikipedia.org/wiki/Data_science)
* [pandas Overview - pandas Docs](https://pandas.pydata.org/docs/getting_started/overview.html)
* [data-titanic.csv source](https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv)
* [Air Quality Practice File Source](https://github.com/pandas-dev/pandas/blob/main/doc/data/air_quality_no2.csv)
* [List Comprehensions Review](https://www.w3schools.com/python/python_lists_comprehension.asp)
* [Matplotlib Pie chart tutorial](https://pythonguides.com/matplotlib-pie-chart/)
* [Stack Overflow - How Slicing in Python Works](https://stackoverflow.com/questions/509211/how-slicing-in-python-works)
* [Coolors](https://coolors.co)
* [Web Site Name](http://url.link.goes.here)

# Future Work

* I am happy with what I have created, but one thing I think could be imporved is the graphs for question 2. I don't if I ever will.

