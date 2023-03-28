import spacy

nlp = spacy.load("en_core_web_trf")

import en_core_web_trf
nlp= en_core_web_trf.load()

nlp = en_core_web_trf.load()

print("loaded")
commands = [
    "hey can you please open firefox",
    "please open chrome",
    "hey you please open opera",
    "hey you open opera",
    "you open terminal",
    "you open a new terminal",
    "hey please show me opera",
    "please search for 'docker image data'"
]


for command in commands:
    doc = nlp(command)
    verb = ""
    adj = ""
    noun = []
#     print([(w.text, w.pos_) for w in doc])
    for ent in doc:
        if ent.pos_ == "VERB":
            verb = ent.text
        if ent.pos_ == "NOUN":
            noun.append(ent.text)
        if ent.pos_ == "ADJ":
            adj = ent.text
    print(f"=>>> {verb} {adj} {noun}")
