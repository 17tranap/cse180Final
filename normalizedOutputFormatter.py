import sys
def shouldWrite(line):
    if line[0:5] == "MSTRG":
        return False
    if "NA" in line:
        return False
    tokens = line.split()
    if tokens[1] == "0"  and tokens[2] == "0" and tokens[3] == "0" and tokens[4] == "0" and tokens[5] == "0" and tokens[6] == "0":
        return False
    return True

    
countsFileName = str(sys.argv[1])
statsFileName = str(sys.argv[2])
countsF = open(countsFileName, "r")
statsF = open(statsFileName, "r")

countsOut = open("RelevantNormalizedCountsDeseq.tabular", "w")
header = countsF.readline()
countsOut.write(header)
for line in countsF:
    if shouldWrite(line):
        countsOut.write(line)


statsOut = open("RelevantDESEQpvalueslog.tabular", "w")
header = "geneID\tBase mean\tlog2(FC)\tStdErr\tWald-Stats\tP-value\tP-adj\n"
statsOut.write(header)
for line in statsF:
    if shouldWrite(line):
        statsOut.write(line)

countsOut.close()
statsOut.close()
