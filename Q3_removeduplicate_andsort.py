
def remove_dulpicate_sort(sentence):
  words = sentence.split()
  unique_words = set(words)
  sorted_words = sorted(list(unique_words))
  return " ".join(sorted_words)

sentence = input("enter a sentence :")
result = remove_dulpicate_sort(sentence)
print(result)
