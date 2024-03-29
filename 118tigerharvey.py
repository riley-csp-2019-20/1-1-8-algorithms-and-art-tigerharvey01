import turtle as trtl

painter = trtl.Turtle()

painter.pensize(3)
painter.speed(3)

#Draw Face
painter.color('black')
painter.pendown()
painter.circle(100)

#Draw Right Ear
painter.penup()
painter.setx(50)
painter.sety(185)
painter.pendown()
painter.begin_fill()
painter.right(90)
painter.circle(30,-260)
painter.end_fill()

#Draw Left Ear
painter.penup()
painter.setx(-50)
painter.sety(185)
painter.pendown()
painter.left(170)
painter.begin_fill()
painter.right(90)
painter.circle(30,260)
painter.end_fill()

#Draw Left Eye
painter.penup()
painter.setx(-40)
painter.sety(90)
painter.pendown()
painter.begin_fill()
painter.circle(30)
painter.end_fill()
painter.left(10)
painter.penup()
painter.setx(-30)
painter.sety(110)
painter.pendown()
painter.color('white')
painter.begin_fill()
painter.circle(15)
painter.end_fill()
painter.penup()
painter.setx(-30)
painter.sety(115)
painter.pendown()
painter.color('black')
painter.begin_fill()
painter.circle(5)
painter.end_fill()

# Right Eye
painter.penup()
painter.setx(40)
painter.sety(90)
painter.pendown()
painter.begin_fill()
painter.circle(30)
painter.end_fill()
painter.left(10)
painter.penup()
painter.setx(30)
painter.sety(110)
painter.pendown()
painter.color('white')
painter.begin_fill()
painter.circle(15)
painter.end_fill()
painter.penup()
painter.setx(30)
painter.sety(115)
painter.pendown()
painter.color('black')
painter.begin_fill()
painter.circle(5)
painter.end_fill()

#Draw nose
painter.color('black')
painter.penup()          
painter.setx(0)
painter.sety(50)
painter.pendown()
painter.begin_fill()
painter.circle(10)
painter.end_fill()

#draw mouth 
painter.right(90)
painter.circle(20,180)
painter.penup()
painter.setx(0)
painter.sety(50)
painter.pendown()
painter.circle(20, -180)