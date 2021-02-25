line = bytes(input('Enter sequence of symbols : '), 'utf-8')

for i in line.split():
    print(list("%s" % ''.join(i.decode("utf-8"))))
