print("michal".upper())
print("JANA".lower())
print("$$$text$$$".strip("$").upper())
print("jana martina michal pavel".split(" "))
print("jana,martina,michal,pavel".split(","))

jmena = "jana,martina,michal,pavel".split(",")

print("$".join(jmena))
print(",".join(jmena))

text = "Jirka Pesik je nejhorsi lektor Pythonu"
new_text = text.replace("nejhorsi", "nejlepsi")

print(new_text)