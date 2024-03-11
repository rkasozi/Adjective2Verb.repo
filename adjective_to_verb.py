# Using a function to extract and transform a word
def adjective_to_verb(sentence, index):
  
  words = sentence.split()
  adjective = words[index]
  return adjective + "en"

# Example usage
print(adjective_to_verb('I need to make that bright', -1 ))
print(adjective_to_verb('It got dark as the sun set.', 2))