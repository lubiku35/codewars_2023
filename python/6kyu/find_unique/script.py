def find_uniq(arr):
	arr = sorted(arr, reverse=True)
	return max(arr) if arr[0] != arr[1] and arr[0] != arr[2] else min(arr) 



print(find_uniq([ 1, 1, 1, 2, 1, 1 ])) # 2 1 1 1 
print(find_uniq([ 0, 0, -1, 0, 0 ])) # 0 0 0 -1
print(find_uniq([ 3, 10, 3, 3, 3 ])) # 10 3 3 3 3 3 
