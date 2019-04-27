# Furkan MUDANYALI 20181701088
# Emir ÖZTÜRK 20181701062

import stdio, sys, stddraw

print("What shape do you want?\n Hearts = 1 \n Spades = 2 \n Clubs = 3 \n Diamonds = 4")
a = input("Enter: ")
if int(a) < 1 or int(a) > 4 or not a.isdigit():
    print(str(a) + " is not acceptable.")
    sys.exit()
a = int(a)

stddraw.setCanvasSize(640, 640)
if a == 1:
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledPolygon([0.5, 0.2, 0.5, 0.8, 0.5], [0.2, 0.5, 0.8, 0.5, 0.2])
    stddraw.filledCircle(0.65, 0.65, 0.215)
    stddraw.filledCircle(0.35, 0.65, 0.215)
elif a == 2:
    stddraw.filledPolygon([0.5, 0.2, 0.5, 0.8, 0.5], [0.3, 0.6, 0.9, 0.6, 0.3])
    stddraw.filledCircle(0.65, 0.45, 0.215)
    stddraw.filledCircle(0.35, 0.45, 0.215)
    stddraw.filledRectangle(0.475, 0.15, 0.05, 0.15)
elif a == 3:
    stddraw.filledCircle(0.5, 0.7, 0.215)
    stddraw.filledCircle(0.675, 0.4, 0.215)
    stddraw.filledCircle(0.325, 0.4, 0.215)
    stddraw.filledRectangle(0.475, 0.15, 0.05, 0.15)
elif a == 4:
    stddraw.setPenColor(stddraw.RED)
    stddraw.filledPolygon([0.5, 0.2, 0.5, 0.8, 0.5], [0.2, 0.5, 0.8, 0.5, 0.2])
stddraw.show()
