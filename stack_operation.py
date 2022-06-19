l=[]
print("Enter Your Choice ")
while True:
  c=int(input('''
  1. Push Element
  2. Pop Element 
  3. Peek Element
  4. Display Elements
  5.Exit
  '''))

  if c==1:
    n=input("Enter the Element:- ");
    l.append(n)
    print(l)
  elif c==2:
    if len(l)==0:
      print("Empty stack")
    else:
      p=l.pop()
      print(p)
      print(l)

  elif c==3:
    if len(l)==0:
      print("Empty stack")
    else:
      print("Last stack value- ", l[-1])

  elif c==4:
    print("Display stack:- ", l)
  elif c==5:
    break;
  else:
    print("Invalid choice")
