# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:05:00 2022

@author: SSD
"""

# DFS 
RouteMatrix=[]
FormedCityMap=dict()

# Function to iFormedCityMaplement DFS Traversal
def DFSUtility(node, stops, dst, cities,flight_det):
	# Base Case
	if (node == dst):
		#print(dst)
		return 0
	if (stops < 0) :
		return 1e9
	key=(node, stops)

	# Find value with key in a map
	if key in FormedCityMap:
		return FormedCityMap[key]
	ans = 1e9       #Assuming there are no routes initially
    
	# Traverse adjacency matrix of
	# source node
	for neighbour in range(cities):
		weight = RouteMatrix[node][neighbour]

		if (weight > 0) :

			# Recursive DFS call for
			# child node
			minVal = DFSUtility(neighbour, stops - 1, dst, cities,flight_det)
			if (minVal + weight > 0):
				#print(neighbour, RouteMatrix[node][neighbour], RouteMatrix[node])
				if(ans>(minVal + weight)):
					print("Cities considered: ",flight_det[node], " ➡️ ",flight_det[neighbour], "Distance: ",RouteMatrix[node][neighbour],", Min",minVal)
				ans = min(ans, minVal + weight)
				
	#print(RouteMatrix)
	FormedCityMap[key] = ans
	# Return ans

	return ans

# Function to find the cheapest price
# from given source to destination
def findCheapestPrice(cities, flights, src, dst, stops,Flight_Det):
	global RouteMatrix
	# Resize Adjacency Matrix
	RouteMatrix=[[0]*(cities + 1) for _ in range(cities + 1)]

	# Traverse flight[][]
	for item in flights:
		# Create Adjacency Matrix
		RouteMatrix[item[0]][item[1]] = item[2]
	

	# DFS Call to find shortest path
	ans = DFSUtility(src, stops, dst, cities,Flight_Det)   
	# Return the cost
	return -1 if ans >= 1e9 else int(ans)
      

#__main__
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
	print("\nMinimum/Best distance From:",Dict[src_c],", To:",Dict[des_c]," with atmost",stp,"stop(s), according to Latest COVID protocols by \U0001F686/\U00002708= ",ans,"km")
