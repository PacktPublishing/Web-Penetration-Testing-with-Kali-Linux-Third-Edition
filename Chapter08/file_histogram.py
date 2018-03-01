import matplotlib.pyplot as plt
import sys
import base64

if (len(sys.argv))<2:
    print "Usage file_histogram.py <source_file> [1|0]"

print "Reading " + sys.argv[1] + "... "
s_file=open(sys.argv[1])

if sys.argv[2] == "1":
    text=base64.b64decode(s_file.read())
else:
    text=s_file.read()

chars=[0]*256
for line in text:
    for c in line:
        chars[ord(c)] = chars[ord(c)]+1

s_file.close()
p=plt.plot(chars)
plt.show()