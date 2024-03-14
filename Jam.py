import jamspell
# Create a corrector
corrector = jamspell.TSpellCorrector()

# Load Language model - 
# argument is a downloaded model file path
corrector.LoadLangModel('Downloads/en_model.bin')

# To fix text automatically run FixFragment:
print(corrector.FixFragment('I am the begt spell cherken!'))

# To get a list of possible candidates 
# pass a splitted sentence, and a word position
print(corrector.GetCandidates(['i', 'am', 'the', 'begt', 'spell', 'cherken'], 3))

print(corrector.GetCandidates(['i', 'am', 'the', 'begt', 'spell', 'cherken'], 5))
