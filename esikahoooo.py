import random

f = open("snowflakes.txt", "w")

maxWidth=80
maxHeight=25

minFlakes=0
maxFlakes=5
pelyhek=["*","O", "."]

rows=[]
for _ in range(maxHeight):
	actFlakes=random.randint(minFlakes, maxFlakes)
	actRow=" "*maxWidth

	flakes=random.sample(range(0,maxWidth),actFlakes)

	for i in flakes:
		actRow=actRow[:i]+random.choice(pelyhek)+actRow[i+1:]

	rows.append(actRow)

print("\n".join(rows))
for u in range(len(rows)):
	f.write(rows[:1])
