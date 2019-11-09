# Most Common Words
dict1 = {}
maxW = 0
paragraph = paragraph.lower()
paragraph = re.sub("[^a-zA-Z0-9]", " ", paragraph)
for i in paragraph.split():
    if i not in dict1.keys():
        dict1[i] = 1
    else:
        dict1[i] = dict1.get(i) + 1
for i in range(len(banned)):
    if banned[i] in dict1.keys():
        dict1.pop(banned[i])

sorted_x = sorted(dict1.items(), key=lambda kv: kv[1])
return (sorted_x[-1][0])
