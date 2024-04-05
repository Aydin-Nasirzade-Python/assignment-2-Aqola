#import libraries here

def main():
  a=int(input("Enter the wavelength in nm: "))
  if 620<=a<750:
    print("The relevant color is Red")
  elif 590<=a<620:
    print("The relevant color is Orange")
  elif 570<=a<590:
    print("The relevant color is Yellow")
  elif 495<=a<570:
    print("The relevant color is Green")
  elif 450<=a<495:
    print("The relevant color is Blue")
  elif 380<=a<450:
    print("The relevant color is Violet")
  else: print("Invalid input!")
  pass

if __name__ == "__main__":
  main()
