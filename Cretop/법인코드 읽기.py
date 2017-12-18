#-*- coding: utf-8 -*-
f = open('파클_법인번호.txt','r')
c_number = []
while True:
    line = f.readline()
    if not line: break
    if not line == '':c_number.append(line[:-1])
del c_number[0]

# print(c_number)
# print(len(c_number))
f.close()
