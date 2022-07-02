def get_noun():
    """Retrieves a noun from the user."""
    noun=input('Enter a noun: ')
    return noun
def get_verb():
    """Retrieves a verb from the user."""
    verb=input('Enter a verb: ')
    return verb
def get_adj():
    """Retrieves an adjective from the user."""
    adj=input('Enter an adjective: ')
    return adj
def get_input():
    """Retrieves all three from the user using other functions."""
    noun=get_noun()
    verb=get_verb()
    adj=get_adj()
    words=[noun,verb,adj]
    return words
def words_fill(words):
    """Fills in the story with words."""
    story="Jerry went to {0} in order to {1} on a {2} stick.".format(words[0],words[1],words[2])
    return story

words=get_input()
story=words_fill(words)
print(story)
