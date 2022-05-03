import random
import time
def route_Length(tsp, solution):
    RouteLength = 0
    for i in range(len(solution)):
        RouteLength += tsp[solution[i - 1]][solution[i]]
    return RouteLength

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def Get_possible_Neighbours(solution):
    possible_neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            possible_neighbours.append(neighbour)
    return possible_neighbours

def Get_Best_Neighbours(tsp, neighbours):
    Best_Route_Length = route_Length(tsp, neighbours[0])
    Best_Neighbour = neighbours[0]
    for neighbour in neighbours:
        current_Route_Length = route_Length(tsp, neighbour)
        if current_Route_Length < Best_Route_Length:
            Best_Route_Length = current_Route_Length
            Best_Neighbour = neighbour
    return Best_Neighbour, Best_Route_Length

#Implementation of Hill CLimb algorithm

def Hill_Climbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = route_Length(tsp, currentSolution)
    neighbours = Get_possible_Neighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = Get_Best_Neighbours(tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = Get_possible_Neighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = Get_Best_Neighbours(tsp, neighbours)
    
    print("The Best path for Travelling salesman is as per below:")
    print("Start City/node -> " , end = "")
    for i in range(len(currentSolution)):
      print(currentSolution[i] , " -> " , end = "")

    print( " City/node")
    print("\nThe Cost of above path is:  ", currentRouteLength)

    #return currentSolution, currentRouteLength

#Driver Code

TSP_path = [
      [0, 2529, 1989, 2856],
      [1000, 0, 2856, 1989],
      [2000, 2323, 0, 2529],
      [2323, 2000, 1000, 0]
  ]

'''
TSP_path = [
      [0, 1400, 800, 1253],
      [1400, 0, 1253, 800],
      [800, 1253, 0, 1400],
      [1253, 800, 1400, 0]
  ]
'''


start_time = time.time()

Hill_Climbing(TSP_path)

finish_time = time.time()

print("\nThe time of execution of TSP using Hill Climb algorithm is :", finish_time - start_time)
