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
player_1_sum = p_1_score_r1 + p_1_score_r2
player_2_sum = p_2_score_r1 + p_2_score_r2
player_3_sum = p_3_score_r1 + p_3_score_r2

round_1 = False
round_2 = False
round_3 = False

players = ['p1', 'p2', 'p3']

word_underlist1 = []
word_underlist2 = []
word_underlist3 = []

#This is where I put my wheel segments

wheel_segments = [50,100,100,100,100,100,150,200,200,200,200,250,300,300,300,350,400,400,500,600,700,800,900]

bankrupt = 50
lose_a_turn = 350

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
spin4 = go_spin() #Have to check to see if I use this one. If I do, then I'll keep it. If not, I will get rid of it.


#This is where I create what my consonants and vowels are

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
rstlne = ['r','s','t','l','n','e']

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
        round_1_spin = spin
        print('Round 1')
        if spin == bankrupt:
            print('Bankrupt, you lose a turn')
            first_consonant_player_1 = True
            player_1_turn = False
            p_1_score_r1 = 0
        elif spin == lose_a_turn:
            print('You lose a turn')
            first_consonant_player_1 = True
            player_1_turn = False
        else:
            print(' '.join(word_underlist1))
            print('Player 1 you up. You are playing for $', spin)
            p1 = input('Guess a consonant: ').lower()
            if len(p1) == 1 and p1 in consonants:
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
                            if len(p1) == 1 and p1 in consonants:
                                if p1 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p1:
                                            word_underlist1[position] = p1
                                            p_1_score_r1 += spin
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            p_2_score_r1 = 0
                                            p_3_score_r1 = 0
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

                        if p1 == 'vowel':
                            p_1_score_r1 -= spin
                            p1 = input('Guess a vowel: ').lower()
                            if len(p1) == 1 and p1 in vowels:
                                if p1 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p1:
                                            word_underlist1[position] = p1
                                            p_1_score_r1 -= 250
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            p_2_score_r1 = 0
                                            p_3_score_r1 = 0
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
                                print('Bad guess. You lost your turn')
                                player_1_turn = False
                                first_consonant_player_1 = True

                        if p1 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p1 = convert(input('Guess a word: ').lower())
                            word1 = convert(word1)
                            if p1 == word1:
                                print('You guessed right!', word1, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_1_score_r1)
                                p_2_score_r1 = 0
                                p_3_score_r1 = 0
                                first_consonant_player_1 = True
                                player_1_turn = False
                                first_consonant_player_2 =True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_1 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_1_turn = False
                                first_consonant_player_1 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_1 = True
                    player_1_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_1 = True
                player_1_turn = False

    while first_consonant_player_2 == False:
        round_1_spin = spin
        if spin == bankrupt:
            print('Bankrupt, you lose a turn')
            first_consonant_player_2 = True
            player_2_turn = False
            p_2_score_r1 = 0
        elif spin == lose_a_turn:
            print('You lose a turn')
            first_consonant_player_2 = True
            player_2_turn = False
        else:
            print(' '.join(word_underlist1))
            print('Player 2 you up. You are playing for $', spin)
            p2 = input('Guess a consonant: ').lower()
            if len(p2) == 1 and p2 in consonants:
                if p2 in word1:
                    for position in range(len(word1)):
                        if word1[position] == p2:
                            word_underlist1[position] = p2
                            p_2_score_r1 += spin
                            first_consonant_player_2 = True
                    print(' '.join(word_underlist1))
                    print('Good job! You currently have $', p_2_score_r1)     

                    #This is where I start the rest of the questions.
                    while player_2_turn == True:
                        #PLAYER2

                        p2 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p2 == 'consonant':
                            p2 = input('Guess a consonant: ').lower()
                            if len(p2) == 1 and p2 in consonants:
                                if p2 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p2:
                                            word_underlist1[position] = p2
                                            p_2_score_r1 += spin
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            p_1_score_r1 = 0
                                            p_3_score_r1 = 0
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

                        if p2 == 'vowel':
                            p_2_score_r1 -= spin
                            p2 = input('Guess a vowel: ').lower()
                            if len(p2) == 1 and p2 in vowels:
                                if p2 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p2:
                                            word_underlist1[position] = p2
                                            p_2_score_r1 -= 250
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            p_1_score_r1 = 0
                                            p_3_score_r1
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
                                print('Bad guess. You lost your turn')
                                player_2_turn = False
                                first_consonant_player_2 = True

                        if p2 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p2 = convert(input('Guess a word: ').lower())
                            word1 = convert(word1)
                            if p2 == word1:
                                print('You guessed right!', word1, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_2_score_r1)
                                p_1_score_r1 = 0
                                p_3_score_r1 = 0
                                first_consonant_player_2 = True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_1 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_2_turn = False
                                first_consonant_player_2 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_2 = True
                    player_2_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_2 = True
                player_2_turn = False

    while first_consonant_player_3 == False:
        round_1_spin = spin
        if spin == bankrupt:
            print('Bankrupt, you lose a turn')
            first_consonant_player_3 = True
            player_3_turn = False
            p_3_score_r1 = 0
        elif spin == lose_a_turn:
            print('You lose a turn')
            first_consonant_player_3 = True
            player_3_turn = False
        else:
            print(' '.join(word_underlist1))
            print('Player 3 you up. You are playing for $', spin)
            p3 = input('Guess a consonant: ').lower()
            if len(p3) == 1 and p3 in consonants:
                if p3 in word1:
                    for position in range(len(word1)):
                        if word1[position] == p3:
                            word_underlist1[position] = p3
                            p_3_score_r1 += spin
                            first_consonant_player_3 = True
                    print(' '.join(word_underlist1))
                    print('Good job! You currently have $', p_3_score_r1)     

                    #This is where I start the rest of the questions.
                    while player_3_turn == True:
                        #PLAYER3

                        p3 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p3 == 'consonant':
                            p3 = input('Guess a consonant: ').lower()
                            if len(p3) == 1 and p3 in consonants:
                                if p3 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p3:
                                            word_underlist1[position] = p3
                                            p_3_score_r1 += spin
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            p_1_score_r1 = 0
                                            p_2_score_r1 = 0
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_1 = True
                                    print(' '.join(word_underlist1))
                                    print('Good job! You currently have $', p_3_score_r1)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_3_turn = False
                                    first_consonant_player_3 = True

                        if p3 == 'vowel':
                            p_3_score_r1 -= spin
                            p3 = input('Guess a vowel: ').lower()
                            if len(p3) == 1 and p3 in vowels:
                                if p3 in word1:
                                    for position in range(len(word1)):
                                        if word1[position] == p3:
                                            word_underlist1[position] = p3
                                            p_3_score_r1 -= 250
                                        if '_' not in word_underlist1:
                                            print('You now won!')
                                            p_1_score_r1 = 0
                                            p_2_score_r1 = 0
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
                                print('Bad guess. You lost your turn')
                                player_3_turn = False
                                first_consonant_player_3 = True

                        if p3 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p3 = convert(input('Guess a word: ').lower())
                            word1 = convert(word1)
                            if p3 == word1:
                                print('You guessed right!', word1, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_3_score_r1)
                                p_1_score_r1 = 0
                                p_2_score_r1 = 0
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_1 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_3_turn = False
                                first_consonant_player_3 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_3 = True
                    player_3_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_3 = True
                player_3_turn = False

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
        round_2_spin = spin2
        print('Round 2')
        if spin == bankrupt:
            print('Bankrupt, you lose a turn')
            first_consonant_player_1 = True
            player_1_turn = False
            p_1_score_r2 = 0
        elif spin == lose_a_turn:
            print('You lose a turn')
            first_consonant_player_1 = True
            player_1_turn = False
        else:
            print(' '.join(word_underlist2))
            print('Player 1 you up. You are playing for $', spin)
            p1 = input('Guess a consonant: ').lower()
            if len(p1) == 1 and p1 in consonants:
                if p1 in word2:
                    for position in range(len(word2)):
                        if word2[position] == p1:
                            word_underlist2[position] = p1
                            p_1_score_r2 += spin
                            first_consonant_player_1 = True
                    print(' '.join(word_underlist2))
                    print('Good job! You currently have $', p_1_score_r2)     

                    #This is where I start the rest of the questions.
                    while player_1_turn == True:
                        #PLAYER1

                        p1 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p1 == 'consonant':
                            p1 = input('Guess a consonant: ').lower()
                            if len(p1) == 1 and p1 in consonants:
                                if p1 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p1:
                                            word_underlist2[position] = p1
                                            p_1_score_r2 += spin
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            p_2_score_r2 = 0
                                            p_3_score_r2 = 0
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

                        if p1 == 'vowel':
                            p_1_score_r2 -= spin
                            p1 = input('Guess a vowel: ').lower()
                            if len(p1) == 1 and p1 in vowels:
                                if p1 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p1:
                                            word_underlist2[position] = p1
                                            p_1_score_r2 -= 250
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            p_2_score_r2 = 0
                                            p_3_score_r2 = 0
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
                                print('Bad guess. You lost your turn')
                                player_1_turn = False
                                first_consonant_player_1 = True

                        if p1 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p1 = convert(input('Guess a word: ').lower())
                            word2 = convert(word2)
                            if p1 == word2:
                                print('You guessed right!', word2, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_1_score_r2)
                                p_2_score_r2 = 0
                                p_3_score_r2 = 0
                                first_consonant_player_1 = True
                                player_1_turn = False
                                first_consonant_player_2 =True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_2 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_1_turn = False
                                first_consonant_player_1 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_1 = True
                    player_1_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_1 = True
                player_1_turn = False

    while first_consonant_player_2 == False:
        round_2_spin = spin2
        if spin == bankrupt:
            print('Bankrupt, you lose a turn')
            first_consonant_player_2 = True
            player_2_turn = False
            p_2_score_r2 = 0
        elif spin == lose_a_turn:
            print('You lose a turn')
            first_consonant_player_2 = True
            player_2_turn = False
        else:
            print(' '.join(word_underlist2))
            print('Player 2 you up. You are playing for $', spin)
            p2 = input('Guess a consonant: ').lower()
            if len(p2) == 1 and p2 in consonants:
                if p2 in word2:
                    for position in range(len(word2)):
                        if word2[position] == p2:
                            word_underlist2[position] = p2
                            p_2_score_r2 += spin
                            first_consonant_player_2 = True
                    print(' '.join(word_underlist2))
                    print('Good job! You currently have $', p_2_score_r2)     

                    #This is where I start the rest of the questions.
                    while player_2_turn == True:
                        #PLAYER2

                        p2 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p2 == 'consonant':
                            p2 = input('Guess a consonant: ').lower()
                            if len(p2) == 1 and p2 in consonants:
                                if p2 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p2:
                                            word_underlist2[position] = p2
                                            p_2_score_r2 += spin
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            p_1_score_r2 = 0
                                            p_3_score_r2 = 0
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

                        if p2 == 'vowel':
                            p_2_score_r2 -= spin
                            p2 = input('Guess a vowel: ').lower()
                            if len(p2) == 1 and p2 in vowels:
                                if p2 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p2:
                                            word_underlist2[position] = p2
                                            p_2_score_r2 -= 250
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            p_1_score_r2 = 0
                                            p_3_score_r2
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
                                print('Bad guess. You lost your turn')
                                player_2_turn = False
                                first_consonant_player_2 = True

                        if p2 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p2 = convert(input('Guess a word: ').lower())
                            word2 = convert(word2)
                            if p2 == word2:
                                print('You guessed right!', word2, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_2_score_r2)
                                p_1_score_r2 = 0
                                p_3_score_r2 = 0
                                first_consonant_player_2 = True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_2 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_2_turn = False
                                first_consonant_player_2 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_2 = True
                    player_2_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_2 = True
                player_2_turn = False

    while first_consonant_player_3 == False:
        round_2_spin = spin3
        if spin == bankrupt:
            print('Bankrupt, you lose a turn')
            first_consonant_player_3 = True
            player_3_turn = False
            p_3_score_r2 = 0
        elif spin == lose_a_turn:
            print('You lose a turn')
            first_consonant_player_3 = True
            player_3_turn = False
        else:
            print(' '.join(word_underlist2))
            print('Player 3 you up. You are playing for $', spin)
            p3 = input('Guess a consonant: ').lower()
            if len(p3) == 1 and p3 in consonants:
                if p3 in word2:
                    for position in range(len(word2)):
                        if word2[position] == p3:
                            word_underlist2[position] = p3
                            p_3_score_r2 += spin
                            first_consonant_player_3 = True
                    print(' '.join(word_underlist2))
                    print('Good job! You currently have $', p_3_score_r1)     

                    #This is where I start the rest of the questions.
                    while player_3_turn == True:
                        #PLAYER3

                        p3 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p3 == 'consonant':
                            p3 = input('Guess a consonant: ').lower()
                            if len(p3) == 1 and p3 in consonants:
                                if p3 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p3:
                                            word_underlist2[position] = p3
                                            p_3_score_r2 += spin
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            p_1_score_r2 = 0
                                            p_2_score_r2 = 0
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_2 = True
                                    print(' '.join(word_underlist2))
                                    print('Good job! You currently have $', p_3_score_r2)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_3_turn = False
                                    first_consonant_player_3 = True

                        if p3 == 'vowel':
                            p_3_score_r2 -= spin
                            p3 = input('Guess a vowel: ').lower()
                            if len(p3) == 1 and p3 in vowels:
                                if p3 in word2:
                                    for position in range(len(word2)):
                                        if word2[position] == p3:
                                            word_underlist2[position] = p3
                                            p_3_score_r2 -= 250
                                        if '_' not in word_underlist2:
                                            print('You now won!')
                                            p_1_score_r2 = 0
                                            p_2_score_r2 = 0
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
                                print('Bad guess. You lost your turn')
                                player_3_turn = False
                                first_consonant_player_3 = True

                        if p3 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p3 = convert(input('Guess a word: ').lower())
                            word2 = convert(word2)
                            if p3 == word2:
                                print('You guessed right!', word2, 'is correct!')
                                print('You won the round!')
                                print('You made $', p_3_score_r2)
                                p_1_score_r2 = 0
                                p_2_score_r2 = 0
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_2 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_3_turn = False
                                first_consonant_player_3 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_3 = True
                    player_3_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_3 = True
                player_3_turn = False

while round_3 == False:
    #The first round needs its own loop.
    #The first consonant question needs its own loop.
    player_1_turn = True
    first_consonant_player_1 = False
    player_2_turn = True
    first_consonant_player_2 = False
    player_3_turn = True
    first_consonant_player_3 = False
    while first_consonant_player_1 == False:
        round_3_spin = spin3
        if spin == bankrupt:
            print('Bankrupt, you lost round 3 Player 1. You will end up with', player_1_sum, 'and did not get a trip to Hawaii')
            first_consonant_player_1 = True
            player_1_turn = False
            p_1_score_r3 = 0
        elif spin == lose_a_turn:
            print('You lost round 3 Player 1. You will end up with', player_1_sum, 'and did not get a trip to Hawaii')
            first_consonant_player_1 = True
            player_1_turn = False
        else:
            print(' '.join(word_underlist3))
            print('Congrats on making it to round 3 Player 1!. You are playing for $', spin) 
            p1 = input('Guess a consonant: ').lower()
            if len(p1) == 1 and p1 in consonants:
                if p1 in word3:
                    for position in range(len(word3)):
                        if word3[position] == p1:
                            word_underlist3[position] = p1
                            p_1_score_r3 += spin
                            first_consonant_player_1 = True
                    print(' '.join(word_underlist3))
                    print('Good job! You currently have $', p_1_score_r3)     

                    #This is where I start the rest of the questions.
                    while player_1_turn == True:
                        #PLAYER1

                        p1 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p1 == 'consonant':
                            p1 = input('Guess a consonant: ').lower()
                            if len(p1) == 1 and p1 in consonants:
                                if p1 in word3:
                                    for position in range(len(word3)):
                                        if word3[position] == p1:
                                            word_underlist3[position] = p1
                                            p_1_score_r3 += spin
                                        if '_' not in word_underlist2:
                                            print('You now won the final round! You also get a free trip to Hawaii! And dont forget your $', p_1_score_r3, 'you made.')
                                            p_2_score_r3 = 0
                                            p_3_score_r3 = 0
                                            first_consonant_player_1 = True
                                            player_1_turn = False
                                            first_consonant_player_2 =True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_3 = True
                                    print(' '.join(word_underlist3))
                                    print('Good job! You ended with $', p_1_score_r3)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_1_turn = False
                                    first_consonant_player_1 = True

                        if p1 == 'vowel':
                            p_1_score_r3 -= spin
                            p1 = input('Guess a vowel: ').lower()
                            if len(p1) == 1 and p1 in vowels:
                                if p1 in word3:
                                    for position in range(len(word3)):
                                        if word3[position] == p1:
                                            word_underlist3[position] = p1
                                            p_1_score_r3 -= 250
                                        if '_' not in word_underlist3:
                                            print('You now won the final round! As a prize you get a free trip to Hawaii! Dont forget the $', p_1_score_r3, 'you made.')
                                            p_2_score_r3 = 0
                                            p_3_score_r3 = 0
                                            first_consonant_player_1 = True
                                            player_1_turn = False
                                            first_consonant_player_2 =True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_3 = True
                                    print(' '.join(word_underlist3))
                                    print('Good job! You currently have $', p_1_score_r3)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_1_turn = False
                                    first_consonant_player_1 = True
                            else:
                                print('Bad guess. You lost your turn')
                                player_1_turn = False
                                first_consonant_player_1 = True

                        if p1 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p1 = convert(input('Guess a word: ').lower())
                            word3 = convert(word3)
                            if p1 == word3:
                                print('You guessed right!', word3, 'is correct!')
                                print('You won the final round! Your prize is a free trip to Hawaii to go along with your $', p_1_score_r3, 'you made.')
                                p_2_score_r3 = 0
                                p_3_score_r3 = 0
                                first_consonant_player_1 = True
                                player_1_turn = False
                                first_consonant_player_2 =True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_3 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_1_turn = False
                                first_consonant_player_1 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_1 = True
                    player_1_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_1 = True
                player_1_turn = False

    while first_consonant_player_2 == False:
        round_3_spin = spin3
        if spin == bankrupt:
            print('Bankrupt, you lost round 3 Player 2. You will end up with', player_2_sum, 'and did not get a trip to Hawaii')
            first_consonant_player_2 = True
            player_2_turn = False
            p_2_score_r3 = 0
        elif spin == lose_a_turn:
            print('You lost round 3 Player 2. You will end up with', player_2_sum, 'and did not get a trip to Hawaii')
            first_consonant_player_2 = True
            player_2_turn = False
        else:
            print(' '.join(word_underlist3))
            print('Congrats on making it to round 3 Player 2! You are playing for $', spin)
            p2 = input('Guess a consonant: ').lower()
            if len(p2) == 1 and p2 in consonants:
                if p2 in word3:
                    for position in range(len(word3)):
                        if word3[position] == p2:
                            word_underlist3[position] = p2
                            p_2_score_r3 += spin
                            first_consonant_player_2 = True
                    print(' '.join(word_underlist3))
                    print('Good job! You currently have $', p_2_score_r3)     

                    #This is where I start the rest of the questions.
                    while player_2_turn == True:
                        #PLAYER2

                        p2 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p2 == 'consonant':
                            p2 = input('Guess a consonant: ').lower()
                            if len(p2) == 1 and p2 in consonants:
                                if p2 in word3:
                                    for position in range(len(word3)):
                                        if word3[position] == p2:
                                            word_underlist3[position] = p2
                                            p_2_score_r3 += spin
                                        if '_' not in word_underlist3:
                                            print('You now won the last round! Your prize is a free trip to Hawaii to go along with the $', p_2_score_r3, 'you made.')
                                            p_1_score_r3 = 0
                                            p_3_score_r3 = 0
                                            first_consonant_player_2 = True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_3 = True
                                    print(' '.join(word_underlist3))
                                    print('Good job! You currently have $', p_2_score_r3)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_2_turn = False
                                    first_consonant_player_2 = True

                        if p2 == 'vowel':
                            p_2_score_r3 -= spin
                            p2 = input('Guess a vowel: ').lower()
                            if len(p2) == 1 and p2 in vowels:
                                if p2 in word3:
                                    for position in range(len(word3)):
                                        if word3[position] == p2:
                                            word_underlist3[position] = p2
                                            p_2_score_r3 -= 250
                                        if '_' not in word_underlist3:
                                            print('You now won the last round! Your prize is a free trip to Hawaii to go along with the $', p_2_score_r3, 'you made.')
                                            p_1_score_r3 = 0
                                            p_3_score_r3 = 0
                                            first_consonant_player_2 = True
                                            player_2_turn = False
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_3 = True
                                    print(' '.join(word_underlist3))
                                    print('Good job! You currently have $', p_2_score_r3)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_2_turn = False
                                    first_consonant_player_2 = True
                            else:
                                print('Bad guess. You lost your turn')
                                player_2_turn = False
                                first_consonant_player_2 = True

                        if p2 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p2 = convert(input('Guess a word: ').lower())
                            word3 = convert(word3)
                            if p2 == word3:
                                print('You guessed right!', word3, 'is correct!')
                                print('You won the final round! Along with this is a free trip to Hawaii')
                                print('And lets not forget you made $', p_2_score_r3)
                                p_1_score_r3 = 0
                                p_3_score_r3 = 0
                                first_consonant_player_2 = True
                                player_2_turn = False
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_3 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_2_turn = False
                                first_consonant_player_2 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_2 = True
                    player_2_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_2 = True
                player_2_turn = False

    while first_consonant_player_3 == False:
        round_3_spin = spin3
        if spin == bankrupt:
            print('Bankrupt, you lost round 3 Player 3. You will end up with', player_3_sum, 'and did not get a trip to Hawaii')
            first_consonant_player_3 = True
            player_3_turn = False
            p_3_score_r3 = 0
        elif spin == lose_a_turn:
            print('You lost round 3 Player 3. You will end up with', player_3_sum, 'and did not get a trip to Hawaii')
            first_consonant_player_3 = True
            player_3_turn = False
        else:
            print(' '.join(word_underlist3))
            print('Congrats on making it to round 3 Player 3!. You are playing for $', spin)
            p3 = input('Guess a consonant: ').lower()
            if len(p3) == 1 and p3 in consonants:
                if p3 in word3:
                    for position in range(len(word3)):
                        if word3[position] == p3:
                            word_underlist3[position] = p3
                            p_3_score_r3 += spin
                            first_consonant_player_3 = True
                    print(' '.join(word_underlist3))
                    print('Good job! You currently have $', p_3_score_r3)     

                    #This is where I start the rest of the questions.
                    while player_3_turn == True:
                        #PLAYER3

                        p3 = input('Do you want to guess a consonant, vowel, or the word?: ').lower()
                        if p3 == 'consonant':
                            p3 = input('Guess a consonant: ').lower()
                            if len(p3) == 1 and p3 in consonants:
                                if p3 in word3:
                                    for position in range(len(word3)):
                                        if word3[position] == p3:
                                            word_underlist3[position] = p3
                                            p_3_score_r3 += spin
                                        if '_' not in word_underlist3:
                                            print('You now won the last round! Your prize is a free trip to Hawaii to go along with the $', p_3_score_r3, 'you made.')
                                            p_1_score_r3 = 0
                                            p_2_score_r3 = 0
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_3 = True
                                    print(' '.join(word_underlist3))
                                    print('Good job! You currently have $', p_3_score_r3)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_3_turn = False
                                    first_consonant_player_3 = True

                        if p3 == 'vowel':
                            p_3_score_r3 -= spin
                            p3 = input('Guess a vowel: ').lower()
                            if len(p3) == 1 and p3 in vowels:
                                if p3 in word3:
                                    for position in range(len(word3)):
                                        if word3[position] == p3:
                                            word_underlist3[position] = p3
                                            p_3_score_r3 -= 250
                                        if '_' not in word_underlist3:
                                            print('You now won the last round! Your prize is a free trip to Hawaii to go along with the $', p_3_score_r3, 'you made.')
                                            p_1_score_r3 = 0
                                            p_2_score_r3 = 0
                                            first_consonant_player_3 =True
                                            player_3_turn = False
                                            round_3 = True
                                    print(' '.join(word_underlist3))
                                    print('Good job! You currently have $', p_3_score_r3)  
                                else:
                                    print('Bad guess. You lost your turn')
                                    player_3_turn = False
                                    first_consonant_player_3 = True
                            else:
                                print('Bad guess. You lost your turn')
                                player_3_turn = False
                                first_consonant_player_3 = True

                        if p3 == 'word':
                            def convert(s):
                                new = ''
                                for x in s:
                                    new += x
                                return new                            
                            p3 = convert(input('Guess a word: ').lower())
                            word3 = convert(word3)
                            if p3 == word3:
                                print('You guessed right!', word3, 'is correct!')
                                print('You won the final round! You get a free trip to Hawaii!')
                                print('And lets not forget the $', p_3_score_r3, 'you made.')
                                p_1_score_r3 = 0
                                p_2_score_r3 = 0
                                first_consonant_player_3 =True
                                player_3_turn = False
                                round_3 = True
                            else:
                                print('That is not the full word. You lost your turn.')
                                player_3_turn = False
                                first_consonant_player_3 = True

                else:
                    print('That is not in the word. You lost your turn')
                    first_consonant_player_3 = True
                    player_3_turn = False
            else:
                print('That is not one letter and a consonant. You lost your turn')
                first_consonant_player_3 = True
                player_3_turn = False