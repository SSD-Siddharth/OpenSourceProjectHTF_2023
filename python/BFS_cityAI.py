# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:05:18 2022

@author: SSD
"""



from queue import Queue as Q
# Function to implement BFS
def findCheapestPrice(cities, flights, src, dst, stops,Detail_Fl):
	adjList=dict()

	# Traverse flight[][]
	for flight in flights :

		# Create Adjacency Matrix
		if flight[0] in adjList:
			adjList[flight[0]].append(
				(flight[1], flight[2]))
		else:
			adjList[flight[0]]=[(flight[1], flight[2])]
	
	q=Q()
	q.put((src, 0))

	# Store the Result
	srcDist = 1e9
	# Traversing the Matrix
	while (not q.empty() and stops >= 0) :
		stops-=1

		for i in range(q.qsize()) :
			curr = q.get()

			for nxt in adjList[curr[0]]:

				# If source distance is already
				# least the skip this iteration
				if (srcDist < curr[1] + nxt[1]):
					continue

				q.put((nxt[0],curr[1] + nxt[1]))

				if (dst == nxt[0]):
					if(srcDist>(curr[1] + nxt[1])):
						print("Cities considered: ",Detail_Fl[nxt[0]], " ➡️ ",Detail_Fl[curr[0]], ", Previous distance: ",srcDist,", Min Dis: ",nxt[1]+curr[1])
						#print(nxt,", "", ",srcDist,curr, nxt)
					srcDist = min( srcDist, curr[1] + nxt[1])
				
	# Returning the Answer
	return -1 if srcDist == 1e9 else srcDist


# Driver Code
	
#__main__
# Destination, Cost
flights = [
	       [0, 1, 138],
	       [0,2,1172],
	       [0,3,379],
	       [0,4,2256],
	       [0,5,321],
           [0,6,1649],
		   [0,7,2106],
		   [1,2,1529],
	       [1,3,523],
	       [1,4,2168],
	       [1,5,212],
           [2,1,1468],
	       [2,3,1148],
	       [2,4,749],
	       [2,5,1459],
	       [3,4,1751],
	       [3,5,656],
	       [4,5,2136],
           [4,7,1149],
           [5,6,1552],
           [6,0,1649],
           [6,2,674],
           [6,4,491],
           [7,3,1402],
           [7,4,1501],
		   [7,2,1172]
	       ]
#Available Cities
Dict={0:"Chennai",1:"Vellore",2:"Bhopal",3:"Amaravati",4:"Delhi",5:"Bangalore",6:"Jodhpur",7:"Siliguri"}
count=0
temp=0
Dict1={}
for i in Dict:
	Dict1[count]=Dict[i].lower()
	print(Dict[i],end=",  ")
	count+=1
print("\nTotal number of available Stations:",count,"\n")

src=input("Enter source city:")
dest=input("Enter your Destination City:")

check1=src.lower() in (Dict1.values())
if(check1==False):
	print("!!! Source city not found/Not Availabe, Kinly re-enter the Source again !!!")
	src=input("Enter source city:")
check2=dest.lower() in (Dict1.values())
if(check2==False):
	print("!!! Destination city not found/Not Availabe, Kinly re-enter the Destination again !!!")
	dest=input("Enter your Destination City:")
stp=int(input("Enter total Number of stops:"))	
if src.lower()=="new delhi": 
    src="Delhi"
if dest.lower()=="new delhi":
    dest="Delhi"
for i in Dict:
    if (Dict[i].lower()==src.lower()):
        src_c=i
    if (Dict[i].lower()==dest.lower()):
        des_c=i



		
# vec, n, stops, src, dst
totalCities = count
#sourceCity = 0
#destCity = 2
ln=len(flights)
#Adding both side directions in the Graph
for i in range(ln):
    a=flights[i][0]
    b=flights[i][1]
    l=[b,a,flights[i][2]]
    flights.append(l)

ans = findCheapestPrice(
	totalCities, flights,
	src_c, des_c,
	stp,Dict)
if (ans==0):
	print("\n!*! Source and Destiantion entered are same, Kindly try again !*!")
elif (ans==-1):
    print("\n!!!Sorry, Route by \U0001F686/ \U00002708  Not availabe, due to Covid travel restrictions, Try again!!!")
else:
	print("\n\nMinimum/Best distance From:",Dict[src_c],", To:",Dict[des_c]," with atmost",stp,"stop(s), according to Latest COVID protocols by \U0001F686/\U00002708= ",ans,"km")
