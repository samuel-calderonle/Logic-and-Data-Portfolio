# 10/16/2024
# By: Samuel C.
# Purpose: use classes and objects to tell a story

class Superhero:

	def __init__(self, name = "", strengthPts = 0, power = "", nemesis = ""):
		self.name = name
		self.strengthPts = strengthPts
		self.power = power
		self.nemesis = nemesis
	
	def addStrengthPts(self, points):
		self.strengthPts += points
	
	def defeatNemesis(self):
		print(self.name + " has defeated his long-time rival, " + self.nemesis + ". This is a day of celebration for " + self.name + "!")


def main():

	ironMan = Superhero("Iron Man", 238, "strength and durability", "The Mandarin")

	# Retell a story
	print(ironMan.name + " is a great hero and what sets him apart is his " + ironMan.power + ".")
	print("When facing his nemesis, " + ironMan.nemesis + ", " + ironMan.name + " is determined.")	
	print("Today, " + ironMan.nemesis + " attacked " + ironMan.name + " by surprise.")
	print("Despite shocked, " + ironMan.name + " fought ??.")
	print("After a long and intense battle, " + ironMan.name + " managed to win.")
	ironMan.defeatNemesis()
	print("This heroic act earns " + ironMan.name + " 317 strength points.")
	ironMan.addStrengthPts(317)
	print("Now, he has a total of " + str(ironMan.strengthPts) + " strength points.")

main()