import numpy as np
import pandas as pd

lab = ['a', 'b', 'c', 'd']
my_list = [1, 2, 3, 4]
arr = np.array([1 , 2, 3, 4])
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#Creating a Series from list, numpy array and dictionary:-
print(pd.Series(my_list))
#It will take index of the list as default index:-
print(pd.Series(arr, index=lab))
#It will take the key of the dictionary as default index:-
print(pd.Series(d))