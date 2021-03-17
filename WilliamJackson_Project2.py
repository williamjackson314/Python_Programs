from graphics import *
from random import *
from time import *

IsItExposed = [False for i in range(16)]

PicturesNamesList = ["0.gif","1.gif","2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif",
                  "0.gif","1.gif","2.gif", "3.gif", "4.gif", "5.gif", "6.gif", "7.gif"]

Backs = ["back.gif" for i in range(16)]



PlayerMoves = 0
MatchesSoFar = 0

def DrawPicture(file_name, x_coordinate, y_coordinate, window):

   image = Image(Point(x_coordinate, y_coordinate), file_name)
   image.draw(window)


def DecideWhichCard(x, y):


   if (242.5<=x<=337.5) and (72.5<=y<=167.5):

      index = 0
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(290, 120), image)

  
   elif (342.5<=x<=437.5) and (72.5<=y<=167.5):

      index = 1
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(390, 120), image)

   elif (442.5<=x<=537.5) and (72.5<=y<=167.5):

      index = 2
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(490, 120), image)

   elif (542.5<=x<=637.5) and (72.5<=y<=167.5):

      index = 3
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(590, 120), image)


   elif (242.5<=x<=337.5) and (172.5<=y<=267.5):

      index = 4
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(290, 220), image)

   elif (342.5<=x<=437.5) and (172.5<=y<=267.5):

      index = 5
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(390, 220), image)

   elif (442.5<=x<=537.5) and (172.5<=y<=267.5):

      index = 6
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(490, 220), image)

   elif (542.5<=x<=637.5) and (172.5<=y<=267.5):

      index = 7
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(590, 220), image)

   elif (242.5<=x<=337.5) and (272.5<=y<=367.5):

      index = 8
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(290, 320), image)

   elif (342.5<=x<=437.5) and (272.5<=y<=367.5):

      index = 9
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(390, 320), image)

   elif (442.5<=x<=537.5) and (272.5<=y<=367.5):

      index = 10
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(490, 320), image)

   elif (542.5<=x<=637.5) and (272.5<=y<=367.5):

      index = 11
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(590, 320), image)

   elif (242.5<=x<=337.5) and (372.5<=y<=467.5):

      index = 12
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(290, 420), image)

   elif (342.5<=x<=437.5) and (372.5<=y<=467.5):

      index = 13
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(390, 420), image)

   elif (442.5<=x<=537.5) and (372.5<=y<=467.5):

      index = 14
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(490, 420), image)

   elif (542.5<=x<=637.5) and (372.5<=y<=467.5):
      index = 15
      back = Backs[index]
      image = PicturesNamesList[index]
      flipped_image = Image(Point(590, 420), image)
      
   else:
      index = -1
      back = 16

   return index, flipped_image
   
def HasItBeenClickedBefore(x_coordinate, y_coordinate, exposed_list):

   index, flipped_image = DecideWhichCard(x_coordinate, y_coordinate)

   if exposed_list[index] == True:
      return True

   else:
      IsItExposed[index] = True
      return False

   
def CheckMatches(card_1, card_2):

   if card_1 == card_2:
      return True

   else:
      return False

def DrawGameWindow(window):


   DrawPicture("seabackground.gif", 400, 300, window)
   
   name_text = Text(Point(400, 270),"Please Enter Your Name")
   name_text.setSize(16)
   name_text.setTextColor("black")
   name_text.draw(window)

   name_entry = Entry(Point(400,300), 20)
   name_entry.setSize(14)
   name_entry.draw(window)
     
   window.getMouse()
   name_text.undraw()
   name_entry.undraw()

   match_text1 = Text(Point(120, 100), "MATCH THE")
   match_text1.setSize(16)
   match_text1.draw(window)

   match_text2 = Text(Point(120, 130), "SEA CREATURES")
   match_text2.setSize(16)
   match_text2.draw(window)

   name = name_entry.getText()
   username_text = Text(Point(120, 200), name.title())
   username_text.setSize(16)
   username_text.draw(window)

   player_moves = Text(Point(120, 300), PlayerMoves)
   player_moves.setSize(16)
   player_moves.draw(window)

   matches_so_far = Text(Point(120, 400), MatchesSoFar)
   matches_so_far.setSize(16)
   matches_so_far.draw(window)

   return player_moves, matches_so_far,  match_text1, match_text2

def DrawCards(window):

   y_coordinate = 120
   for i in range(4):
      x_coordinate = 290
      for i in range(1,4):
         DrawPicture("back.gif", x_coordinate, y_coordinate, window)
         x_coordinate += 100
      DrawPicture("back.gif", x_coordinate, y_coordinate, window)
      y_coordinate += 100  

   
def main():

   PlayerMoves = 0
   MatchesSoFar = 0
 
   shuffle(PicturesNamesList)
   
   project_window = GraphWin("Match the Sea Creatures", 800, 600)

   player_moves, matches_so_far, match_text1, match_text2 = DrawGameWindow(project_window)

   
   beginTime = time()
   
   DrawCards(project_window)



   while MatchesSoFar < 8:
      
      mouse_click1 = project_window.getMouse()
      x1 = mouse_click1.getX()
      y1 = mouse_click1.getY()
      index1, flipped_image1 = DecideWhichCard(x1, y1)
      exposed1 = HasItBeenClickedBefore(x1, y1, IsItExposed) 
      
      while True:
         if index1 == (-1):
            print("Please click on a card.")
            break
         else:
            flipped_image1.draw(project_window)
            break

      mouse_click2 = project_window.getMouse()
      x2 = mouse_click2.getX()
      y2 = mouse_click2.getY()
      exposed2 = HasItBeenClickedBefore(x2, y2, IsItExposed)

      if exposed2 == False:                 
         index2, flipped_image2 = DecideWhichCard(x2, y2)
         while True:
            if index2 == (-1):
               print("Please click on a card.")
               break
            else:
               flipped_image2.draw(project_window)
               break

         PlayerMoves += 1
         player_moves.setText(PlayerMoves)

         sleep(.5)
         
         image1 = PicturesNamesList[index1]
         image2 = PicturesNamesList[index2]
     
         match_test = CheckMatches(image1, image2)
         if match_test == True:
            MatchesSoFar += 1
            matches_so_far.setText(MatchesSoFar)
            match_text2.undraw()
            match_text1.setText("MATCH!")
            sleep(.4)
            match_text2.draw(project_window)
            match_text1.setText("MATCH THE")
            
         else:
            flipped_image1.undraw()
            flipped_image2.undraw()
            IsItExposed[index1] = False
            IsItExposed[index2] = False

      else:
            
            match_text1.setText("Please Click On An")
            match_text2.setText("Unflipped Card.")
            sleep(1.3)
            match_text1.setText("MATCH THE")
            match_text2.setText("SEA CREATURES")     

   endTime = time()
   time_difference = endTime - beginTime
   
   match_text1.setText("Game Time: ")
   match_text2.setText(str(int(time_difference)) + " Seconds")

main()

'''
Loop that controls the game  
   while IsItExposed != True:

      mouse_click1 = project_window.getMouse()
      x1 = mouse_click1.getX()
      y1 = mouse_click1.getY()

      HasItBeenClickedBefore(x1, y1, IsItExposed, project_window)
      index1, image1 = DecideWhichCard(x1, y1)

      mouse_click2 = project_window.getMouse()
      x2 = mouse_click2.getX()
      y2 = mouse_click2.getY()

      HasItBeenClickedBefore(x2, y2, IsItExposed, project_window)
      index2 = DecideWhichCard(x2, y2)
      
      CheckMatches(image1, image2) 
               if  == True:
               print("Please pick a different card.")
               break
            else:
            if HasItBeenClickedBefore(x2, y2, IsItExposed) == True:
               print("Please pick a different card.")
               break
            else:

project_window = GraphWin("Match the Sea Creatures", 800, 600)
player_moves, matches_so_far = DrawGameWindow(project_window)
BeginTime = time()
DrawCards(project_window)
mouse_click1 = project_window.getMouse()
x1 = mouse_click1.getX()
y1 = mouse_click1.getY()
print(str(x1) + ", " + str(y1))


 
def InsertInsideTheTopPlayer(player_name, game_time, window):

   player_scores = []                    
   FileHandler = open(TopPlayersScores.txt, "r")
   top_players = TopPlayersScores.readlines()
   FileHandler.close()

   for line in top_players:                    
     line = top_players.split(",")
     players.append(line[0])
     player_scores.append(line[1])                  
      

   player_info = player_name + ", " + str(game_time)
   if game_time < 50:
      top_players.insert(0, player_info)
   #elif game_time
               
''' 
