import pickle

with open('pydata.pickle', 'wb') as pydatastore:
    pickle.dump([1, 12, 123, 'hello'], pydatastore)

with open('pydata.pickle', 'rb') as pydataload:
    savedlist = pickle.load(pydataload)

print(savedlist)