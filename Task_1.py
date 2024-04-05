#import libraries here

def main():
  a="y"
  b="aeiou"
  k=input("Enter a letter of the alphabet: ")
  if k in b:
    print("Entered alphabet is a vowel!")
  elif k in a:
    print("Sometimes it is a vowel, and sometimes it is a consonant!")
  else: print("Entered alphabet is a consonant!")
  pass

if __name__ == "__main__":
  main()
