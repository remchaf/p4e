fname = input("Enter a file name :")
fhand = open(fname, 'r')
sumup = 0
count = 0
for line in fhand :
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        value = line[line.find(':') + 1:]
        sumup += float(value)
        count += 1
        
print(sumup / count)