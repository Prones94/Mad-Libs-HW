nouns = []
verbs = []
adj = []
def list_all_nouns():
    for index in nouns:
        print(index)
def list_all_verbs():
    for index in verbs:
        print(index)
def list_all_adj():
    for index in adj:
        print(index)
def user_Input(prompt):
    user_Input = input(prompt)
    return user_Input

def select(select_letter):
    if select_letter == 'N':
        list_all_nouns()
        return True
    elif select_letter == 'A':
        list_all_adj()
        return True
    elif select_letter == 'V':
        list_all_verbs()
        return True
    elif select_letter == 'Q':
        return False
    else:
        print('Not an option, try again:')
        return True
    return True
# Function that prints story
def first_story():
    r_number = input('Enter a number: ')
    r_sport = input('Enter your favorite sport: ')
    f_food = input('Enter your favorite food: ')
    cool_location = input('Where would you like this story to take place? ')
    p_body = input('Enter a body part: ')
    f_noun = input('Enter a noun: ')
    nouns.append(f_noun)
    p_noun = input('Enter a plural noun: ')
    nouns.append(p_noun)
    s_noun = input('Alright, one more noun: ')
    nouns.append(s_noun)
    ing_verb = input('Enter a verb ending in ing: ')
    verbs.append(ing_verb)
    f_verb = input('Enter a verb: ')
    verbs.append(f_verb)
    s_verb = input('Last but not least, one more verb: ')
    verbs.append(s_verb)
    f_adj = input('Enter an adj: ')
    adj.append(f_adj)
    s_adj = input('One more adj: \n')
    adj.append(s_adj)
    story = (
        f'A vacation is when you take a trip to some {f_adj} place. '
        f'Usually you go to some place that is near a/an {f_noun}. '
        f'A good vacation place is one where you can ride {p_noun} or play {r_sport}. '
        f'I like to spend to my time {f_verb} or {s_verb}. '
        f'When parents go on a vacation they spend their time eating three {f_food} a day, '
        f'and fathers play golf, and mothers sit around {ing_verb}. Last summer, ym little brother fell in a/an '
        f'{s_noun} and got poison oak all over his {p_body}. My family is going to {cool_location}, and I will '
        f'practice {r_sport}. Parents need vacations more than kids because parents are always {s_adj} and because '
        f'they have to work {r_number} hours every day all year making enough money.'
    )
    print(story)
print("Hi welcome to my Mad Libs project. After you finish the story you have the option to replace, add, or remove certain words to make the story more interesting. Ready? Here we go!\n")
first_story()
start= True
while start:
    user_Input = input('\nN to list all the nouns, A for all adj, V to list all the verbs. Type Q to quit program ')
    start = select(user_Input)