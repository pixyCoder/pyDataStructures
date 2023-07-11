Dict = { }
print("Initial empty hashmap : ")
print(Dict)
print()
 
Dict['Brentwood'] = {}
Dict['Downtown']  = {}
Dict['Torrance']  = {}
Dict['Irvine']    = {}
Dict['Burbank']   = {}
Dict['Pasadena']   = {}
print('After initializing nesting : ')
print(Dict)
print()
 
# Adding elements one at a time for Brentwood hashmap
Dict['Brentwood']['Torrance'] = 20
Dict['Brentwood']['Irvine']   = 62
Dict['Brentwood']['Downtown'] = 14
Dict['Brentwood']['Burbank']  = 16
Dict['Brentwood']['Pasadena'] = 34
print("\nAfter populating weights for nested hashmap Brentwood : ")
print(Dict)
print()
 
# Adding elements one at a time for Downtown
Dict['Downtown']['Torrance']  = 26
Dict['Downtown']['Irvine']    = 52
Dict['Downtown']['Burbank']   = 22
Dict['Downtown']['Pasadena']  = 12
Dict['Downtown']['Brentwood'] = 24
print("\nAfter populating weights for nested hashmap Downtown : ")
print(Dict)
print()
