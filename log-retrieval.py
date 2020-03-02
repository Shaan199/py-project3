#author Shaan P
#author Jannelle C (THANKS FOR THE HELP)

from urllib.request import urlretrieve
import os
import re
import collections 


#define varibles 
i=0
redirectCounter = 0
errorCounter = 0
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'http_access_log'


def file_len(LOCAL_FILE):
    with open (LOCAL_FILE) as f:
        for i, l in enumerate (f):
            pass
    return i + 1

#find all the files
def fileCount():
	filelog = []
	leastcommon = []
	with open(LOCAL_FILE) as logs:
		for line in logs:
			try:
				filelog.append(line[line.index("GET")+4:line.index("HTTP")])		
			except:
				pass
	counter = collections.Counter(filelog)
	for count in counter.most_common(1):														
		print("Most common file: {} with {} requests.".format(str(count[0]), str(count[1])))
	for count in counter.most_common():					
		if str(count[1]) == '1':
			leastcommon.append(count[0])
	if leastcommon:																						
		response = input("Display files requested only once? Y/N)".format(len(leastcommon)))
		if response == 'y' or response == 'Y':
			for file in leastcommon:
				print(file)

#retrieve files
if not os.path.isfile(LOCAL_FILE):
    urlretrieve(URL, LOCAL_FILE)

#define months
months_count ={
  "Jan": 0,
  "Feb": 0,
  "Mar": 0,
  "Apr": 0,
  "May": 0,
  "Jun": 0,
  "Jul": 0,
  "Aug": 0,
  "Sep": 0,
  "Oct": 0,
  "Nov": 0,
  "Dec": 0
}

#defien log files
janlogs=open("january.txt", "a+"); feblogs=open("february.txt", "a+"); marlogs=open("march.txt", "a+"); 
aprlogs=open("april.txt", "a+"); maylogs=open("may.txt", "a+"); junlogs=open("june.txt", "a+");
jullogs=open("july.txt", "a+"); auglogs=open("august.txt", "a+"); seplogs=open("september.txt", "a+")
octlogs=open("octlogs.txt", "a+"); novlogs=open("november.txt", "a+"); declogs=open("december.txt", "a+")   


# Adam's regix pattern 
pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'

lines = open(LOCAL_FILE, 'r').readlines()


for line in lines:
    match = re.match(pattern, line)

    if not match:
        continue

    match.group(0) 
    match.group(3) 
    timestamp = match.group(3)
    month = timestamp[3:6]
    months_count[month] += 1
    match.group(7) 
    
    if (match.group(7)[0] == "3"):
        redirectCounter += 1
    elif (match.group(7)[0] == "4"):
        errorCounter += 1
    if (month == "Jan"): 
        janlogs.write(line)
    elif (month == "Feb"): 
        feblogs.write(line)
    elif (month == "Mar"): 
        marlogs.write(line)
    elif (month == "Apr"): 
        aprlogs.write(line)
    elif (month == "May"): 
        maylogs.write(line)
    elif (month == "Jun"): 
        junlogs.write(line)
    elif (month == "Jul"): 
        jullogs.write(line)
    elif (month == "Aug"): 
        auglogs.write(line)
    elif (month == "Sep"): 
        seplogs.write(line)
    elif (month == "Oct"): 
        octlogs.write(line)
    elif (month == "Nov"): 
        novlogs.write(line)
    elif (month == "Dec"): 
        declogs.write(line)
    
    else:
        continue
print("Request Made")
print(file_len(LOCAL_FILE))
totalResponses = file_len(LOCAL_FILE)
print("Average number for month:", round(totalResponses/12,2))
print("Average number for week: ",round(totalResponses/52,2))
print("Average number for day: ", round(totalResponses/365,2))
print("Month Count:", months_count)
print("Total number of redirects:",redirectCounter)
print("Percentage of all requests that were redirects (3xx): {0:.2%}".format(redirectCounter/totalResponses))
print("Error count:",errorCounter)
print("Percentage of client error (4xx) requests: {0:.2%}".format(errorCounter/totalResponses))	
fileCount()
