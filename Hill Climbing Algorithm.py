#Heuristic Value is Iniatialize as per the below:

heuristicValue = {
    "A" : 40,
    "B" : 32,
    "C" : 25,
    "D" : 35,
    "E" : 19,
    "F" : 17,
    "G" : 0,
    "H" : 10,
}
#Graph is Iniatialize as per the below:

graph = { 
   'A' : [['B', 11],
          ['C', 14],
          ['D', 7]],
   'B' : [['A', 11], 
          ['E', 15]],
   'C' : [['A', 14],
          ['E', 8],
          ['F', 10]],
   'D' : [['A', 7],
          ['F', 25]],
   'E' : [['B', 15],
          ['C', 8],
          ['H', 9]],
   'F' : [['C', 10],
          ['G', 20]],
   'G' : [['F', 20],
          ['H', 10]],
   'H' : [['E', 9],
          ['G', 10]]
}
#Implementation part of Hill climbing algorithm

def hill_climbing(startState, goalState):
  pathList = []

  pathList.append(startState)
  current_State = pathList[0]

  while( current_State != goalState ):
    for node in graph.keys():
      if (node == current_State):
        minCost = 99999
        minNode = current_State

        for neighborNode in graph[node]:
          currNode = neighborNode[0]
          if(heuristicValue[currNode] < minCost):
            minCost = heuristicValue[currNode]
            minNode = currNode
  
        pathList.append(minNode)

    current_State = pathList[ len(pathList)-1 ]

  print(f"The Hill Climbing Algorithm:")
  print(f"\nThe path is as per below: \nStart State -> ", end="")
  for pathNode in pathList:
    print(f"{pathNode} -> ", end="")
  print(f"Goal State")

#Driver code

Start_State = "A"
Goal_State = "F"

hill_climbing(Start_State, Goal_State)