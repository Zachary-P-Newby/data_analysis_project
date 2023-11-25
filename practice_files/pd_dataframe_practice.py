import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

 
titanic = pd.read_csv("practice_files//data_titanic.csv")
air_quality = pd.read_csv("practice_files//air_quality_no2.csv", index_col=0, parse_dates=True)
penguins = pd.read_csv("penguins.csv")

#Sorting Practice
""" df = pd.DataFrame(
    data = {
        #"one":pd.Series([np.random.randint(27),np.random.randint(27),np.random.randint(27),np.random.randint(27),np.random.randint(27)],index=["a","b","c","d","e"]),
        "four":pd.Series([8,10,6,4,12],index=["a","b","c","d","e"]),
        "one":pd.Series([1,2,3,4,5],index=["a","b","c","d","e"]),
        "five":pd.Series([7,5,1,9,32],index=["a","b","c","d","e"]),
        "two":pd.Series([9,4,7,2,23],index=["a","b","c","d","e"]),
        "three":pd.Series([23,8,7,13,26],index=["a","b","c","d","e"])
    }) """

# .sort_values sorts whatever coulmn or index you put into 'by' in ascending order - ie. coulumn one, and sorts all the other coulumns to match indexes
#print(df.sort_values(by=["four"]))

#sort_index sorts by the indexes or coulumns

#print(df.sort_index(axis=1)) - puts strings into alphebetical order



""" df = pd.DataFrame(
    data = {
        #"one":pd.Series([np.random.randint(27),np.random.randint(27),np.random.randint(27),np.random.randint(27),np.random.randint(27)],index=["a","b","c","d","e"]),
        1:pd.Series([8,10,6,4,12],index=["a","b","c","d","e"]),
        5:pd.Series([1,2,3,4,5],index=["a","b","c","d","e"]),
        4:pd.Series([7,5,1,9,32],index=["a","b","c","d","e"]),
        3:pd.Series([9,4,7,2,23],index=["a","b","c","d","e"]),
        2:pd.Series([23,8,7,13,26],index=["a","b","c","d","e"])
    })  """



#print(df.sort_index(axis=1)) - puts numbers in ascending or descending order

""" df = pd.DataFrame(
    data = {
        #"one":pd.Series([np.random.randint(27),np.random.randint(27),np.random.randint(27),np.random.randint(27),np.random.randint(27)],index=["a","b","c","d","e"]),
        1:pd.Series([8,10,6,4,12],index=["5","4","3","2","1"]),
        5:pd.Series([1,2,3,4,5],index=["c","e","a","b","d"]),
        4:pd.Series([7,5,1,9,32],index=["n","m","l","o","p"]),
        3:pd.Series([9,4,7,2,23],index=["10","14","8","32","26"]),
        2:pd.Series([23,8,7,13,26],index=["sex","age","body_mass","hair_color","eye_color"])
    }) 
 """

#indexes must all be of the same type
#print(df)
#print(df.sort_index()) - puts Nan for values that do not exsist

df = pd.DataFrame(
    data = {
        #"one":pd.Series([np.random.randint(27),np.random.randint(27),np.random.randint(27),np.random.randint(27),np.random.randint(27)],index=["a","b","c","d","e"]),
        1:pd.Series([1,2,3,4,5],index=[5,4,3,2,1]),
        5:pd.Series([1,2,3,4,5],index=[4,5,1,3,2]),
        4:pd.Series([1,2,3,4,5],index=[1,6,2,5,4]),
        3:pd.Series([1,2,3,4,5],index=[1,2,4,3,5]),
        2:pd.Series([1,2,3,4,5],index=[6,4,3,1,2])
    }) 
print(df)
print(df.sort_index())
#4:pd.Series([7,5,1,9,32],index=[1,3,2,2,4]), - no duplicate lablels

""" I guess could I could sort the filtered resultss """





#dataframe.filter practice
"""frame = pd.DataFrame((["Nibbs","Splash","Fluffy","Sparky"],["Muffin","Trip","Lucky","Alphie"],[4,8,5,2],[6,11,23,4],["Z","a","c","h"]), columns=["Oshawott","Dewott","Mimikyu","Pawmi"])

#print(frame.filter(like="wott",axis=1))
#print(frame.filter(like="mi",axis=1))
#print(frame.filter(items=[2,4],axis=0))
 print(frame.filter(items=["Mimikyu"],axis=1)) 
print(frame)"""


""" print(titanic.filter(items=["Name","Age","SibSp"]).head())

#dataframe.loc pracatice
print(titanic.loc["Ticket"].head()) """

""" titanic """

""" print([method_name for method_name in dir(air_quality.plot) if not method_name.startswith("_")])
#air_quality.plot.hexbin(x="station_london",y="station_paris" ,subplots=True)

plt.show() """

#penguin_expiriments
#___________________________________________________________________
#penguins.plot.scatter(x="bill_length_mm",y="bill_depth_mm", alpha = 0.5)

#plot body weight - penguins["body_mass_g"].plot()

#filter pracice

#dream = penguins[penguins["island"] == "Dream"]

#filtered_pen = penguins[(penguins["island"] == "Dream") & (penguins["species"] == "Gentoo")]
#Turns out there are none

#There are 152 penguins with bills >= 200 mm
""" count = 0
filtered_pen =penguins[penguins["flipper_length_mm"] >=200]
for i in filtered_pen["species"]:
    count += 1

print(f"Count: {count}") """

""" filter_pen = penguins[(penguins["species"] == "Adelie") & (penguins["island"] == "Torgersen")]
filter_pen.plot.bar(y="body_mass_g")
filter_pen.plot.line(y="body_mass_g")
filter_pen.plot.hist(by="body_mass_g") """

""" Penguins recorded on each island
t_count = 0
b_count = 0
d_count = 0

for i in penguins["island"]:
    if i == "Torgersen":
        t_count +=1
    elif i == "Biscoe":
        b_count +=1
    elif i== "Dream":
        d_count +=1
    else:
        pass

plt.pie(x=[t_count,b_count,d_count],labels=[f"Torgersen: {t_count}",f"Biscoe: {b_count}",f"Dream: {d_count}"])

plt.title("Penguins by Island") """

""" #Penguins per species count
a_count = 0
c_count = 0
g_count = 0
for i in penguins["species"]:
    if i == "Adelie":
        a_count +=1
    elif i == "Chinstrap":
        c_count +=1
    elif i== "Gentoo":
        g_count +=1
    else:
        pass
plt.pie(x=[a_count,c_count,g_count],labels=[f"Adelie: {a_count}",f"Chinstrap: {c_count}",f"Gentoo: {g_count}"], colors=["#F45B69","#613F75","#114B5F"])
plt.title("Penguins of each species recorded", loc="left", color="#6D6A75") """

#plt.pie(titanic["Pclass"])

""" count1 = 0
count2 = 0
count3 = 0
for i in titanic["Pclass"]:
    if i == 1:
        count1 +=1
    elif i == 2:
        count2 +=1
    elif i== 3:
        count3 +=1
    else:
        pass

plt.pie(x=[count1,count2,count3],labels=[f"First Class: {count1}",f"Second Class: {count2}",f"Third Class: {count3}"], colors=["r","y","b"])

plt.title("Titanic Passenger class counts: ")
plt.show() """

