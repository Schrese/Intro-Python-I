# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
# class Waypoint:
#     def __init__(self, name, lat, lon): 
#         self.name
#         self.lat = lat
#         self.lon = lon
# If we do it like above ^^ It would mean that it isn't inherited
class Waypoint(LatLon):
    def __init__(self, name, lat, lon): 
        # use the 'super method to access methods on the partent class
        super().__init__(lat, lon)
        self.name = name
        # question: can we get rid of name on line 21? Answer: no, it needs all of them

    # the "__str__" method allows us to define how we want to how we want the class to be printed out
    def __str__(self):
        # this method returns a string that can then be printed
        return f"<Waypoint '{self.name}', {self.lat}, {self.lon}>"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, diff, size, lat, lon):
        super().__init__(name, lat, lon)
        self.diff = diff
        self.size = size
    def __str__(self):
        return f"<Geocache '{self.name}', {self.diff}, {self.size}, {self.lat}, {self.lon}>"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
# this is the initializer, there's no "new" keyword, you just pass in the right things
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)
# first time we printed, we got "<__main__.Waypoint object at 0x7f48d1e867c0>", which is an object Id (I need to look this up again 12:48 in video)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
# Note: This printed using the string method of the Waypoint by default (if none is provided in Geochache class)


# Print it--also make this print more nicely
print(geocache)
