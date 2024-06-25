import random
words=["apple" ,"banana" , "mango" , "strawberry",  
"orange", "grape" , "pineapple ", "apricot ", "lemon" , "coconut ","watermelon ",
"cherry"," papaya","berry" , "peach", "lychee", "muskmelon"]
target=random.choice(words)
# print(target)
Answer = ['_'] * len(target)

while '_' in Answer:
    guess = input("please enter the select char:")
    if guess in target:
        for i in range(len(target)):
            if target[i] == guess:
                Answer[i] = guess
        print(Answer)
    else:
        print("The guessed character is not in the word.")
