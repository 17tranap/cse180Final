import sys

statsFileName = str(sys.argv[1])
statsF = open(statsFileName, "r")

statsOut = open("SignificantGenes.tabular", "w")
header = statsF.readline()
statsOut.write(header)
for line in statsF:
    tokens = line.strip().split()
    pval = float(tokens[5])
    if pval < 0.05:
        statsOut.write(line)

