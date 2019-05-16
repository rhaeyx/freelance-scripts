from datetime import datetime

filename = input('Enter a file name: ')

data = []

with open(filename, 'r') as f:
    data = f.read().split('\n')
    print('Number of emails:', len(data))
    print('Removing duplicates...')
    data = set(data)
    print('Number of emails after removing dupes:', len(data))

filename = 'clean-' + filename
print(filename)
with open(filename, 'w') as f:
    for line in data:
        f.write(line + '\n')
