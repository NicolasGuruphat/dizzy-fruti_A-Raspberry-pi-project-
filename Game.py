from tkinter import *
from UI import UI
from Bowl import Bowl
from Fruit import Fruit
from Score import Score
from time import *

class Game:

	def __init__(self):
		self.interface=UI(self)
		self.interface.displayMainMenu()
		self.listFruit=[]
		self.interface.root.TkMenu.mainloop()
		self.victory
		
	def fruitFactory(self) :
		if(not self.victory): 
			self.listFruit.append(Fruit(self.interface.getMenu()))
			self.interface.getMenu().TkMenu.after(1000,self.fruitFactory)
			
	def fruitFalling(self) : 
		for fruit in self.listFruit :
			Fruit.moveDown(fruit,self.interface)
			if(Fruit.verifyCollisionBowl(fruit,self.bowl)):
				self.score.increment(fruit.point)
				self.listFruit.remove(fruit)
				print(self.score.value)
				self.victory=self.score.value>=64		
			elif(Fruit.verifyCollisionGround(fruit,self.interface.menu.taille)):
				self.listFruit.remove(fruit)
				print("hit the ground")
		if(not self.victory):
			self.interface.getMenu().TkMenu.after(60,self.fruitFalling)
		else :
			self.win()

	def play(self):
		print("Play !")
		self.victory=False
		self.interface.displayGameMenu()
		self.bowl=Bowl(self.interface.getMenu())
		self.interface.getMenu().TkMenu.bind('<KeyPress-Left>',lambda event :self.bowl.move("left"))
		self.interface.getMenu().TkMenu.bind('<KeyPress-Right>',lambda event :self.bowl.move("right"))
		self.score=Score()
		self.fruitFactory()
		self.fruitFalling()
	

	def win(self):
		print("well play ! you won")
		self.interface.displayWinMenu()


game=Game()




