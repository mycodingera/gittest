from re import X
import pandas as pd

#mydataset = {
    #'Cars' : ["BMW", "Volvo", "Ford"],
    #'Passing' : [3, 7, 2]
#}

calories = {"Day1": 340, "Day2": 550, "Day3": 372}

myvar = pd.Series(calories)

print(myvar)