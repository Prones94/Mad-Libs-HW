# User selects mad libs story
select_story = input('Which story would you liek to choose: vacation, school, or home?')


if select_story == "vacation":
    first_story()
# elif select_story =="school":
def userInput():
    someVar = input(">> ")
    return someVar


def grab_word():
    print('Give me a number:')
    r_number = userInput()
    print('Enter a noun:')
    f_noun = userInput()
    print('Enter a plural noun:')
    p_noun = userInput()
    print('Enter an adjective:')
    f_adj = userInput()
    print('Enter a verb: ')
    f_verb = userInput()
    print('Enter a sport: ')
    r_sport = userInput()
    print('Enter a favorite food')
    f_food = userInput()
    print('Enter one more noun: ')
    s_noun = userInput()
    print('One more adj:')
    s_adj = userInput()
    print('Enter another verb: ')
    s_verb = userInput()
    print('What body part would you like to use?')
    p_body = userInput()
    print('Where would you like this story to take place?')
    cool_location = userInput()

grab_word()
def first_story():
    print(f'A vacation is when you take a trip to some {f_adj} place. Usually you go to some place 
        that is near a/an {f_noun}. A good vacation place is one where you can ride {plural_noun} 
        or play{r_sport}. I like to spend my time {f_verb} or {s_verb}.
        When parents go on a vacation, they spend their time eating three {f_food} a day, and fathers play golf, and mothers
        sit around {}. Last summer, my little brother fell in a/an {s_noun} and got poison oak all
        over his {p_body}. My family is going to go to{cool_location}, and I will practice{s_verb}. Parents
        need vacations more than kids because parents are always very
        {s_adj} and because they have to work {r_number} hours every day all year making enough money to pay
        for the vacation')
