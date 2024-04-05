#import libraries here

def main():
  a="bcdfghjklmnpqrstuvwxz"
  b="aeiou"
  k=input("Enter a letter of the alphabet: ")
  if k in a:
    print("Entered alphabet is a consonant!")
  elif k in b:
    print("Entered alphabet is a vowel!")
  else: print("Sometimes it is a vowel, and sometimes it is a consonant!") 
  pass

if __name__ == "__main__":
  main()
