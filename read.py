data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('Finish loading, there are totally', len(data), 'sets of data.')

sum_len = 0
for d in data:
	sum_len += len(d)
print('And the average length of the comments is', sum_len / len(data))
