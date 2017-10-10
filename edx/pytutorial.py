squares = []
for x in range(10):
	squares.append(x**2)
squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


from collections import deque
	queue = deque(["Eric", "John", "Michael"])
	queue.append("Terry")           # Terry arrives
	queue.append("Graham")          # Graham arrives
	queue.popleft()                 # The first to arrive now leaves
	queue.popleft()                 # The second to arrive now leaves
	queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

#tutorial: https://docs.python.org/3.5/tutorial/datastructures.html
#python functions tutorial: http://www.tutorialspoint.com/python/python_functions.htm
#blog OOP: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
