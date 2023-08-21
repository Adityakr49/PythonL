# dictionary = A changeable,unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals={'USA':'Washington DC',
          'India':'New Delhi',
          'China':'Beijing',
          'Russia':'Moscow'}
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')


# print(capitals['Germany']) #Gives Error
print(capitals.get('Germany')) #More safer way to check if pair exist
print(capitals.keys())
print(capitals.values())
print(capitals.items())
for key,value in capitals.items():
    print(key,value)
capitals.clear()