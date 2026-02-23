def make_acronym(string):
    words = string.split(" ")  # split sentence into words
    acronym = ""                # initialize empty string
    for word in words:
        acronym += word[0]      # take first letter of each word
    print(acronym.upper())      # print in uppercase

# Examples
make_acronym("New York")                 # NY
make_acronym("same stuff different day") # SSDD
make_acronym("Laugh out loud")           # LOL
make_acronym("don't over think stuff")   # DOTS
