#This is where I import the file I will be using
import random
f = open('words.txt')
words_list = f.read().splitlines()
f.close()

#for word in clean_list:
    #if word.isalpha() == False:
        #clean_list.remove(word)

def get_word():
    return random.choice(words_list).lower()

#This will be round 1 scores

p_1_score_r1 = 0
p_2_score_r1 = 0
p_3_score_r1 = 0

#This will be round 2 scores

p_1_score_r2 = 0
p_2_score_r2 = 0
p_3_score_r2 = 0

#This will be round 3 scores

p_1_score_r3 = 0
p_2_score_r3 = 0
p_3_score_r3 = 0

#This is where I sum up the scores for round 3
player_1 = p_1_score_r1 + p_1_score_r2
player_2 = p_2_score_r1 + p_2_score_r2
player_3 = p_3_score_r1 + p_3_score_r2

round_1 = False
round_2 = False
round_3 = False

players = ['p1', 'p2', 'p3']

word_underlist1 = []
word_underlist2 = []
word_underlist3 = []

#This is where I put my wheel segments

wheel_segments = ['bankrupt',150,200,250,300,'lose_a_turn',400,450,500,550,600,650,700,750,800,850,900]

word1 = get_word()
word2 = get_word()
word3 = get_word()


for char in word1:
    word_underlist1.append('_')

for char in word2:
    word_underlist2.append('_')

for char in word3:
    word_underlist3.append('_')

#This is where I create the function for my wheel

def go_spin():
    return random.choice(wheel_segments)

#This is where I can summon a spin
spin = go_spin()
spin2 = go_spin()
spin3 = go_spin()
spin4 = go_spin()
spin5 = go_spin()
spin6 = go_spin()
spin7 = go_spin()
spin8 = go_spin()
spin9 = go_spin()


#This is where I create what my consonants and vowels and rstlne

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
rstlne = ['r','s','t','l','n','e']

round_letters = set()
round_words = set()

while round_1 == False:
    #The first round needs its own loop.
    #The first consonant question needs its own loop.
    player_1_turn = True
    first_consonant_player_1 = False
    player_2_turn = True
    first_consonant_player_2 = False
    player_3_turn = True
    first_consonant_player_3 = False
    while first_consonant_player_1 == False:
        print('Round 1')
        print(word1)
        if spin == 'bankrupt':
            print('Bankrupt and you lost your turn Player 1')
            first_consonant_player_1 = True
            player_1_turn = False
            p_1_score_r1 = 0
        elif spin == 'lose_a_turn':
            print('You lose a turn Player 1')
            first_consonant_player_1 = True
            player_1_turn = False
        else:
            print(' '.join(word_underlist1))
            print('Player 1 you up. You are playing for $', spin)
            p1 = input('Guess a consonant: ').lower()
            if len(p1) == 1 and p1 in consonants and p1 not in round_letters:
                round_letters.add(p1)
                if p1 in word1:
                    for position in range(len(word1)):
                        if word1[position] == p1:
                            word_underlist1[position] = p1
                            p_1_score_r1 += spin
                            first_consonant_player_1 = True
                    print(' '.join(word_underlist1))
                    print('Good job! You currently have $', p_1_score_r1)   

                    #This is where I start the rest of the questions.
                    while player_1_turn == True:
                        #PLAYER1

                        p1 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p1 == 'consonant':
                            p1 = input('Guess a consonant: ').lower()
                            if len(p1) == 1 and p1 in consonants and p1 not in round_letters:
                                round_letters.add(p1)
                                if p1 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p1:
                                            word_underlist1[position] = p1
                                            p_1_score_r1 += spin
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            player_1 += p_1_score_r1
                                            first_consonant_player_1 = True
                                            player_1_turn = False
                                            first_consonant_player_2 =True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_1 = True
                                    print(' '.join(word_underlist1))
                                    print('Good job! You currently have $', p_1_score_r1)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_1_turn = False
                                    first_consonant_player_1 = True
                            else:
                                print('Its not a consonant, letter, or has already been chosen. Choose again.')

                        if p1 == 'vowel' and p_1_score_r1 >= 250:
                            p_1_score_r1 -= 250
                            p1 = input('Guess a vowel: ').lower()
                            if len(p1) == 1 and p1 in vowels and p1 not in round_letters:
                                round_letters.add(p1)
                                if p1 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p1:
                                            word_underlist1[position] = p1
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            player_1 += p_1_score_r1
                                            first_consonant_player_1 = True
                                            player_1_turn = False
                                            first_consonant_player_2 =True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_1 = True
                                    print(' '.join(word_underlist1))
                                    print('Good job! You currently have $', p_1_score_r1)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_1_turn = False
                                    first_consonant_player_1 = True
                            else:
                                print('Its not a vowel, letter, or has already been chosen. Choose again.')

                        if p1 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p1 = convert(input('Guess a word: ').lower())
                            word1 = convert(word1)
                            if p1 == word1 and p1 not in round_words:
                                print('You guessed right!', word1, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_1_score_r1)
                                round_words.add(p1)
                                player_1 += p_1_score_r1
                                first_consonant_player_1 = True
                                player_1_turn = False
                                first_consonant_player_2 =True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_1 = True
                            else:
                                print('That is not the full word or has already been guessed. You lost your turn.')
                                player_1_turn = False
                                first_consonant_player_1 = True
                        
                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_1 = True
                    player_1_turn = False
            else:
                print('That is not one letter and/or a consonant. Try again.')

    while first_consonant_player_2 == False:
        if spin2 == 'bankrupt':
            print('Bankrupt and you lost your turn Player 2')
            first_consonant_player_2 = True
            player_2_turn = False
            p_2_score_r1 = 0
        elif spin2 == 'lose_a_turn':
            print('You lose a turn Player 2')
            first_consonant_player_2 = True
            player_2_turn = False
        else:
            print(' '.join(word_underlist1))
            print('Player 2 you up. You are playing for $', spin2)
            p2 = input('Guess a consonant: ').lower()
            if len(p2) == 1 and p2 in consonants and p2 not in round_letters:
                round_letters.add(p2)
                if p2 in word1:
                    for position in range(len(word1)):
                        if word1[position] == p2:
                            word_underlist1[position] = p2
                            p_2_score_r1 += spin2
                            first_consonant_player_2 = True
                    print(' '.join(word_underlist1))
                    print('Good job! You currently have $', p_2_score_r1)     

                    #This is where I start the rest of the questions.
                    while player_2_turn == True:
                        #PLAYER2

                        p2 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p2 == 'consonant':
                            p2 = input('Guess a consonant: ').lower()
                            if len(p2) == 1 and p2 in consonants and p2 not in round_letters:
                                round_letters.add(p2)
                                if p2 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p2:
                                            word_underlist1[position] = p2
                                            p_2_score_r1 += spin2
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            player_2 += p_2_score_r1
                                            first_consonant_player_2 = True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_1 = True
                                    print(' '.join(word_underlist1))
                                    print('Good job! You currently have $', p_2_score_r1)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_2_turn = False
                                    first_consonant_player_2 = True
                            else:
                                print('Its not a consonant, letter, or has already been chosen. Choose again.')

                        if p2 == 'vowel' and p_2_score_r1 >= 250:
                            p_2_score_r1 -= 250
                            p2 = input('Guess a vowel: ').lower()
                            if len(p2) == 1 and p2 in vowels and p2 not in round_letters:
                                round_letters.add(p2)
                                if p2 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p2:
                                            word_underlist1[position] = p2
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            player_2 += p_2_score_r1
                                            first_consonant_player_2 = True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_1 = True
                                    print(' '.join(word_underlist1))
                                    print('Good job! You currently have $', p_2_score_r1)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_2_turn = False
                                    first_consonant_player_2 = True
                            else:
                                print('Its not a vowel, letter, or has already been chosen. Choose again.')

                        if p2 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p2 = convert(input('Guess a word: ').lower())
                            word1 = convert(word1)
                            if p2 == word1 and p2 not in round_words:
                                print('You guessed right!', word1, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_2_score_r1)
                                round_words.add(p2)
                                player_2 += p_2_score_r1
                                first_consonant_player_2 = True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_1 = True
                            else:
                                print('That is not the full word or has already been guessed. You lost your turn.')
                                player_2_turn = False
                                first_consonant_player_2 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_2 = True
                    player_2_turn = False
            else:
                print('That is not one letter and/or a consonant. Try again.')

    while first_consonant_player_3 == False:
        if spin3 == 'bankrupt':
            print('Bankrupt and you lost your turn Player 3')
            first_consonant_player_3 = True
            player_3_turn = False
            p_3_score_r1 = 0
        elif spin3 == 'lose_a_turn':
            print('You lose a turn Player 3')
            first_consonant_player_3 = True
            player_3_turn = False
        else:
            print(' '.join(word_underlist1))
            print('Player 3 you up. You are playing for $', spin3)
            p3 = input('Guess a consonant: ').lower()
            if len(p3) == 1 and p3 in consonants and p3 not in round_letters:
                p_3_score_r1 += spin3
                if p3 in word1:
                    for position in range(len(word1)):
                        if word1[position] == p3:
                            word_underlist1[position] = p3
                            round_letters.add(p3)
                            first_consonant_player_3 = True
                    print(' '.join(word_underlist1))
                    print('Good job! You currently have $', p_3_score_r1)     

                    #This is where I start the rest of the questions.
                    while player_3_turn == True:
                        #PLAYER3

                        p3 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p3 == 'consonant':
                            p3 = input('Guess a consonant: ').lower()
                            if len(p3) == 1 and p3 in consonants and p3 not in round_letters:
                                round_letters.add(p3)
                                if p3 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p3:
                                            word_underlist1[position] = p3
                                            p_3_score_r1 += spin3
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            player_3 += p_3_score_r1
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_1 = True
                                    print(' '.join(word_underlist1))
                                    print('Good job! You currently have $', p_3_score_r1)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_3_turn = False
                                    first_consonant_player_3 = True
                            else:
                                print('Its not a consonant, letter, or has already been chosen. Choose again.')

                        if p3 == 'vowel' and p_3_score_r1 >= 250:
                            p_3_score_r1 -= 250
                            p3 = input('Guess a vowel: ').lower()
                            if len(p3) == 1 and p3 in vowels and p3 not in round_letters:
                                round_letters.add(p3)
                                if p3 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p3:
                                            word_underlist1[position] = p3
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            player_3 += p_3_score_r1
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_1 = True
                                    print(' '.join(word_underlist1))
                                    print('Good job! You currently have $', p_3_score_r1)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_3_turn = False
                                    first_consonant_player_3 = True
                            else:
                                print('Its not a vowel, letter, or has already been chosen. Choose again.')

                        if p3 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p3 = convert(input('Guess a word: ').lower())
                            word1 = convert(word1)
                            if p3 == word1 and p3 not in round_words:
                                print('You guessed right!', word1, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_3_score_r1)
                                round_words.add(p3)
                                player_3 += p_3_score_r1
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_1 = True
                            else:
                                print('That is not the full word or has already been guessed. You lost your turn.')
                                player_3_turn = False
                                first_consonant_player_3 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_3 = True
                    player_3_turn = False
            else:
                print('That is not one letter and/or a consonant. Try again.')

round_letters= set()
round_words = set()

while round_2 == False:
    #The first round needs its own loop.
    #The first consonant question needs its own loop.
    player_1_turn = True
    first_consonant_player_1 = False
    player_2_turn = True
    first_consonant_player_2 = False
    player_3_turn = True
    first_consonant_player_3 = False
    while first_consonant_player_1 == False:
        print('Round 2')
        print(word2)
        if spin4 == 'bankrupt':
            print('Bankrupt and you lost your turn Player 1')
            first_consonant_player_1 = True
            player_1_turn = False
            p_1_score_r2 = 0
        elif spin4 == 'lose_a_turn':
            print('You lose a turn Player 1')
            first_consonant_player_1 = True
            player_1_turn = False
        else:
            print(' '.join(word_underlist2))
            print('Player 1 you up. You are playing for $', spin4)
            p1 = input('Guess a consonant: ').lower()
            if len(p1) == 1 and p1 in consonants and p1 not in round_letters:
                round_letters.add(p1)
                if p1 in word2:
                    for position in range(len(word2)):
                        if word2[position] == p1:
                            word_underlist2[position] = p1
                            p_1_score_r2 += spin4
                            first_consonant_player_1 = True
                    print(' '.join(word_underlist2))
                    print('Good job! You currently have $', p_1_score_r2)     

                    #This is where I start the rest of the questions.
                    while player_1_turn == True:
                        #PLAYER1

                        p1 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p1 == 'consonant':
                            p1 = input('Guess a consonant: ').lower()
                            if len(p1) == 1 and p1 in consonants and p1 not in round_letters:
                                round_letters.add(p1)
                                if p1 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p1:
                                            word_underlist2[position] = p1
                                            p_1_score_r2 += spin4
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            player_1 += p_1_score_r2
                                            first_consonant_player_1 = True
                                            player_1_turn = False
                                            first_consonant_player_2 =True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_2 = True
                                    print(' '.join(word_underlist2))
                                    print('Good job! You currently have $', p_1_score_r2)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_1_turn = False
                                    first_consonant_player_1 = True
                            else:
                                print('Its not a consonant, letter, or has already been chosen. Choose again.')

                        if p1 == 'vowel' and p_1_score_r2 >= 250:
                            p_1_score_r2 -= 250
                            p1 = input('Guess a vowel: ').lower()
                            if len(p1) == 1 and p1 in vowels and p1 not in round_letters:
                                round_letters.add(p1)
                                if p1 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p1:
                                            word_underlist2[position] = p1
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            player_1 += p_1_score_r2
                                            first_consonant_player_1 = True
                                            player_1_turn = False
                                            first_consonant_player_2 =True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_2 = True
                                    print(' '.join(word_underlist2))
                                    print('Good job! You currently have $', p_1_score_r2)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_1_turn = False
                                    first_consonant_player_1 = True
                            else:
                                print('Its not a vowel, letter, or has already been chosen. Choose again.')

                        if p1 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p1 = convert(input('Guess a word: ').lower())
                            word2 = convert(word2)
                            if p1 == word2 and p1 not in round_words:
                                print('You guessed right!', word2, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_1_score_r2)
                                round_words.add(p1)
                                player_1 += p_1_score_r2
                                first_consonant_player_1 = True
                                player_1_turn = False
                                first_consonant_player_2 =True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_2 = True
                            else:
                                print('That is not the full word or has already been guessed. You lost your turn.')
                                player_1_turn = False
                                first_consonant_player_1 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_1 = True
                    player_1_turn = False
            else:
                print('That is not one letter and/or a consonant. Try again.')

    while first_consonant_player_2 == False:
        if spin5 == 'bankrupt':
            print('Bankrupt and you lost your turn Player 2')
            first_consonant_player_2 = True
            player_2_turn = False
            p_2_score_r2 = 0
        elif spin5 == 'lose_a_turn':
            print('You lose a turn Player 2')
            first_consonant_player_2 = True
            player_2_turn = False
        else:
            print(' '.join(word_underlist2))
            print('Player 2 you up. You are playing for $', spin5)
            p2 = input('Guess a consonant: ').lower()
            if len(p2) == 1 and p2 in consonants and p2 not in round_letters:
                round_letters.add(p2)
                if p2 in word2:
                    for position in range(len(word2)):
                        if word2[position] == p2:
                            word_underlist2[position] = p2
                            p_2_score_r2 += spin5
                            first_consonant_player_2 = True
                    print(' '.join(word_underlist2))
                    print('Good job! You currently have $', p_2_score_r2)     

                    #This is where I start the rest of the questions.
                    while player_2_turn == True:
                        #PLAYER2

                        p2 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p2 == 'consonant':
                            p2 = input('Guess a consonant: ').lower()
                            if len(p2) == 1 and p2 in consonants and p2 not in round_letters:
                                round_letters.add(p2)
                                if p2 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p2:
                                            word_underlist2[position] = p2
                                            p_2_score_r2 += spin5
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            player_2 += p_2_score_r2
                                            first_consonant_player_2 = True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_2 = True
                                    print(' '.join(word_underlist2))
                                    print('Good job! You currently have $', p_2_score_r2)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_2_turn = False
                                    first_consonant_player_2 = True
                            else:
                                print('Its not a consonant, letter, or has already been chosen. Choose again.')

                        if p2 == 'vowel' and p_2_score_r2 >= 250:
                            p_2_score_r2 -= 250
                            p2 = input('Guess a vowel: ').lower()
                            if len(p2) == 1 and p2 in vowels and p2 not in round_letters:
                                round_letters.add(p2)
                                if p2 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p2:
                                            word_underlist2[position] = p2
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            player_2 += p_2_score_r2
                                            first_consonant_player_2 = True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_2 = True
                                    print(' '.join(word_underlist2))
                                    print('Good job! You currently have $', p_2_score_r2)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_2_turn = False
                                    first_consonant_player_2 = True
                            else:
                                print('Its not a vowel, letter, or has already been chosen. Choose again.')

                        if p2 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p2 = convert(input('Guess a word: ').lower())
                            word2 = convert(word2)
                            if p2 == word2 and p2 not in round_words:
                                print('You guessed right!', word2, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_2_score_r2)
                                round_words.add(p2)
                                player_2 += p_2_score_r2
                                first_consonant_player_2 = True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_2 = True
                            else:
                                print('That is not the full word or has already been guessed. You lost your turn.')
                                player_2_turn = False
                                first_consonant_player_2 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_2 = True
                    player_2_turn = False
            else:
                print('That is not one letter and/or a consonant. Try again.')

    while first_consonant_player_3 == False:
        if spin6 == 'bankrupt':
            print('Bankrupt and you lost your turn Player 3')
            first_consonant_player_3 = True
            player_3_turn = False
            p_3_score_r2 = 0
        elif spin6 == 'lose_a_turn':
            print('You lose a turn Player 3')
            first_consonant_player_3 = True
            player_3_turn = False
        else:
            print(' '.join(word_underlist2))
            print('Player 3 you up. You are playing for $', spin6)
            p3 = input('Guess a consonant: ').lower()
            if len(p3) == 1 and p3 in consonants and p3 not in round_letters:
                round_letters.add(p3)
                if p3 in word2:
                    for position in range(len(word2)):
                        if word2[position] == p3:
                            word_underlist2[position] = p3
                            p_3_score_r2 += spin6
                            first_consonant_player_3 = True
                    print(' '.join(word_underlist2))
                    print('Good job! You currently have $', p_3_score_r1)     

                    #This is where I start the rest of the questions.
                    while player_3_turn == True:
                        #PLAYER3

                        p3 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p3 == 'consonant':
                            p3 = input('Guess a consonant: ').lower()
                            if len(p3) == 1 and p3 in consonants and p3 not in round_letters:
                                round_letters.add(p3)
                                if p3 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p3:
                                            word_underlist2[position] = p3
                                            p_3_score_r2 += spin6
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            player_3 += p_3_score_r2
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_2 = True
                                    print(' '.join(word_underlist2))
                                    print('Good job! You currently have $', p_3_score_r2)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_3_turn = False
                                    first_consonant_player_3 = True
                            else:
                                print('Its not a consonant, letter, or has already been chosen. Choose again.')

                        if p3 == 'vowel' and p_3_score_r2 >= 250:
                            p_3_score_r2 -= 250
                            p3 = input('Guess a vowel: ').lower()
                            if len(p3) == 1 and p3 in vowels and p3 not in round_letters:
                                round_letters.add(p3)
                                if p3 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p3:
                                            word_underlist2[position] = p3
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            player_3 += p_3_score_r2
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_2 = True
                                    print(' '.join(word_underlist2))
                                    print('Good job! You currently have $', p_3_score_r2)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_3_turn = False
                                    first_consonant_player_3 = True
                            else:
                                print('Its not a vowel, letter, or has already been chosen. Choose again.')

                        if p3 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p3 = convert(input('Guess a word: ').lower())
                            word2 = convert(word2)
                            if p3 == word2 and p3 not in round_words:
                                print('You guessed right!', word2, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_3_score_r2)
                                round_words.add(p3)
                                player_3 += p_3_score_r2
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_2 = True
                            else:
                                print('That is not the full word or has already been guessed. You lost your turn.')
                                player_3_turn = False
                                first_consonant_player_3 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_3 = True
                    player_3_turn = False
            else:
                print('That is not one letter and/or a consonant. Try again.')

round_letters = set()
round_words = set()

#This is round 3
#Here I add the letters "R","S","T", "L", "N","E" if the randomly generated word has them.

#Here I code what player moves on
winner = max(player_1,player_2,player_3)
spin7

if player_1 == winner:
    print('========================================================================================================================')
    print(f'Player 1 with bank amount: $ {player_1} is going to Round 3. You cant make mistakes in your guesses for the final round.')
    print('========================================================================================================================')

elif player_2 == winner:
    print('========================================================================================================================')
    print(f'Player 2 with bank amount: $ {player_2} is going to Round 3. You cant make mistakes in your guesses for the final round.')
    print('========================================================================================================================')
elif player_3 == winner:
    print('========================================================================================================================')
    print(f'Player 3 with bank amount: $ {player_3} is going to Round 3. You cant make mistakes in your guesses for the final round.')
    print('========================================================================================================================')

print('Round 3')
print('Here is your word after revealing R-S-T-L-N-E:')

print(word3)
for letter in rstlne:
    if letter in word3:
        for position in range(len(word3)):
            if word3[position] == letter:
                word_underlist3[position] = letter
print(' '.join(word_underlist3))


#This is for the first consonant guess

winner_consonant1 = input("Guess your first consonant (Don't make a mistake or you will lose your turn):")
if len(winner_consonant1) == 1 and winner_consonant1 in consonants and winner_consonant1 not in round_letters:
    round_letters.add(winner_consonant1)
    if winner_consonant1 in word3:
        for position in range(len(word3)):
            if word3[position] == winner_consonant1:
                word_underlist3[position] = winner_consonant1
                print(f'Good job!')
                print(' '.join(word_underlist3))
                if '_' not in word_underlist3:
                    print(f'You now won! You made a total of: $ {winner} and you won a trip to Hawaii!')
                    print(' '.join(word_underlist3))
    else:
        print('That is not a consonant or not in the word.')
else:
    print('That is either not a consonant, a letter, or you already guessed it. You lost your turn')

#This is for the second consonant guess

winner_consonant2 = input("Guess your second consonant (Don't make a mistake or you will lose your turn):")
if len(winner_consonant2) == 1 and winner_consonant2 in consonants and winner_consonant2 not in round_letters:
    round_letters.add(winner_consonant2)
    if winner_consonant2 in word3:
        for position in range(len(word3)):
            if word3[position] == winner_consonant2:
                word_underlist3[position] = winner_consonant2
                print(f'Good job!')
                print(' '.join(word_underlist3))
                if '_' not in word_underlist3:
                    print(f'You now won! You made a total of: $ {winner} and you won a trip to Hawaii!')
                    print(' '.join(word_underlist3))
    else:
        print('That is not a consonant or not in the word')
else:
    print('That is either not a consonant, a letter, or you already guessed it. You lost your turn')

#This is for the third consonant guess

winner_consonant3 = input("Guess your third consonant (Don't make a mistake or you will lose your turn):")
if len(winner_consonant3) == 1 and winner_consonant3 in consonants and winner_consonant3 not in round_letters:
    round_letters.add(winner_consonant3)
    if winner_consonant3 in word3:
        for position in range(len(word3)):
            if word3[position] == winner_consonant3:
                word_underlist3[position] = winner_consonant3
                print(f'Good job!')
                print(' '.join(word_underlist3))
                if '_' not in word_underlist3:
                    print(f'You now won! You made a total of: $ {winner} and you won a trip to Hawaii!')
                    print(' '.join(word_underlist3))
    else:
        print('That is not a consonant or not in the word')
else:
    print('That is either not a consonant, a letter, or you already guessed it. You lost your turn')

#This is for the vowel guess

winner_vowel = input("Guess your vowel (Don't make a mistake or you will lose your turn):")
if len(winner_vowel) == 1 and winner_vowel in vowels and winner_vowel not in round_letters:
    round_letters.add(winner_vowel)
    if winner_vowel in word3:
        for position in range(len(word3)):
            if word3[position] == winner_vowel:
                word_underlist3[position] = winner_vowel
                if '_' not in word_underlist3:
                    print(f'You now won! You made a total of: $ {winner} and you won a trip to Hawaii!')
                    print(' '.join(word_underlist3))
                else:
                    print(f'Good job! However, you did not finish the word, so you leave the game with a total of: $ {winner}')
                    print(' '.join(word_underlist3))

    else:
        print(f'That is not a consonant or not in the word, you finished the game with: $ {winner} and unfortunately no trip to Hawaii')
else:
    print(f'That is either not a consonant, a letter, or you already guessed it. You finished the game with: $ {winner} and unfortunately no trip to Hawaii')