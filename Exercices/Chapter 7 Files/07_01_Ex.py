fname = input("Enter a file name :")
fhand = open(fname, 'r')
sumup = 0
for line in fhand :
    if line.startswith("X-DSPAM-Confidence:") :
        value = line[line.find(':'):]
        sumup += float(value)