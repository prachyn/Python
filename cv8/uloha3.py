with open("praha.txt", mode="r", encoding="utf-8") as file:
    lines = file.readlines()

words_count = []
for line in lines:
    words_count.append(len(line.split())) # do listu words_count přidám délku řádku, což je list, protože daný řádek je splitnut mezerou, což takto rozdělíte na jednotlivá slova

total_words_count = sum(words_count)
print(words_count, total_words_count)