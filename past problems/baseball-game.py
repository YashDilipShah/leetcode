def calPoints(ops):
	score = []
	for i in ops:
		try:
			score.append(int(i))
		except:
			if i == "C":
				del score[-1]
			elif i == "D":
				score.append(score[-1] * 2)
			elif i == "+":
				score.append(score[-1] + score[-2])
		#print(score)
	return sum(score)

print(calPoints(["5","2","C","D","+"]))
print(calPoints(["5","-2","4","C","D","9","+","+"]))