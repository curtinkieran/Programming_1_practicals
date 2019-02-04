'''pseudocode
prompt for table size
while i <= table size
    j=0
    while j<=
        print i*j
        increment j
    print newline
    increment i

print finished'''

table_size = int(input('Enter a number: '))
i=1
while i <= table_size:
    j=1
    while j <= table_size:
        print(i*j, ' ', end='')
        j += 1
    print()
    i += 1
