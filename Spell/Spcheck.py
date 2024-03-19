from spellchecker import SpellChecker
 
spell = SpellChecker()

# find those words that may be misspelled
inp1 = 'thiz iz 3rror'

#Split the string
mis1 = inp1.split()
ot1 = []

for word in mis1:
    # Get the one `most likely` answer
    # ot1.append(spell.correction(word))
    # print(spell.correction(word))
 
    # Get a list of `likely` options
    print(spell.candidates(word))


print(f'final {' '.join(ot1)}')
#print (spell.candidates(inp1))
