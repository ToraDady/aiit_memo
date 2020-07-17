
import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1], "r")
    print("here")
else:
    f = sys.stdin


s = f.read()
words = s.split()
# n  = len(words)

freqs = {}

for w in words:
    if w in freqs:
        freqs[w] += 1
    else:
        freqs[w] = 1

sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

# print(sorted_freqs, file=sys.stdout, end='')
i=0
for (k, v) in sorted_freqs:
    if i == 20: 
        break
    print(" {}: {}".format(k, v))
    i += 1

