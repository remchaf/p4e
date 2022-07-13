# def Abi():
#  while True:
#    value = input(">>")
#    if value == "done":
#      break
#    print(value)
#  return "jtm Abi !"

# Abi()



counts = { 'a': 10, 'b': 1, 'c': 20 }
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)
