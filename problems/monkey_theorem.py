#print("456" in "1234567890")
import time
pi = "3141592653589793238462643383279"
array = ['3', '314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793']

def remove_excess(array, excess):
	array_int = [int(i) for i in array]
	array_int.sort()
	while excess != 0:
		excess -= len(str(array_int[0]))
		del array_int[0]
	return array_int


def check(pi, array):
	start_time = time.time()
	pi = str(pi)
	pi_len = len(pi)
	total_len = 0
	contains = []
	for i in array:
		if i in pi:
			contains.append(i)
			total_len += len(i)
	#return min(contains), total_len, len(pi)
	if total_len == pi_len:
		return len(contains) - 1
	else:
		excess = total_len - pi_len
		contains = remove_excess(contains, excess)
		return ("Number of spaces: {} \nTime taken = {}".format(len(contains) - 1, round(time.time() - start_time, 7))), excess


print(check(pi, array))