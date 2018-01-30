handle = open('my_notes.txt')
word_dict = dict()
for line in handle:
    words = line.strip().split()
    for word in words:
        count = word_dict.get(word, 0) + 1
        word_dict[word] = count
new_list = list()
# for (k, v) in word_dict.items():
#     new_list.append((v,k))
# print([(v, k) for k, v in word_dict.items()])
lst = sorted([(v, k) for k, v in word_dict.items()], reverse=True)

for v, k in lst[:10]:
    print(k, v)
