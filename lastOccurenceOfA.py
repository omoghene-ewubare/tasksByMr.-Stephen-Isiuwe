#name= Last
#Author= Omoghene Ewubare
#Date= July 28 2024
#purpose=  assignmentAssingedToMeByMr. Stephen Isiuwe
#Function= To capitalize the first letter in a string.
#test= 



s=("Bananas are yellow.") 

#3 searches for the last occurrence of ”a” in the first word.

# Extract the first word

first_word = s.split()[0]

# Find the last occurrence of 'a' in the first word

last_occurance_a= first_word.rfind('a')

print ("The last occurrence of 'a' in the first word is at " + str(last_occurance_a) )
