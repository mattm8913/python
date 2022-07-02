def get_word(word_type):
    """Retrieves a word from the user."""
    if word_type.lower=='adjective':
        a_or_an='an'
    else:
        a_or_an='a' 
    return input('Enter a word that is {} {}: '.format(a_or_an, word_type))

def words_fill(words):
    """Fills in the story with words."""
    story="Jerry went to {0} in order to {1} on a {2} stick.".format(words[0],words[1],words[2])
    return story

def display_story(story):
    """Displays the story"""
    print()
    print('Here is the story you created.  Enjoy!')
    print()
    print(story)

def create_story():
    """Creates a story by getting input from the user and filling it in"""
    noun=get_word('noun')
    verb=get_word('verb')
    adjective=get_word('adjective')
    words=[noun,verb,adjective]

    story=words_fill(words)
    display_story(story)

create_story()
