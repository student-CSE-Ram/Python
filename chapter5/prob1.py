# make a dictionary and put some english words in it and hindi words as their value and ask the user to give some input of the whose hindi they want to know

words = {
   "Help":"Sahayata",
   "Fan":"Pankha",
   "Chair":"Kursi",
   "Shop":"Dukaan" 
}

word = input("Enter the word whose hindi do you  want to know :")

print(words[word])

d = {}

friends = input("Enter friends name :")
lang = input("Enter language name :")

d.update({friends:lang})
friends = input("Enter friends name :")
lang = input("Enter language name :")

d.update({friends:lang})
friends = input("Enter friends name :")
lang = input("Enter language name :")

d.update({friends:lang})
friends = input("Enter friends name :")
lang = input("Enter language name :")

d.update({friends:lang})

print(d)