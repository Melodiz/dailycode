start = '1'*77
while '111' in start:
    start = start.replace('111','2',1)
    start = start.replace('222','3',1)
    start = start.replace('333','1',1)

print(start)