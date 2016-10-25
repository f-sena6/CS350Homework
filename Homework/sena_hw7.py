global responses, respones2

class Talker:

    def __init__(self, n, v): #constructor; initialize
        self.name = n  #self is the object
        self.vocab = v #vocab

    def getname(self):
        return self.name

    def getvocab(self, text):
      v = []
      z = [] 

      for i in text.split(): #Seperates each word in text
       v.append(i) #Appends each word in the text


      for i in self.vocab: #Each sentence in responses
       keyword = 0 #Resets keyword every loop

       for j in v: #Searches for keyword
         if j in i:
          keyword +=1

       z.append(keyword)#Appends the value of keyword (occurences)
      return self.vocab[z.index(max(z))] #Finds the largest keyword value, then uses the index of that value to return a response


def main():
    
     
    responses = ['I want to build the wall', 'But we have some bad hombres here', 'We need the wall', 'No puppet. You are the puppet', 'One of my first acts will be to get all of the drug lords.', 'We are getting the drugs, they are getting the cash', 'They are coming in illegally', 'Drugs are pouring in through the border', 'They have been deported', 'We are a country of laws']

    responses2 = ['I find that just astonishing', 'We will not have open borders', 'Well, that is because he would rather have a puppet as president of the United States', 'I dont want to be sending families away from children', 'We are both a nation of immigrants and we are a nation of laws and that we can act accordingly', 'I am introducing comprehensive immigration reform within the first 100 days with a path to citizenship', 'It is pretty clear you wont admit that the Russians have engaged in cyber attacks against the US.', 'I find that deeply disturbing', 'I am not quoting myself', 'We have tried that']


    while True:
      text = raw_input("Please ask Hilary and Donald a Question: ")
      donald = Talker('Donald Trump', responses) #name is donald, vocab is responses (or array)
      clinton = Talker('Hilary Clinton', responses2) #name is clinton, vocab is responses
      print "\n"
      print donald.getname(), "responds, ", donald.getvocab(text)
      print clinton.getname(),"responds, ", clinton.getvocab(text)
      print "\n"

      ask = raw_input("Would you like to ask another question? Please type yes or no: ")
      yes = hash('yes')
      no = hash('no')

      if hash(ask) == yes:
       print "Ask another question.\n"

      elif hash(ask) == no:
       print "Thank you for your time today. Good luck to the both of you.\n"
       break
      else:
       print "This is not an answer. Please try again. \n"
       break
    

if __name__ == '__main__':
    main()




"""


            
else:
  l = (hash(text) % len(self.vocab))
  return self.vocab[l]




"""

