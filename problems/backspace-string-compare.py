def backspaceCompare(S, T):
	S = S.lstrip("#")
	T = T.lstrip("#")
	S = [i for i in S]
	T = [i for i in T]
	while "#" in S:
		S = [i for i in "".join(S).lstrip("#")]
		try:
			ind = S.index("#")
			del S[ind]
			del S[ind-1]
		except:
			pass
	while "#" in T:
		T = [i for i in "".join(T).lstrip("#")]
		try:
			ind = T.index("#")
			del T[abs(ind)]
			del T[abs(ind-1)]
		except:
			pass

	return (S==T)

print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a##c", "#a#c"))
print(backspaceCompare("a#c", "b"))
import numpy as np
print("Imported numpy")