import random

def draw_hangman(lives):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[lives]

def play_again():
    while True:
        choice = input("Deseja jogar novamente? (s/n): ").lower()
        if choice == 's':
            return True
        elif choice == 'n':
            return False
        else:
            print("Opção inválida. Por favor, escolha 's' para sim ou 'n' para não.")

def play_hangman():
    words = ["python", "java", "sistemas"]
    lives = 6
    word = random.choice(words).lower()
    guessed_letters = []
    word_progress = ['_' for _ in range(len(word))]

    while True:
        print(draw_hangman(lives))
        print(' '.join(word_progress))
        print(f"Letras já digitadas: {' '.join(guessed_letters)}")
        guess = input("Digite uma letra: ").lower()

        if len(guess) != 1:
            print("Por favor, digite apenas uma letra.")
            continue

        if guess in guessed_letters:
            print("Você já digitou essa letra. Tente outra.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_progress[i] = guess

            if '_' not in word_progress:
                print("Parabéns! Você venceu!")
                break
        else:
            print("Letra errada.")
            lives -= 1
            if lives == 0:
                print(draw_hangman(lives))
                print(f"Você perdeu! A palavra era '{word}'.")
                break

    if play_again():
        play_hangman()
    else:
        print("Obrigado por jogar!")

play_hangman()