#import libraries here

def main():
  a="AprilMay"
  b="JulyAugust"
  c="OctoberNovember"
  k=input("Enter name of the month [ex. June]: ")
  t=int(input("Enter the day [ex. 5]: "))
  if k=="March" and t>=20 or k=="June" and t<21 or k in a:
    print(f"{k} {t} is in Spring")
  elif k=="June" and t>=21 or k=="September" and t<22 or k in b:
    print(f"{k} {t} is in Summer")      
  elif k=="September" and t>=22 or k=="December" and t<21 or k in c:
    print(f"{k} {t} is in Fall")
  else: print(f"{k} {t} is in Winter")
  pass

if __name__ == "__main__":
  main()
