from symspellpy import SymSpell

symsp = SymSpell()

symsp.load_dictionary('Dict.txt',\
                      term_index=0, \
                      count_index=1, \
                      separator=' ')

para_1 = '''wherre is the love hehad dated forImuch of the past who couqdn'tread in sixthgrade and ins pired him'''
para_2 = """As far as I am abl to judg, after long attnding to the sbject, the condiions of lfe apear to act in two ways—directly on the whle organsaton or on certin parts alne and indirectly by afcting the reproducte sstem. Wit respct to te dirct action, we mst bea in mid tht in every cse, as Profesor Weismann hs latly insistd, and as I have inidently shwn in my wrk on "Variatin undr Domesticcation," thcere arae two factrs: namly, the natre of the orgnism and the natture of the condiions. The frmer sems to be much th mre importannt; foor nealy siimilar variations sometimes aris under, as far as we cn juddge, disimilar conditios; annd, on te oter hannd, disssimilar variatioons arise undder conditions which aappear to be nnearly uniiform. The efffects on tthe offspring arre ieither definnite or in definite. They maay be considdered as definnite whhen allc or neearly all thhe ofefspring off inadividuals exnposed tco ceertain conditionas duriing seveal ggenerations aree moodified in te saame maner."""
para_3 = """Cinderella came frm a grea family. She is the only daughter of an affluent and widowrr duke who has rewed to provide her witha stepmom and two stepsistrs. Cinderella’s mother died due to illness when she was stilll a younng girl, leawing her with a doll, faworite dress, and a pair of glasss slipppers."""


terms = symsp.lookup_compound(para_1,
max_edit_distance=2) 
print(terms[0].term)
terms = symsp.lookup_compound(para_2,
max_edit_distance=1)
print(terms[0].term)
terms = symsp.lookup_compound(para_3,
max_edit_distance=2)
print(terms[0].term)

