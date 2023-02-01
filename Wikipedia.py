
# IMPORTAR las Libreria de wikipedia
import wikipedia

text= input("Buscar:\n")
wikipedia.set_lang("es")
info= wikipedia.summary(text)
print("\nWikipedia: ",info)

result= wikipedia.search("Obama")
for i in result:
    print(i)

