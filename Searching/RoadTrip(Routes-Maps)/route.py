#!/usr/local/bin/python3
# route.py : Find routes through maps
#
# Code by: Dheeraj Manchandia
#
# Based on skeleton code by V. Mathur and D. Crandall, Fall 2022
#


# !/usr/bin/env python3
import sys
import math

# Function to find the successor cities from a city

def successors(city,segments,v):
    succ = []
    
    # Loop to run through the segments datasets
    
    for i in range(len(segments)):
        
        # Locate the segment starting or ending with the given city
        # If found check if it's not already visited
        # Then add it as a successor city
        
        if segments[i][0] == city and segments[i][1] not in v:
            succ.append([segments[i][1],segments[i][2],segments[i][3],segments[i][4]])
        if segments[i][1] == city and segments[i][0] not in v:
            succ.append([segments[i][0],segments[i][2],segments[i][3],segments[i][4]])
            
    return succ

# Function for cost function : segments, tries to find a route with the fewest number of road segments (i.e. edges of the graph) 

def cost_segments(start, end, segments):
    
    # Fringe list
    
    fringe = []
    
    # Add starting city
    
    fringe += [(((((0,start),[]),0),0),0)] 
    
    # Visited list
    v = []
    
    # Loop through the fringe (priority queue)
    while len(fringe) > 0:
        
        # Sort the fringe to get the highest priority(lowest heuristic value) successor
        fringe.sort()
        
        # Pop first element from queue
        (((((seg,city),path),distance),time),delivery) = fringe.pop(0)
        
        # Add it to the visited list
        v.append(city)
                
        # Check goal, if city is the end city, return the solution
        if city == end:
            return (path,float(distance),time,delivery)
    
        # Loop thorugh the successors
        for s in successors(city,segments,v):
            
            
            # Logic to calculate the delivery time
            tr = int(s[1])/int(s[2])
            tt = delivery
            p = math.tanh(int(s[1])/1000)
            
            if int(s[2]) >= 50:
                t = tt + tr + (p * 2 * (tr + tt))
            else:
                t = tt + (int(s[1])/int(s[2]))
            
            # Append the successors in the fringe
            # Heuristic will be the segments travelled + 1, for the new segment
            # Other parameters are just added to their previous values
            # Fringe will be sorted based on the value of segments
            
            fringe.append((((((seg + 1, s[0]), path + [(s[0],s[3] + " for "+s[1]+" miles ")]), distance + int(s[1])), time + (int(s[1])/int(s[2]))),t))
    
    return ([],0,0,0)

# Function for cost function : distance, tries to find a route with the shortest total distance

def cost_distance(start, end, segments):
    
    # Fringe list
    
    fringe = []
    
    # Add starting city
    
    fringe += [(((((0,start),[]),0),0),0)] 
    
    # Visited list
    v = []
    
    # Loop through the fringe (priority queue)
    while len(fringe) > 0:
        
        # Sort the fringe to get the highest priority(lowest heuristic value) successor
        fringe.sort()
        
        # Pop first element from queue
        (((((distance,city),path),seg),time),delivery) = fringe.pop(0)
        
        # Add it to the visited list
        v.append(city)
        
        # Check goal, if city is the end city, return the solution
        if city == end:
            return (path,float(distance),time,delivery)
    
        # Loop thorugh the successors
        for s in successors(city,segments,v):
            
            # Logic to calculate the delivery time
            
            tr = int(s[1])/int(s[2])
            tt = delivery
            p = math.tanh(int(s[1])/1000)
            
            if int(s[2]) >= 50:
                t = tt + tr + (p * 2 * (tr + tt))
            else:
                t = tt + (int(s[1])/int(s[2]))
            
            # Append the successors in the fringe
            # Heuristic will be the distance travelled + distance of new segment
            # Other parameters are just added to their previous values
            # Fringe will be sorted based on the value of distance
            
            fringe.append((((((distance + int(s[1]), s[0]), path + [(s[0],s[3] + " for "+s[1]+" miles ")]), seg + 1), time + (int(s[1])/int(s[2]))),t))
    
    return ([],0,0,0)

# Function for cost function : time, finds the fastest route, assuming one drives the speed limit

def cost_time(start, end, segments):
    
    # Fringe list
    
    fringe = []
    
    # Add starting city
    
    fringe += [(((((0,start),[]),0),0),0)] 
    
    # Visited list
    v = []
    
    # Loop through the fringe (priority queue)
    while len(fringe) > 0:
        
        # Sort the fringe to get the highest priority(lowest heuristic value) successor
        fringe.sort()
        
        # Pop first element from queue
        (((((time,city),path),distance),seg),delivery) = fringe.pop(0)
        
        # Add it to the visited list
        v.append(city)
                
        # Check goal, if city is the end city, return the solution
        if city == end:
            return (path,float(distance),time,delivery)
    
        # Loop thorugh the successors
        for s in successors(city,segments,v):
            
            # Logic to calculate the delivery time
            
            tr = int(s[1])/int(s[2])
            tt = delivery
            p = math.tanh(int(s[1])/1000)
            
            if int(s[2]) >= 50:
                t = tt + tr + (p * 2 * (tr + tt))
            else:
                t = tt + (int(s[1])/int(s[2]))
            
            # Append the successors in the fringe
            # Heuristic will be the time taken to trvel till now + time that will take to travel via new segment
            # Time is calulated as, Time = Distance / Speed (max limit as in dataset)
            # Other parameters are just added to their previous values
            # Fringe will be sorted based on the value of time
            
            fringe.append((((((time + (int(s[1])/int(s[2])), s[0]), path + [(s[0],s[3] + " for "+s[1]+" miles ")]), distance + int(s[1])), seg + 1),t))
    
    return ([],0,0,0)
    
# Function for cost function : delivery, finds the fastest route, in expectation, for a certain delivery driver

def cost_delivery(start, end, segments):
    
    # Fringe list
    
    fringe = []
    
    # Add starting city
    
    fringe += [(((((0,start),[]),0),0),0)] 
    
    # Visited list
    v = []
    
    # Loop through the fringe (priority queue)
    while len(fringe) > 0:
        
        # Sort the fringe to get the highest priority(lowest heuristic value) successor
        fringe.sort()
        
        # Pop first element from queue
        (((((delivery,city),path),distance),time),seg) = fringe.pop(0)
        
        # Add it to the visited list
        v.append(city)
             
        # Check goal, if city is the end city, return the solution
        if city == end:
            return (path,float(distance),time,delivery)
        
        # Loop thorugh the successors
        for s in successors(city,segments,v):
            
            # Logic to calculate the delivery time
            
            tr = int(s[1])/int(s[2])
            tt = delivery
            p = math.tanh(int(s[1])/1000)
            
            if int(s[2]) >= 50:
                t = tt + tr + (p * 2 * (tr + tt))
            else:
                t = tt + (int(s[1])/int(s[2]))
            
            # Append the successors in the fringe
            # Heuristic will be the delivery time calculated till now + delivery time for new segment
            # Other parameters are just added to their previous values
            # Fringe will be sorted based on the value of segments
            
            fringe.append(((((( t, s[0]), path + [(s[0],s[3] + " for "+s[1]+" miles ")]), distance + int(s[1])), time + (int(s[1])/int(s[2]))),seg + 1))
    
    return ([],0,0,0)
    
def get_route(start, end, cost):
    
    """
    Find shortest driving route between start city and end city
    based on a cost function.
    Your function should return a dictionary having the following keys:
        -"route-taken" : a list of pairs of the form (next-stop, segment-info), where
           next-stop is a string giving the next stop in the route, and segment-info is a free-form
           string containing information about the segment that will be displayed to the user.
           (segment-info is not inspected by the automatic testing program).
        -"total-segments": an integer indicating number of segments in the route-taken
        -"total-miles": a float indicating total number of miles in the route-taken
        -"total-hours": a float indicating total amount of time in the route-taken
        -"total-delivery-hours": a float indicating the expected (average) time 
                                   it will take a delivery driver who may need to return to get a new package
    """
    
    road_segments = []
    with open("road-segments.txt", 'r') as file:
         for line in file:
            road_segments += [ line.split() ]

    route_taken = []
    
    if cost == "segments":
        route_taken,distance,time,delivery = cost_segments(start, end, road_segments)
    elif cost == "distance":
        route_taken,distance,time,delivery = cost_distance(start, end, road_segments)
    elif cost == "time":
        route_taken,distance,time,delivery = cost_time(start, end, road_segments)
    elif cost == "delivery":
        route_taken,distance,time,delivery = cost_delivery(start, end, road_segments)
    
    #route_taken = [("Martinsville,_Indiana","IN_37 for 19 miles"),
    #               ("Jct_I-465_&_IN_37_S,_Indiana","IN_37 for 25 miles"),
    #               ("Indianapolis,_Indiana","IN_37 for 7 miles")]
    
    return {"total-segments" : len(route_taken), 
            "total-miles" : distance, 
            "total-hours" : time, 
            "total-delivery-hours" : delivery, 
            "route-taken" : route_taken}


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise(Exception("Error: expected 3 arguments"))

    (_, start_city, end_city, cost_function) = sys.argv
    if cost_function not in ("segments", "distance", "time", "delivery"):
        raise(Exception("Error: invalid cost function"))

    result = get_route(start_city, end_city, cost_function)

    # Pretty print the route
    print("Start in %s" % start_city)
    for step in result["route-taken"]:
        print("   Then go to %s via %s" % step)

    print("\n          Total segments: %4d" % result["total-segments"])
    print("             Total miles: %8.3f" % result["total-miles"])
    print("             Total hours: %8.3f" % result["total-hours"])
    print("Total hours for delivery: %8.3f" % result["total-delivery-hours"])


