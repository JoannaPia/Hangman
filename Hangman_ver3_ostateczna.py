import random

def draw_word(): # losuje słowo z listy słów
    words = ["Zagreb", "Warsaw", "Vilnius", "Baku‎", "Amsterdam", "Dublin", "Reykjavík‎", "Luksemburg", " Berlin", "Oslo",
     "Belfast‎", "Londyn", "Andora", "Belgrade", "Madryt", "Valetta", "Monako", "Bratislava","San Marino", "Berno", "Bucharest‎", "Edinburgh‎", "Budapest‎", "Podgorica‎", "Paris", "Moscow‎",
     "Monaco‎", "Minsk", "Madrid‎", "London‎", "Ljubljana‎", "Lisbon‎", "Kyiv‎", "Helsinki‎", "Gibraltar‎", "Prague", "Riga", "Rome‎", "City of San Marino‎", "Sarajevo‎", "Skopje‎", "Sofia‎",
     "Stockholm‎", "Tallinn", "Tirana", "Vienna", "Buenos Aires", "La Paz", "Brasilia", "Santiago", "Bogota", "Quito", "Georgetown", "Asuncion", "Lima", "Paramaribo", "Montevideo",
     "Caracas", "Nassau", "Bridgetown", "Belmopan", "Ottawa", "San Jose", "Havana", "Roseau", "Santo Domingo", "San Salvador", "Saint George's", "Guatemala City", "Port au Prince",
     "Tegucigalpa", "Kingston", "Mexico City", "Managua", "Panama City", "Basseterre", "Castries", "Port of Spain", "Washington", "Kabul", "Yerevan", "Manama", "Dhaka", "Thimphu",
     "Bandar Seri Begawan", "Phnom Penh", "Beijing", "Nicosia", "Tbilisi", "New Delhi", "Jakarta", "Tehran", "Baghdad", "Jerusalem", "Tokyo", "Amman", "Nur Sultan", "Kuwait", 
     "Bishkek", "Vientiane", "Beirut", "Kuala Lumpur", "Male", "Ulaanbaatar", "Pyongyang", "Kathmandu", "Muscat", "Islamabad", "Jerusalem", "Manila", "Doha", "Riyadh", "Seoul", 
     "Damascus", "Taipei", "Dushanbe", "Bangkok", "Ankara", "Ashgabat", "Tashkent", "Hanoi", "Sana", "Nairobi"]
    word = words[random.randint(0, len(words)) - 1]
    return word


def input_user(letters_entered): # wprowadzanie danych
    while True:
        user_input = input("Enter the letter: ")
            
        if user_input.upper() == "QUIT": # zakończenie po wpisaniu QUIT
            quit()
        elif len(user_input) == 1:
            if ((user_input.isalpha() or user_input == " ") and (user_input.upper() not in letters_entered)): # sprawdzenie czy wprowadzone dane to litery, upper nie ważne czy duża czy mała
                letters_entered.append(user_input.upper()) # jezeli dużo warunków to zamieniam na zmienne UWAGA 
                return user_input
            elif user_input.upper() in letters_entered:
                print("This letter has already been checked!")
                print("Give a new one!")
            else:
                print("Please enter a letter!")
        else:
            print("You must enter one letter!")

def correct_answer(word, letter, result): # wyświetlanie odgadniętych liter
    

    for i in range(len(word)):
        if word[i].lower() == letter.lower():
            result[i] = letter
    
    return result


def incorect_answer(lives): 
    if lives == 1:
        print("""
        +---+
        |   |
            |
            |
            |
            |
        =========""")
    
    elif lives == 2:
        print("""
        +---+
        |   |
        O   |
            |
            |
            |
        =========""")

    elif lives == 3:
        print("""
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========""")

    elif lives == 4:
        print("""
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========""")

    elif lives == 5:
        print("""
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========""")

    elif lives == 6:
        print(""""
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========""")

    elif lives == 7:
        print("""
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========""")

        print("You used up all your trials. The end of the game.")
        print("Do you want play again?")
        user_answer = ask_yes_no("Answer yes or no: ")
        print(user_answer)
        if user_answer == "yes":
            print("great")
            start_game()
        elif user_answer == "no":
            print("Bye")
        quit()

def play(word, lives):
    
    result = []
    letters_entered = []
    for i in range(len(word)):
        result.append("_")

    for letter in word:
        print("_ ", end = "")
    print("\n")

    while lives <= 7: ### nie robić sztywnie 7 żyć tylko pusta, żeby można było zmieniać LUB   
        if "_" in result:
            user_letter = input_user(letters_entered)
        
            if (user_letter.upper() in word) or (user_letter.lower() in word): # wyświetlanie liter duze i małe, żeby wszystko wzięło pod uwagę
                result = correct_answer(word, user_letter, result)
                print(*result, sep=" ")

            else:
                lives += 1
                incorect_answer(lives)
                print("List of checked letters: ")
                print(*letters_entered, sep=", ")
        else:
            print("Congratulations!!!")
            print("You have won!!!")
            quit()    



def quit():
    exit()

def start_game():
    print("""\n
                             Welcome to the game:
    \n\n""")

    print("""
                 _   _                                       
                | | | |                                     
                | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
                |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                | | | | (_| | | | | (_| | | | | | | (_| | | | | 
                \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                                    __/ |                    
                                    |___/  
    \n\n
                You have 7 chances to guess the word (there are double word), 
                            if you enter QUIT you will exit the game.
                              Remember you can use space and letter
                                         Good luck!""")
    word = draw_word()
    print(word)
    lives = 0
    play(word, lives)

def ask_yes_no(question): 

    response = None
    while response not in ("yes", "no"):
        response = input(question).lower()   #Czy chcesz zagrać ponownie
    return response 


def main():
    start_game()

if __name__ == "__main__":
    main()