fi = open('/tmp/String.txt')
s = fi.readline()
res = ""
for char in s:
    if char.isdigit():
        res += char
print(res)
fi.close()


with open('/tmp/String.txt') as f:
    s = f.read()
res = ""

for char in s:
    if char.isdigit():
        res += char
print(res)
