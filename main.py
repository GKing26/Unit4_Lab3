# Griffin King
# U4 L3
# Reversing a list


from StackClass import ArrayStack
from os import system
def cleaner(files):
  filterFile = ""
  for a in range(len(files)):
    if (65 <= ord(files[a]) <= 90) or (97 <= ord(files[a]) <= 122):
      filterFile += files[a]
    elif files[a] == " " or files[a] == "\n":
      try:
        if files[a+1] != " ":
          filterFile += " " + "-"
      except:
        pass
def main():
  reversedFile = ""
  stack = ArrayStack()
  with open("earnest.txt",'r') as files:
    filterFile = cleaner(files.read())
    
  for a in filterFile.split("-"):
    stack.push(a)
  for a in range(len(stack)):
    reversedFile += stack.pop()
  with open("reversed.txt","w") as files:
    files.write(reversedFile)
if __name__ == "__main__":
  system("clear")
  main()