import multiprocessing
import os
import time

def functionThatPrintNumbers(numbers):
  for number in range(numbers):
    print("The number  is " + str(number))
    time.sleep(1)
  print("TE SEC PID IS " + str(os.getpid()) + " The parent PID is " + str(os.getppid()))

def main():
  print("The main Pid is " + str(os.getpid()) + " The Parent PID is " + str(os.getppid()))
  user_number = int(input("Please Enter A Number "))
  process = multiprocessing.Process(target=functionThatPrintNumbers, args=(user_number,))
  process.start()
  print("First Line")
  print("Second Line")
  print("Third Line")
  print("Fourth Line")
  print("Fifth Line")
  process.join()

if __name__ == "__main__":
  main()