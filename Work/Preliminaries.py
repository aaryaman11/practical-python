with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f) # advaces the file iterator to the next line, effectively skipping the header
# print(headers) 
    for line in f: # loop starts reading from the second line onward,
        print(line, end='')