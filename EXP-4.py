my_strings ="we are better  than anything in the universe"

sentences = [sentences.lower() for sentences in my_strings.split()]

sentences.sort()


print("The sorted sentences are:")
for sentence in sentences:
 print(sentence)
