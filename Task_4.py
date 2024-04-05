#import libraries here

def main():
  a=int(input("Enter the year [ex. 2021]: "))
  if a==2000 or (a-2000)%12==0:
    print(f"{a} is the year of the Dragon")
  elif a==2001 or (a-2001)%12==0:
    print(f"{a} is the year of the Snake")
  elif a==2002 or (a-2002)%12==0:
    print(f"{a} is the year of the Horse")
  elif a==2003 or (a-2003)%12==0:
    print(f"{a} is the year of the Sheep")
  elif a==2004 or (a-2004)%12==0:
    print(f"{a} is the year of the Monkey")
  elif a==2005 or (a-2005)%12==0:
    print(f"{a} is the year of the Rooster")
  elif a==2006 or (a-2006)%12==0:
    print(f"{a} is the year of the Dog")
  elif a==2007 or (a-2007)%12==0:
    print(f"{a} is the year of the Pig")
  elif a==2008 or (a-2008)%12==0:
    print(f"{a} is the year of the Rat")
  elif a==2009 or (a-2009)%12==0:
    print(f"{a} is the year of the Ox")
  elif a==2010 or (a-2010)%12==0:
    print(f"{a} is the year of the Tiger")
  elif a==2011 or (a-2011)%12==0:
    print(f"{a} is the year of the Hare")
  else: print("Invalid year!")
  pass

if __name__ == "__main__":
  main()
