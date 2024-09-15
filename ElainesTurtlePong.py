import turtle

screenWidth = 800;
screenHeight = 600;
scale = 20
pixelWidth = 1;

window = turtle.Screen()
window.title("Turtle Pong")
window.bgcolor("black")
window.tracer(0)
window.setup(width=screenWidth, height=screenHeight)
window._root.resizable(False, False)

class sprite:
	def __init__(self, color, width, height, x, y):
		self.color = color
		self.width = width
		self.height = height
		self.x = x
		self.y = y

		self.turtle = turtle.Turtle()
		self.turtle.shape("square")
		self.turtle.speed(0)
		self.turtle.penup()

	def drawSprite(self):
		self.turtle.shapesize(stretch_wid = self.height, stretch_len = self.width)
		self.turtle.color(self.color)
		self.turtle.goto(self.x, self.y)
	
	def moveUp(self):
		self.y += pixelWidth*scale

	def moveDown(self):
		self.y -= pixelWidth*scale

class text():
	def __init__(self, color, characters, font, size, x, y):
		self.color = color
		self.characters = characters
		self.font = font
		self.size = size
		self.x = x
		self.y = y
		
		self.turtle = turtle.Turtle()
		self.turtle.speed(0)
		self.turtle.penup()
		self.turtle.hideturtle()

	def writeText(self):
		self.turtle.clear()
		self.turtle.color(self.color)
		self.turtle.goto(self.x, self.y)
		self.turtle.write(self.characters, align="center", font=(self.font, self.size, "normal"))

score1 = 0
score2 = 0

player1 = sprite("white", pixelWidth, 5*pixelWidth, -320, 0)
player2 = sprite("white", pixelWidth, 5*pixelWidth, 320, 0)
ball = sprite("white", pixelWidth, pixelWidth, 0,0)

title = text("white", "Pong Demo", "Comic Sans MS", 24, 0, 250)
title.writeText()
p1Score = text("white", score1,  "Comic Sans MS", 35, -200, 200)
p1Score.writeText()
p2Score = text("white", score2,  "Comic Sans MS", 35, 200, 200)
p2Score.writeText()

dx = 0.1
dy = 0.1

def resetPos():
	global dx
	dx *= -1
	ball.x = 0
	ball.y = 0

window.listen()
	

while True:
	window.onkeypress(player1.moveUp, "w")
	window.onkeypress(player1.moveDown, "s")
	window.onkeypress(player2.moveUp, "Up")
	window.onkeypress(player2.moveDown, "Down")

	ball.x += dx
	ball.y += dy

	if ball.x > screenWidth/2 - 10:
		resetPos()
		score1 += 1
		p1Score.characters = score1
		p1Score.writeText()
	if ball.x < -screenWidth/2 + 10:
		resetPos()
		score2 += 1
		p2Score.characters = score2
		p2Score.writeText()

	if ball.y > screenHeight/2 - 10 or ball.y < -screenHeight/2 +10:
		dy *= -1
	
	if (ball.x > player2.x - player2.width * scale/2 and
		ball.x < player2.x + player2.width * scale/2 and
		ball.y > player2.y - player2.height * scale/2 and
		ball.y < player2.y + player2.height * scale/2):
		dx *= -1  
		ball.x = player2.x - (player2.width * scale/2)

	if (ball.x > player1.x - player1.width * scale/2 and
		ball.x < player1.x + player1.width * scale/2 and
		ball.y > player1.y - player1.height * scale/2 and
		ball.y < player1.y + player1.height * scale/2):
		dx *= -1  
		ball.x = player1.x + (player1.width * scale/2)

	player1.drawSprite()
	player2.drawSprite()
	ball.drawSprite()
	window.update()

