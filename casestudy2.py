import random
def game():
    w= ["internet" , "python" , "programming" , "coding" , "tiger" ,"lion" ,"animal" , "book" , "house" , "study"]
    word = random.choice(w)
    s= ''.join(random.sample(word, len(word)))
    a  = 5
    print("Unscramble the word:", s)
    while a > 0:
        g = input("Enter your word: ")

        if g == word:
            print("Congratulation!! Correct")
            break
        else:
            a  -= 1
            print("Wrong guess!! Attempts left:", a)
    if a == 0:
        print("You lost!! The correct word was:", word)
while True:
    game()
    ans = input("Do you want to play again? (yes/no): ")
    if ans != "yes":
        print("Thank you for playing!!")
        break