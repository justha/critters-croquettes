from flyers import Elephant, FlyingMonkey
from hoppers import Kangaroo, Rabbit
from slitherers import KingSnake
from swimmers import Duck, Penguin
from walkers import Alpaca, Donkey, Horse, Koala, Lemur, Llama, Pig, Sloth


fuzz = Llama("Fuzz", "domestic llama", "morning", "llama chow mix")
snakey = KingSnake("Snakey", "king snake", "morning", "fruit-by-the-foot")
quinn = Penguin("Quinn", "arctic penguin", "morning", "Klondike Bar")
donald = Duck("Donald", "quacky duck", "morning", "bruschetta")
my_little = Horse("My Little", "miniature horse", "morning", "rainbow mallows")
wooly = Alpaca("Wooly", "moppy-haired alpaca", "midday", "hot cocoa")
eeyore = Donkey("Eeyore", "ditzy donkey", "midday", "thistles")
kiddo = Kangaroo("Kiddo", "maternal roo", "midday", "culantro")
choc = Rabbit("Choc", "festive bunny", "midday", "Woppers Robin Eggs")
flash = Sloth("Flash", "quick-witted sloth", "midday", "sour gummy worms")
blinky = Koala("Blinky", "friendly koala bear", "afternoon", "coriander leaves")
wilbur = Pig("Wilbur", "timid pig", "afternoon", "cotton candy")
leapin = Lemur("Leapin", "lemur", "afternoon", "Reese's pb cups")
manny = FlyingMonkey("Manny", "narcissistic monkey", "afternoon", "banana pudding")
dumbo = Elephant("Dumbo", "peanut-eating elephant", "afternoon", "packing peanuts")

print(f'{wilbur.name} the {wilbur.species} is available to pet during the {wilbur.shift} shift.')
# prints Wilbur the pig is available to pet during the afternoon shift.

print(wilbur.feed())
print(wilbur)