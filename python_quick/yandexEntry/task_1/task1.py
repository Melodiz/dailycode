import json
import sys

file_name = input()
# file_name = "task_1/sample_1.json"
with open(file_name, 'r') as f:
    task = json.load(f)
    f.close()

res = {}
data = []

for line in sys.stdin:
    data.append(line.rstrip())

alf = set()  # containg aeuioy
alf.add('a')
alf.add('e')
alf.add('u')
alf.add('i')
alf.add('o')
alf.add('y')

for i in range(len(data)):
    row = data[i].split('_')
    if task[str(i + 1)] == "30":
        res[str(i + 1)] = sorted(row, reverse=True)
    elif task[str(i + 1)] == "20":
        row = [row[k] for k in range(len(row)) if len(row[k]) % 2 == 0]
        res[str(i + 1)] = sorted(row, reverse=True)
    else:
        temp = []
        for j in range(len(row)):
            count = 0
            was_set = set()
            for k in range(len(row[j])):
                if row[j][k] in alf and row[j][k] not in was_set:
                    count += 1
                    was_set.add(row[j][k])
                if count == 2:
                    temp.append(row[j])
                    break
        res[str(i + 1)] = sorted(temp, reverse=True)

output_file_name = "output.json"
with open(output_file_name, 'w') as f:
    json.dump(res, f)
    f.close()
