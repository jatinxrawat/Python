import random
a=random.randint(1,100)
def guessnum():

  count=0
  for i in range (0,100):
      num=int(input())
      if(a==num):
        count+=1
        print(f"Sucess in {count} timrs")

      elif(num>a):
        count+=1
        print("Too high")

      elif(num<a):
        count+=1
        print("Too low")


guessnum()

