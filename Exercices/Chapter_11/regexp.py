# import re

# name = input("Enter the file name :")
# if len(name) == 0 : name = 'actual_data.txt'
# elif name == '3' : name = 'sample_data.txt'
# h = open(name, 'r')
# s = 0

# for line in h :
#     line = line.rstrip()
#     if not re.search('[0-9]+', line) : continue
    
#     numbers = re.findall('[0-9]+', line)
#     for n in numbers :
#         s += int(n)
        
# print(s)

    
from distutils.filelist import findall
import re
print( sum( [ int(num) for num in re.findall('[0-9]+', open('actual_data.txt').read()) ] ) )