# using get()  for bypass error mesasge 
# when you call a value which doest exist , then you counter error , to solve this problem use get()  function 
alian_0 = {'color': 'blue', 'point':  5}
# print(alian_0['band'])
# File "c:\Users\Rishu\Documents\oneshot mosh\17.5_using_get_to_access_values.py", line 4, in <module>
#     print(alian_0['band'])
#           ~~~~~~~^^^^^^^^
# KeyError: 'band'



# get mehtod is use for bypass error counter in pythn

point_value = alian_0.get('band', 'no band found in dic')
print(point_value)