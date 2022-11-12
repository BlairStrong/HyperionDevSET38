import spacy

def recommendations():
    #using the md(medium) model for the sentances below
    nlp_md = spacy.load("en_core_web_md")

    # defining the comparison sample:
    comparitor = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
    #generating the comparator model
    model_comparitor = nlp_md(comparitor)

    recommendations = {} # using a dict to keep the key/value pairs linked for sorting later
    # reading in the moves text file to a list
    with open("movies.txt", "r") as rm:  # rm acronym for read movies
        for line in rm:
            line = line.split(":") #creating a list to split movie and and movie description
            similarity_md = nlp_md(line[1]).similarity(model_comparitor) # calculation the similarty for each of the movie descriptions line by line
            recommendations[line[0]] = similarity_md # creatin dictionary entry
            print(line[0], similarity_md)

    #sorted function is sorting the value pairs of the keys in recommendations by reerse order, so largest first.
    print("Best in order of similarity:", sorted(recommendations, key=recommendations.get, reverse=True))

recommendations()
