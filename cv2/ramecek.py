# Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

# Zadej slovo: ahoj
# ********
# * ahoj *
# ********
# Nápověda: 8 * '*' == '********'

# Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr.

def oramuj(text):
    delka = len(text)
    delka = delka + 4;
    hvezdicky = delka * "*"
    print(hvezdicky)
    print(f"* {text} *")
    print(hvezdicky)

oramuj("Ahoj Nazdar")


#od lektora
def show_text(text):
    delka_textu = len(text)
    delimiter = f"**{delka_textu * '*'}**"
    print(delimiter)
    print(f"* {text} *")
    print(delimiter)
show_text("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
