lstr = []
for path in ['1.txt', '2.txt', '3.txt']:
    with open(path, encoding= 'utf8') as f:
        lstr.append(f.read())
        lstr.append('\n')
        s_lstr = sorted(lstr)
with open('4.txt', 'a') as f:
    for s in s_lstr:
        f.write(s)




