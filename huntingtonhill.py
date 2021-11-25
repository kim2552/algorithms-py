import numpy as np
import copy
import operator
import random as rnd

#Inputs
Pop = {
    'Texas':28304596,
    'Florida':20984400,
    'NewYork':19849399,
    'Pennsylvania':12805537,
    'Illinois':12802023,
    'Ohio':11658609,
    'Georgia':10429379,
    'NorthCarolina':10273419,
    'Michigan':9962311,
    'NewJersey':9005644,
    'Virginia':8470020,
    'Washington':7405743,
    'Arizona':7016270,
    'Massachusetts':6859819,
    'Tennessee':6715984,
    'Indiana':6666818,
    'Missouri':6113532,
    'Maryland':6052177,
    'Wisconsin':5795483,
    'Colorado':5607154,
    'Minnesota':5576606,
    'SouthCarolina':5024369,
    'Alabama':4874747,
    'Louisiana':4684333,
    'Kentucky':4454189,
    'Oregon':4142776,
    'Oklahoma':3930864,
    'Connecticut':3588184,
    'Iowa':3145711,
    'Utah':3101833,
    'Arkansas':3004279,
    'Nevada':2998039,
    'Mississippi':2984100,
    'Kansas':2913123,
    'NewMexico':2088070,
    'Nebraska':1920076,
    'WestVirginia':1815857,
    'Idaho':1716943,
    'Hawaii':1427538,
    'NewHampshire':1342795,
    'Maine':1335907,
    'RhodeIsland':1059639,
    'Montana':1050493,
    'Delaware':961939,
    'SouthDakota':869666,
    'NorthDakota':755393,
    'Alaska':739795,
    'Vermont':623657,
    'Wyoming':579315
}
Reps = {
    'Texas':0,
    'Florida':0,
    'NewYork':0,
    'Pennsylvania':0,
    'Illinois':0,
    'Ohio':0,
    'Georgia':0,
    'NorthCarolina':0,
    'Michigan':0,
    'NewJersey':0,
    'Virginia':0,
    'Washington':0,
    'Arizona':0,
    'Massachusetts':0,
    'Tennessee':0,
    'Indiana':0,
    'Missouri':0,
    'Maryland':0,
    'Wisconsin':0,
    'Colorado':0,
    'Minnesota':0,
    'SouthCarolina':0,
    'Alabama':0,
    'Louisiana':0,
    'Kentucky':0,
    'Oregon':0,
    'Oklahoma':0,
    'Connecticut':0,
    'Iowa':0,
    'Utah':0,
    'Arkansas':0,
    'Nevada':0,
    'Mississippi':0,
    'Kansas':0,
    'NewMexico':0,
    'Nebraska':0,
    'WestVirginia':0,
    'Idaho':0,
    'Hawaii':0,
    'NewHampshire':0,
    'Maine':0,
    'RhodeIsland':0,
    'Montana':0,
    'Delaware':0,
    'SouthDakota':0,
    'NorthDakota':0,
    'Alaska':0,
    'Vermont':0,
    'Wyoming':0
}
R = 435     # Number of current representatives
n = 50      # Number of states
PQ = copy.deepcopy(Reps)

i = 0
for key in Reps:
    Reps[key] = 1
    PQ[key] = float(Pop[key])/np.sqrt(2)
    i+=1

j = 0
for j in range(1,np.abs(i-R)+1):
    hp = max(PQ.items(), key=operator.itemgetter(1))[0]
    Reps[hp] += 1
    PQ[hp] = Pop[hp]/np.sqrt(Reps.get(hp)*(Reps.get(hp)+1))

total=0
for key in Reps:
    total += Reps.get(key)
print(Reps)
print("Total num reps=",total)
