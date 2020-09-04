content = open('new1.txt', 'r').readlines()
content_set = set(content)
cleandata = open('new2.txt', 'w')
for line in content_set:
    cleandata.write(line)