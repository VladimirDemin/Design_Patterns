result_file = '/var/data/data.txt'
output_file = '/var/result/result.txt'

with open(result_file, 'r') as f:
    numbers = [int(line.strip()) for line in f]

min_number = min(numbers)
count_min = numbers.count(min_number)

with open(output_file, 'w') as f:
    f.write(str(count_min))

print(count_min)
