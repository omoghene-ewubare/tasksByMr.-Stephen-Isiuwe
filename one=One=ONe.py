
#name= one=One=ONe
#Author= Omoghene Ewubare
#Date= July 28 2024
#purpose=  assignmentAssingedToMeByMr. Stephen Isiuwe
#Function= toMakeTheProgramRecognise"one,One,ONe"AsTheSameWord
#test= 



#(2) should treat ”one”, ”One”, and ”oNE” identically

#The String I am using

a=("One banana was brown, but one was green.")

#make all lower case

all_identical=(a.lower())

#count all the "one"'s to show they are all the same

print(all_identical.count('one'))
