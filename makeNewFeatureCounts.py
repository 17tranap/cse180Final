import sys

countsFileName = str(sys.argv[1])
statsFileName = str(sys.argv[2]) #for this portion should only have nontrivial genes of p-value < 0.5
countsF = open(countsFileName, "r") #should already have trivial genes removed
statsF = open(statsFileName, "r")

sigGenesList = [] #build list of significant genes from stats so only those included in output counts
header = statsF.readline()
for line in statsF:
    tokens = line.strip().split()
    gene = tokens[0]
    sigGenesList.append(gene)


#loops through rows of counts and only add gene row if gene was significant in stats
countsOut = open("SignificantCounts.tsv", "w")
header = countsF.readline()
countsOut.write(header)
for line in countsF:
    tokens = line.strip().split()
    gene = tokens[0]
    if gene in sigGenesList:
        countsOut.write(line)

countsF.close()
statsF.close()
countsOut.close()
