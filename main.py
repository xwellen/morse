import csv

d = dict()
with open("morse_russian.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["letter", "morse"])
    for item in reader:
        d.update({item["letter"]: item["morse"]})


def to_morse(s):
    res = ""
    for l in s.upper():
        resu = d.get(l)
        if resu:
            res += resu
    return res

mors = dict()

with open("clean_russian", "r") as file:
    for line in file:
        mors.update({to_morse(line): line})
x = open("results", "w")
with open("clean_russian", "r") as file:
    for line in file:
        s1 = to_morse(line)[::-1]
        res = mors.get(s1)
        if res:
            x.write(line[:-1] + "->" + res)

