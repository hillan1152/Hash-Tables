# Understand:
#   Purpose:
#       How many times does a word show up in a single string?
#   Rules:
#       Case = ignored
#       Output keys = lowercase
#       Split strings into words on any white space
#       ignore these: " : ; , . - + = / \ | [ ] { } ( ) * ^ &
#       If the input contains no ignored characters, return empty dictionary 

def word_count(s):
    # convert string to lower case
    s = s.lower()

    # split defines words and eliminates white space
    s = s.split()

    # define ignored characters
    ignored = ['"', ':', ';', ',', '.', '-', '+', '=','/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

    ignored_char = set(ignored)
    
    cache = dict()
    # iterate through list
    for word in s:
    # check to see if ignored is in word, replace with '' if it matches
        filtered = ''
        for char in word:
            if char not in ignored_char:
                filtered = filtered + char
        # check if word is in table, if it is add 1.
        if filtered in cache:
            cache[filtered] += 1
        # if not, make it = 1
        elif filtered != "":
            cache[filtered] = 1
    return cache
    



         
            



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))