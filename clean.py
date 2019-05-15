from datetime import datetime

filename = 'emails.txt'

data = []

with open(filename, 'r') as f:
    data = f.read().split('\n')
    print('Number of emails:', len(data))
    print('Removing duplicates...')
    data = set(data)
    print('Number of emails after removing dupes:', len(data))

filename = datetime.now().strftime('%H-%M-') + filename
print(filename)
with open(filename, 'w') as f:
    for line in data:
        f.write(line + '\n')
