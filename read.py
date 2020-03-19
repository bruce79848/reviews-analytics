data = []
count = 0
with open('reviews.txt', 'r') as r:
	for line in r:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('Finish loading, there are totally', len(data), 'sets of data.')

sum_len = 0
for d in data:
	sum_len += len(d)
print('The average length of each comment is', sum_len / len(data), 'word.')\

new = []
for d in data:
	if len(d) <= 100:
		new.append(d)
print('There are totally', len(new), 'comments which have less than 100 words.')