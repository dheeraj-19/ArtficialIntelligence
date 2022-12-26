# Road trip!

Finding the shortest driving route between two distant places — say, one on the east coast and one on the west coast of the U.S. — is extremely complicated. 
There are over 4 million miles of roads in the U.S. alone, and trying all possible paths between two places would be nearly impossible

To solve this we can use A* search!

A dataset is given which consists of major highway segments of the United States (and parts of southern Canada and northern Mexico), including highway names, distances, and speed limits; we can visualize this as a graph with nodes as towns and highway segments as edges

Also a dataset of cities and towns with corresponding latitude-longitude positions

### Goal:
    Find good driving directions between pairs of cities
    
Code can be run on the command line like this:

python3 ./route.py [start-city] [end-city] [cost-function]

#### Where:
     • start-city and end-city are the cities we need a route between
     • cost-function is one of:
        – segments tries to find a route with the fewest number of road segments (i.e. edges of the graph). – distance tries to find a route with the shortest total distance.
        – time finds the fastest route, assuming one drives the speed limit.
        – delivery finds the fastest route, in expectation, for a certain delivery driver. 
          Whenever this driver drives on a road with a speed limit ≥ 50 mph, there is a chance that a package will fall out of their truck and be destroyed. 
          They will have to drive to the end of that road, turn around, return to the start city to get a replacement, then drive all the way back to where they were (they won’t make the same mistake the second time they drive on that road).
          Consequently, this mistake will add an extra 2 · (troad + ttrip ) hours to their trip, where ttrip is the time it took to get from the start city to the beginning of the road, and troad is the time it takes to drive the length of the road segment.
          For a road of length l miles, the probability p of this mistake happening is equal to tanh( l / 1000) If the speed limit is ≥ 50 mph, and 0 otherwise. 
          This means that, in expectation, it will take troad + p · 2(troad + ttrip) hours to drive on this road.
