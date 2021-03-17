from graphics import *


def CalculatingCommission(weekly_sales):
   weekly_sales = int(weekly_sales)
   
   # Determines commission based on amount of weekly_sales
   if weekly_sales > 1000:
      commission = 200 + (.09 * weekly_sales)
   elif weekly_sales <= 1000:
      commission = 100 + (.1 * weekly_sales)
   
   return commission
      
def MicrowaveRecommendedTime(number_of_items,heating_time):
   number_of_items = int(number_of_items)
   heating_time = int(heating_time)
   
   # Determines cooking time based on how many items and how long for baseline 1 item
   if number_of_items == 2:
      heating_time += (heating_time * .5)
   elif number_of_items == 3:   
      heating_time = heating_time * 2
   elif number_of_items > 3:
      print("It is not recommended that you heat more than 3 items at a time.")
   
   return heating_time
   
   
def ShippingCost(weight):
   weight = int(weight)
   
   # Determines shipping cost based on weight of object(s) being shipped
   if (0 < weight <= 1):
      shipping_cost = 3.5
   elif (1 < weight <= 3):
      shipping_cost = 5.5
   elif (3 < weight < 10):
      shipping_cost = 8.5
   elif (10 < weight <= 20):
      shipping_cost = 10.5
   
   return shipping_cost
   
def SoundTime(medium, distance_to_travel):
   distance_to_travel = int(distance_to_travel)

   # Finds speed of sound based on what medium it travels in
   if medium == "air":
      speed = 1100 
   if medium == "water":
      speed = 4900
   
   # Calculates the time it takes for sound to travel through medium
   time = round((distance_to_travel)/(speed), 3)
   
   return time

def CreateWindow():
   
   # Creates a 600 x 600 window with white background
   Lab5_Window = GraphWin("Lab 5", 600, 600)
   Lab5_Window.setBackground("white")
   
   # Creates red text at top of window 
   text_point = Point(300, 15)
   message = Text(text_point, "Welcome to Lab 5")
   message.setSize(16)
   message.setTextColor("red")
   message.draw(Lab5_Window)
   
   #Draws a blue line at the top of window underneath the text
   endpoint1 = Point(10,25)
   endpoint2 = Point(590, 25)
   line = Line(endpoint1, endpoint2)
   line.setColor("blue")
   line.draw(Lab5_Window)
   
   return Lab5_Window

def CloseWindow(window_name):
   window_name.getMouse()
   window_name.close()

def CreateInterface():
   window = CreateWindow()
   
   # Covers quarter of window with yellow
   corner_point1 = Point(0,0)
   corner_point2 = Point(300,300)
   quad2 = Rectangle(point1, point2)
   quad2.setBackground("yellow")
   quad2.draw(window)
   
   # Creates text saying "Problem #1"
   text_point1 = Point(150,50)
   problem_1 = Text(text_point1, "Problem #1")
   problem_1.setSize(16)
   problem_1.setTextColor("blue")
   problem_1.draw(window)
   
   # Creates text "Sales"
   text_point2 = Point(100, 75)
   sales_text = Text(text_point2, "Sales")
   sales_text.setTextColor("blue")
   sales_text.setSize(14)
   sales_text.draw(window)
   
   #Creates entry next to text for sales amount
   entry_point1 = Point(225,75)
   sales_entry = Entry(entry_point1, 7)
   sales_entry.setSize(14)
   sales_entry.draw(window)


   # Colors top left quadrant of window red
   corner_point3 = Point(300,0)
   corner_point4 = Point(600, 300)
   quad1 = Rectangle(point3, point4)
   quad1.setBackground("red")
   quad1.draw(window)
   
   # Creates text "Problem #2"
   text_point3 = Point(450, 50)
   problem_2 = Text(text_point3, "Problem #2")
   problem_2.setSize(16)
   problem_2.setTextColor("blue")
   problem_2.draw(window)
   
   # Creates text for items
   text_point4 = Point(400, 75)
   items_text = Text(text_point4, "Items")
   items_text.setTextColor("blue")
   items_text.setSize(14)
   items_text.draw(window)
   
   # Creates entry for number of items 
   entry_point2 = Point(525, 75)
   item_entry = Entry(entry_point2, 1)
   item_entry.setSize(14)
   item_entry.draw(window)
   
   # Makes text "time"
   text_point5 = Point(400, 150)
   time_text = Text(text_point5, "Time")
   time_text.setTextColor("blue")
   time_text.setSize(14)
   time_text.draw(window)
   
   #Makes entry for the time to heat up one item
   entry_point3 = Point(525, 150)
   time_entry = Entry(entry_point, 3)
   time_entry.setSize(14)
   time_entry.draw(window)
   

   # Makes bottom left quadrant blue
   corner_point5 = Point(0,300)
   corner_point6 = Point(300,600)
   quad_3 = Rectangle(corner_point5, corner_point6)
   quad_3.setBackground("blue")
   quad_3.draw(window)
   
   # Makes text for Problem #3 title
   text_point6 = Point(150, 350)
   problem_3 = Text(text_point6, "Problem #3")
   problem_3.setTextColor("yellow")
   problem_3.setSize(16)
   problem_3.draw(window)
   
   # Makes text "weight"
   text_point7 = Point(100, 375)
   weight_text = Text(text_point7, "Weight")
   weight_text.setTextColor("yellow")
   weight_text.setSize(14)
   weight_text.draw(window)
   
   # Makes an entry to input weight
   entry_point4 = Point(225, 375)
   weight_entry = Entry(entry_point4, 2)
   weight_entry.setSize(14)
   weight_entry.draw(window)
   
   # Colors bottom right quadrant green 
   corner_point7 = (600,600)
   quad_4 = Rectangle(corner_point2, corner_point7)
   quad_4.setBackground("green")
   quad_4.draw(window)
   
   # Makes title for Problem #4
   text_point8 = Point(450,350)
   problem_4 = Text(text_point8, "Problem #4")
   problem_4.setTextColor("blue")
   problem_4.setSize(16)
   problem_4.draw(window)
   
   # Makes text "Medium"
   text_point9 = Point(400, 375)
   medium_text = Text(text_point9, "Medium")
   medium_text.setTextColor("blue")
   medium_text.setSize(14)
   medium_text.draw(window)
  
  # Creates an entry for the medium of travel of sound
   entry_point5 = (525, 375)
   medium_entry = Entry(entry_point5, 5)
   medium_entry.setSize(14)
   medium_entry.draw(window)
  
  # Creates a text "Distance"
   text_point10 = Point(400, 450)
   distance_text = Text(text_point10, "Distance")
   distance_text.setTextColor("blue")
   distance_text.setSize(14)
   distance_text.draw(window)

   # Makes an entry for distance value
   entry_point6 = (525, 450)
   distance_entry = Entry(entry_point6, 5)
   distance_entry.setSize(14)
   distance_entry.draw(window)
   
   # Draws an oval in each of the four quadrants
   oval_1 = Oval(Point(20,220), Point(290, 270))
   oval_1.draw(window)
   oval_2 = Oval(Point(320,220), Point(585, 270))
   oval_2.draw(window)
   oval_3 = Oval(Point(20, 340), Point(290, 380))
   oval_3.draw(window)
   oval_4 = Oval(Point(320,520), Point(585, 570))
   oval_4.draw(window)
   
   # After mouse click this retrieves the values of each of the entries
   window.getMouse()
   sales = sales_entry.getText()
   items = items_entry.getText()
   time = time_entry.getText()
   weight = weight_entry.getText()
   medium = medium_entry.getText()
   distance = distance_entry.getText()
   
   # Calls the four functions defined below the the entry values from above 
   commission = CalculatingCommission(sales)
   microwave_time = MicrowaveRecommendedTime(items, time)
   shipping_cost = ShippingCost(weight)
   time_of_travel = SoundTime(medium, distance)

   # Displays return value of CalculatingCommission in top left oval
   commission_text_point = Point(150,225)
   commission_text = Text(commission_text_point1, commission)
   commission_text.setTextColor("black")
   commission_text.setSize(16)
   commission_text.draw(window)
   
   # Displays return value of MicrowaveRecommendedTime in top right oval
   microwave_time_point = Point(450,225)
   microwave_time_text = Text(microwave_time_point, microwave_time)
   microwave_time_text.setTextColor("black")
   microwave_time_text.setSize(16)
   microwave_time_text.draw(window)
   
   # Displays the return value of ShippingCost in bottom left oval
   shipping_cost_point = Point(150,525)
   shipping_cost_text = Text(shipping_cost_point, shipping_cost)
   shipping_cost_text.setTextColor("black")
   shipping_cost_text.setSize(16)
   shipping_cost_text.draw(window)
   
   # Displays the return value of SoundTime in bottom right oval
   time_of_travel_point = Point(450,525)
   time_of_travel_text = Text(time_of_travel_point, time_of_travel)
   time_of_travel_text.setTextColor("black")
   time_of_travel_text.setSize(16)
   time_of_travel_text.draw(window)
   
   # Calls function to close window
   CloseWindow()
   
   
def main():
   
   CreateInterface()
   
main()

