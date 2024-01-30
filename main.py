from art import logo
print(logo)

def cal(n1,n2):
  def add(n1, n2):
     return n1+n2
  def sub(n1, n2):  
    return n1-n2
  def mul(n1, n2):
    return n1*n2 
  def div(n1, n2):
    return n1/n2
  operations={
    "*":mul,
    "/":div,
    "+":add,
    "-":sub}
  for i in operations:
    print(i)
  a=input("pick an operation:")
  display=operations[a]
  print(display(n1,n2))
  b=input(f"continue with {display(n1,n2)} or restart")
  if b=="restart":
    restart()
  while  b=="yes":
    n1=display(n1,n2)
    n2=float(input("Enter Second no:"))
    cal(n1,n2)   
  else:
    return "THank YOU"
  
def restart():
  n1=float(input("Enter First no:"))
  n2=float(input("Enter Second no:"))
  cal(n1,n2)  
  
restart()