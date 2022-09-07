import random
import time

print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]


def find_all(sub,s):
    index_list = []
    index = s.find(sub)
    while index != -1:
        index_list.append(index)
        index=s.find(sub,index+1)

    if len(index_list) > 0:
        return index_list
    else:
        return -1        
        
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()


def guess_next_letter(pattern, used_letters=[], word_list=[]):
    global count
    global word
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: " + pattern + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        guess_next_letter(pattern, used_letters, word_list)


    elif guess in word:
        used_letters.extend([guess])
        index_list = find_all(guess,word)
        for index in index_list:
            index = word.find(guess)
        # 把找到的word重置为_
            word = word[:index] + "_" + word[index + 1:]
            pattern = pattern[:index] + guess + pattern[index + 1:]

    elif guess in used_letters:
        print("Try another letter.\n")

    else:
        count += 1

        if count < limit:
            time.sleep(1)
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        guess_next_letter(pattern, used_letters, word_list)


main()

guess_next_letter(display,already_guessed,words_to_guess)