import colorama
from colorama import Fore, Back, Style

nouns = []
verbs = []
adj = []
def list_all_nouns():
    for index in nouns:
        print(Fore.LIGHTRED_EX + index + Fore.RESET)
def list_all_verbs():
    for index in verbs:
        print(Fore.LIGHTGREEN_EX + index + Fore.RESET)
def list_all_adj():
    for index in adj:
        print(Fore.LIGHTCYAN_EX + index + Fore.RESET)
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
    r_number = input(Fore.CYAN + 'Enter a number: ' + Fore.RESET)
    r_sport = input(Fore.CYAN + 'Enter your favorite sport: ' + Fore.RESET)
    f_food = input(Fore.CYAN + Fore.CYAN + 'Enter your favorite food: ' + Fore.RESET)
    cool_location = input(Fore.CYAN + 'Where would you like this story to take place? ' + Fore.RESET)
    p_body = input(Fore.CYAN + 'Enter a body part: ' + Fore.RESET)
    f_noun = input(Fore.CYAN + 'Enter a noun: ' + Fore.RESET)
    nouns.append(f_noun)
    p_noun = input(Fore.CYAN + 'Enter a plural noun: ' + Fore.RESET)
    nouns.append(p_noun)
    s_noun = input(Fore.CYAN + 'Alright, one more noun: ' + Fore.RESET)
    nouns.append(s_noun)
    ing_verb = input(Fore.CYAN + 'Enter a verb ending in ing: ' + Fore.RESET)
    verbs.append(ing_verb)
    f_verb = input(Fore.CYAN + 'Enter a verb: ' + Fore.RESET)
    verbs.append(f_verb)
    s_verb = input(Fore.CYAN + 'Last but not least, one more verb: ' + Fore.RESET)
    verbs.append(s_verb)
    f_adj = input(Fore.CYAN + 'Enter an adj: ' + Fore.RESET)
    adj.append(f_adj)
    s_adj = input(Fore.CYAN + 'One more adj: \n' + Fore.RESET)
    adj.append(s_adj)
    story = (
        f'A vacation is when you take a trip to some {f_adj} place. '
        f'Usually you go to some place that is near a/an {f_noun}. '
        f'A good vacation place is one where you can ride {p_noun} or play {r_sport}. \n'
        f'I like to spend to my time {f_verb} or {s_verb}. '
        f'When parents go on a vacation they spend their time eating three {f_food} a day, '
        f'and fathers play golf, and mothers sit around {ing_verb}. \nLast summer, ym little brother fell in a/an '
        f'{s_noun} and got poison oak all over his {p_body}. My family is going to {cool_location}, and I will '
        f'practice {r_sport}. \nParents need vacations more than kids because parents are always {s_adj} and because '
        f'they have to work {r_number} hours every day all year making enough money.'
    )
    print(story)
print(Back.YELLOW + Fore.BLACK + "Hi! Welcome to my Mad Libs project. After you finish the story you have the option to replace, add, or remove certain words to make the story more interesting. Ready? Here we go!" + Fore.RESET + Back.RESET + '\n')
first_story()
start= True
while start:
    user_Input = input(Fore.BLUE + '\nN to list all the nouns, A for all adj, V to list all the verbs. Type Q to quit program ' + Fore.RESET)
    start = select(user_Input)