import spacy
nlp_sm = spacy.load("en_core_web_sm")
nlp_md = spacy.load("en_core_web_md")

word1 = nlp_md("cat")
word2 = nlp_md("monkey")
word3 = nlp_md("banana")

print(word1.similarity(word2))
print(word1.similarity(word3))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp_md("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:

        #removing the tokens from self comparison to save computational time
        if token1 != token2:
            print(token1.text, token2.text, token1.similarity(token2))
            """
            Notes: the fruits are higher ranked together, the animals are higher ranked together, highest similarities are between 
            the fruits banana and apple."""



sentences = ["Where did my dog go?", "Hello, there is my car", "I've lost my car in my car", "I'd like my boat back", "I will name my dog diana"]

comparison_sentence = "Why is my cat on the car?"
model_sentence_sm = nlp_sm(comparison_sentence)
model_sentence_md = nlp_md(comparison_sentence)

for line in sentences:
    similarity_sm = nlp_sm(line).similarity(model_sentence_sm)
    similarity_md = nlp_md(line).similarity(model_sentence_md)
    print(line+" - ", similarity_sm, similarity_md)
    """ the nlp_sm function returns consistently lower similarities across the board to the nlp_md"""
