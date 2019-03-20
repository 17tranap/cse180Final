import sys

countsFileName = str(sys.argv[1])
statsFileName = str(sys.argv[2])
geneFileName = str(sys.argv[3])

geneIDs = {}
geneF = open(geneFileName, "r")
for line in geneF:
    tokens = line.strip().split()
    ucscID = tokens[0]
    gene = ""
    if len(tokens) > 1:
        gene = tokens[1]
    geneIDs[ucscID] = gene
geneF.close()

countsF = open(countsFileName, "r")
statsF = open(statsFileName, "r")

countsOut = open("RelevantGenesNormalizedCounts.tsv", "w")
header = countsF.readline()
countsOut.write(header)
for line in countsF:
    tokens = line.strip().split()
    ucscID = tokens[0]
    gene = geneIDs[ucscID]
    if gene == "":
        continue
    tokens[0] = gene
    outLine = ""
    for token in tokens:
        outLine += token + "\t"
    outLine = outLine[0:len(outLine)-1]
    countsOut.write(outLine + "\n")

statsOut = open("RelevantGenesStats.tsv", "w")
header = statsF.readline()
statsOut.write(header)
for line in statsF:
    tokens = line.strip().split()
    ucscID = tokens[0]
    gene = geneIDs[ucscID]
    if gene == "":
        continue
    tokens[0] = gene
    outLine = ""
    for token in tokens:
        outLine += token + "\t"
    outLine = outLine[0:len(outLine)-1]
    statsOut.write(outLine + "\n")

countsF.close()
countsOut.close()
statsF.close()
statsOut.close()
