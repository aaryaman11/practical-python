with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',') # advaces the file iterator to the next line, effectively skipping the header
# print(headers) 
    for line in f: # loop starts reading from the second line onward,
        row = line.split(',')
        print(row)