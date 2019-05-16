'dental',
'dentist',
'smile',
'dds',
'ortho',
'dr'

keywords = ['dental',
            'dentist',
            'smile',
            'dds',
            'ortho',
            'dr']

inp_filename = input('Enter an input file name: ')

with open(inp_filename, 'r') as f:
    emails = f.read().split('\n')
    print('Total emails found:', len(emails))

good_emails = []

for email in emails:
    for keyword in keywords:
        if keyword in email:
            good_emails.append(email)
            break

print('After removing irrelevant emails:', len(good_emails), 'left')

out_filename = 'good-' + inp_filename

with open(out_filename, 'w') as f:
    for email in good_emails:
        f.write(email + '\n')