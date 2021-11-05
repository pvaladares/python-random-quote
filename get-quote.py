import random

def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  for i in range (0, 2): #  Print out more than one quote at a time
    rnd = random.randint(0,last)
    print(quotes[rnd], end="") # Remove that extra line (called a newline) when printing

if __name__== "__main__":
  primary()
