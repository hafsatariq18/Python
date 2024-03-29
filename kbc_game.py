print("Let's play Kaun Banega Crorepati","\n")
questions=["Which IPL team has never won any IPL season?","1.CSK","2.RCB","3.MI","4.RR",2],["What is the name of largest ocean in the world?","1.Indian Ocean","2.Arctic Ocean","3.Pacific Ocean","4.Atlantic Ocean",3],["What is the national sport of India?","1.Cricket","2.Hockey","3.Football","4.Kabaddi",2]

price_money=0
for question in questions:
  print(question[0])
  print(question[1],question[2],question[3],question[4])
  ans=input("Enter correct option:")
  if ans==str(question[5]):
     price_money=price_money+5000
     print("Congratulations!","You won Rs",price_money,"\n")
  else:
    print("Game Over!","Total amount is",price_money)
    break