boxTypes = [[5,10],[2,5],[4,7],[3,9]]
array = sorted(boxTypes, key = lambda x : x[1], reverse=True)
print(array)