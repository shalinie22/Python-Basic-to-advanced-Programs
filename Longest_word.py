# Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

def LongestWord(sen):

  # code goes here
  import re
  words = sen.split(" ")
  m = 0
  long_word = ""
  for wor in words:
    count = len(re.findall(r"[a-z0-9]",wor,flags = re.IGNORECASE))
    if m < count:
      m=count
      long_word = wor

  return long_word

# keep this function call here 
print(LongestWord(input()))