import sys
import re

sqlStartStr = "exec sp_executesql N'"
sqlEndStr = "',N'"
argTypesStartStr = "',N'"
argTypesEndStr = "',"

def extractText(beginStr, endStr, text):
	startIndex = text.index(beginStr) + len(beginStr)
	endIndex = -1
	if(endStr):
		endIndex = text.index(endStr, startIndex + 1)
	return text[startIndex:endIndex]

inputStr = ""
with open(sys.argv[1], "r") as inputfile:
    inputStr = inputfile.read()

sql = extractText(sqlStartStr, sqlEndStr, inputStr)
argTypes = extractText(argTypesStartStr, argTypesEndStr, inputStr)
argsText = extractText(argTypes + argTypesEndStr, None, inputStr)

matches = re.findall('@P[\d]+', sql)
args = argsText.split(",")

for i in range(0, len(matches)):
	sql = sql.replace(matches[i], args[i], 1)

print sql