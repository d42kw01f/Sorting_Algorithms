def selectionsort(Arr):
	numComp = 0
	for i in range(len(Arr)):
		minVal = i
		for j in range(i, len(Arr)):
			numComp += 1
			if Arr[j] < Arr[minVal]:
				minVal = j
		temp = Arr[i]
		Arr[i] = Arr[minVal]
		Arr[minVal] = temp
	return numComp, Arr


if __name__ == '__main__':
    TheArr = [32,421,21,32,5312,52,12,32,32,12]
    count,FinalArr = selectionsort(TheArr)
    print(FinalArr)
    print(count)
