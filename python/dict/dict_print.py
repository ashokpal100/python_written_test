d = {
  'apples' : 'tasty',
  'bananas' : 'the best',
  'brussel sprouts' : 'evil',
  'cauliflower' : 'pretty good'
}


print d.keys()
print d.values()
for sKey in d:
  print "{0} are {1}".format(sKey,d[sKey])