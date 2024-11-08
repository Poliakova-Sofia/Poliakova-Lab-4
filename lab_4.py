from point_3 import Point_3
import math
import matplotlib.pyplot as plt

    # clear the file
filename = "points_coordinates.txt"
with open(filename, "a") as file: # use "a" to append to file
    file.seek(0)  # move to the beginning of the file
    file.truncate()  # remove everything from the file

    # function for calculating the distance between two points
def distance_to(point1, point2):
        distance = math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
        return round(distance, 2)

    # function for reading exactly three points from user input
def three_points():
        points = [] # list for coordinates
        print("Enter coordinates of 3 points:")
        try:
            for i in range(3): # entering coordinates
                x = float(input(f"Enter X of point {i + 1}: "))
                y = float(input(f"Enter Y of point {i + 1}: "))
                point = Point_3(x, y)
                points.append(point)
        except ValueError: # error notification
            print("Invalid input. Please enter numeric values for coordinates.")
        return points

    # function for saving point coordinates into the file
def save_points(points, stage, filename="points_coordinates.txt"):
        with open(filename, "a") as file: 
            file.write(f"{stage}:\n")
            for i, point in enumerate(points, start=1):
                # write coordinates
                file.write(f" {i}: {point.x}; {point.y}\n") 
            file.write("\n")

    # reading exactly three points from user input
points = three_points()

    # ensure exactly three points are provided
if len(points) == 3:
        # calculation of the distance between the first and third points
        distance = distance_to(points[0], points[2])
        print(f"Distance between point 1 and point 3: {distance}")

        # points with original coordinates
        initial_x = [p.x for p in points]
        initial_y = [p.y for p in points]

        # save the initial coordinates in a file labeled "Before changes"
        save_points(points, "Before changes")

        # move the second point 15 units to the left
        points[1].move(-15, 0)  
        print(f"New coordinates of point 2: ({points[1].x}, {points[1].y})")

        # points with new coordinates
        updated_x = [p.x for p in points]
        updated_y = [p.y for p in points]

        # save the new coordinates in a file labeled "After changes"
        save_points(points, "After changes")

        # plotting
        plt.figure(figsize=(8, 6))

        # plot before changes
        plt.subplot(1, 2, 1)
        plt.scatter(initial_x, initial_y, color='green', label='Before')
        plt.plot(initial_x, initial_y, color='green', linestyle='--', marker='o')
        plt.title("Before the changes")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()

        # plot after changes
        plt.subplot(1, 2, 2)
        plt.scatter(updated_x, updated_y, color='red', label='After')
        plt.plot(updated_x, updated_y, color='red', linestyle='--', marker='o')
        plt.title("After the changes")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()

        # show both plots
        plt.show()
else:
        print("An error occurred. Please enter exactly 3 points.")
    

class Point_3:
  # class variable to count the number of instances (private)
  __instance_count = 0


  def __init__(self, x, y):
   # private variables for coordinates
    self.x = x
    self.y = y
    Point_3.__instance_count += 1


  # method for checking coordinates
  def _validate_coordinate(self, value):
     return value if -100 <= value <= 100 else 0


 # properties for x and y with validation
  @property
  def x(self):
     return self.__x


  @x.setter
  def x(self, value):
     self.__x = self._validate_coordinate(value)


  @property
  def y(self):
     return self.__y


  @y.setter
  def y(self, value):
     self.__y = self._validate_coordinate(value)


  # class method to get the number of instances
  @staticmethod
  def get_instance_count():
     return Point_3.__instance_count


  # method for changing coordinates with an offset
  def move(self, shift_x, shift_y):
     self.x += shift_x
     self.y += shift_y


  # destructor
  def __del__(self):
     Point_3.__instance_count -= 1
     
