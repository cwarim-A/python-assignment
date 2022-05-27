# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


file = open("C:/Users/hp/Desktop/Reading-Text-Files/story.txt","r")
content = file.read()
def read_file_content(content):
      content = file.read()
      return content

    
      print(content) 
    


 def count_words(content):
     counts = dict()
     text = content.split()
     for word in text:
     if word in counts:
     counts[word] +=1
     else:
     counts[word] =1
     return counts
     print(count_words)
