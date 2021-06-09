from random import choice 

print( '''
hello welcome to rock paper scissors
we will now play 5 turns 
'''
)
print ('the rules of rock paper scissors are, rock beats scicors, \nsciccors beat paper and paper beats rock')

userchoice = input("which do u pick tyo play?\n") # make sure user doesn't put in something that's not an option
opt = ["rock","paper","scissors"]
compchoice = choice(opt)
print (compchoice)