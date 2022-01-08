import random                                # For random suggestions

import sys

from random import sample

import os           # For clearing Terminal

from time import sleep      # Default time = 3 Seconds



font_list = ['big']
random_font = random.sample(font_list, 1)

try:    # Optional for style, importing pyfiglet module
    from pyfiglet import Figlet
    f = Figlet(font='{}'.format(*random_font))
    print(f.renderText('DeCodeX Restaurant'))
except ImportError or ModuleNotFoundError:
    pass



random_choice = ["Bread cheesecakes", "No egg cheesecakes", "Low amount cheese cheesecakes", 'Egg cheesecakes', 'Cappucino']     # If something is unavailable orfor suggesting random things

cart = []


new_list = []


def limit():             # If order exceeds the 10 item limit
    cls()
    print('Sorry you cannot order more than 10 items.')
    sleep(3)


def cls():

    if sys.platform.startswith('win32' or 'win64' or 'win86'):
        os.system('cls')
    else:
        os.system('clear')




    
def limit_reached():        # When you cannot order more items
    cls()
    print('Sorry it looks like you have reached the maximum limit of ordering this item. Maybe you can try something else. \n')
    order()


    
def get_name(shop_name = 'DeCodeX Restaurant'):
    name = input("Can I have your name please?\n\n> ")
    name1 = name.title()
    cls()
    
    if len(name1) > 0 and not name1.isdigit():
        print("Hello {}, welcome to {}." .format(name1, shop_name))
        print('')
        order()

        
    elif len(name1) == 0:
        print('Error, name empty.')
        get_name()

        
    elif name1.isdigit():
        print('Please enter only Alphabets.')
        print('')
        get_name()

        
    else:
        print('')
        print('Sorry, I do not understand.')
        print('')
        get_name()

        
def empty_response():  # For empty responses (Do you really think I wouldn't have patched that?)
    cls()
    print("Please answer the respective question.")
    sleep(3)


    
def unavailable():    # If something is unavailable
    cls()
    random1 = random.sample(random_choice, 1)
    abc = input('Sorry, the thing you\'re looking for is currently unavailable.\n \nWould you like to try our delicious {}? (Enter either \'Yes\' or \'No\')\n\n> ' .format(*random1))
    print('')
    
    if abc == 'yes' or abc == 'YES' or abc == 'Yes' or abc == 'y' or abc == 'Y' and abc.isalpha() and len(abc) > 0:
        new_list.append(*random1)
        
        if new_list.count('Bread cheesecakes') > 0:
            bread_cheesecake()
            
        elif new_list.count('No egg cheesecakes') > 0:
            no_egg_cheesecake()
            
        elif new_list.count('Low amount cheese cheesecakes') > 0:
            low_amount_cheese()
            
        elif new_list.count('Egg cheesecakes') > 0:
            egg_cheesecake()
            
        elif new_list.count('Cappucino') > 0:
            cappucino()
            
    elif abc == 'no' or abc == 'NO' or abc == 'No' or abc == 'n' or abc == 'N' and abc.isalpha() and len(abc) > 0:
        cls()
        print('Okay, some other time.')
        print('')
        order()
        
    elif abc != 'yes' or abc != 'Yes' or abc != 'YES' or abc != 'y' or abc != 'Y' or abc != 'no' or abc != 'No' or abc != 'NO' or abc != 'N' or abc != 'n':
        print('Enter only \'Yes\' or \'No\'')
        unavailable()
        
    elif len(abc) == 0:
        print('Error, response empty.')
        unavailable()
        
    elif abc != abc.isalpha():
        print('Please enter only \'Yes\' or \'No\'')
        unavailable()
        
    else:
        print('Sorry I do not understand.')
        unavailable()



def order2(shop_name = 'Merryweather Cheesecakes'):  # For ordering different types of items.
    print('')
    choice = input('Do you want to order something else? (Enter either \'Yes\' or \'No\' )\n\n> ')
    
    if choice == 'yes' or choice == 'YES' or choice == 'Yes' or choice == 'Y' or choice == 'y' and choice.isalpha() and len(choice) > 0:
        cls()
        order()
        return cart
    
    elif choice == 'No' or choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n' and choice.isalpha() and len(choice) > 0:
        cls()
        print("Here is your final order: ") #\n{} .format(*cart))
        print('')
        for items in cart:
            print('{}\n' .format(items))
        print('')
        abc = input('Thank you for shopping with {}.\n\nPress Enter to exit program. \n \n' .format(shop_name))
        
        if len(abc) > 0:
            exit()
            
        else:
            exit()
            
    elif choice != 'yes' or choice != 'no':
        empty_response()
        order2()
        
    elif len(choice) == 0:
        empty_response()
        order2()
        
    elif choice != choice.isalpha():
        empty_response()
        order2()
        
    else:
        print('Sorry, I do not understand.')
        order2()

        
        
def random_suggestion(): # For suggesting random things
    cls()
    suggestion_sample = random.sample(random_choice, 1)
    will = input('We think you would like our {}.\n \nDo you wish to continue? Enter either \'Yes\' or \'No\'.\n\n> '.format(*suggestion_sample))
    
    if will == 'yes' or will == 'YES' or will == 'Yes' or will == 'Y' or will == 'y' and will.isalpha() and len(will) > 0:
        new_list.append(*suggestion_sample)
        
        if new_list.count('Bread cheesecakes') > 0:
            bread_cheesecake()
            
        elif new_list.count('No egg cheesecakes') > 0:
            no_egg_cheesecake()
            
        elif new_list.count('Low amount cheese cheesecakes') > 0:
            low_amount_cheese()
            
        elif new_list.count('Egg cheesecakes') > 0:
            egg_cheesecake()
            
        elif new_list.count('Cappucino') > 0:
            cappucino()
            
    elif will == 'no' or will == 'NO' or will == 'No' or will == 'N' or will == 'n' and will.isalpha() and len(will) > 0:
        cls()
        print('Okay, some other time.')
        print('')
        order()
    elif will != 'no' or will != 'NO' or will != 'No' or will != 'N' or will != 'n' or will != 'Yes' or will != 'YES' or will != 'yes' or will != 'Y' or will != 'y':
         empty_response()
         random_suggestion()


        
def bread_cheesecake():
    cls()
    choice = input("What type of Bread cheesecake do you want? \n \na) Double sided Bread cheesecake \nb) Single sided Bread cheesecake \n\nEnter the respective option \'a\', \'b\', or enter \'1\' to go back to menu. \n> ")
    
    if choice  == 'a' or choice == 'A' or choice == 'a)' or choice == 'A)' and choice.isalpha() and len(choice) > 0:
        cls()
        
        while cart.count('10 pieces of Double sided Bread cheesecake.') == 0:
            
            try:
                pieces = int(input("And how many pieces of Double sided Bread cheesecake do you want?\n\n> "))
                
                if pieces == 1:
                    cls()
                    print("Here is your order:\n\n{} piece Double sided Bread cheesecake." .format(pieces))
                    cart.append("{} piece Double sided Bread cheesecake.".format(pieces))
                    order2()
                    return counter
                
                elif pieces == 0:
                    empty_response()
                    bread_cheesecake()
                    
                elif pieces > 10:
                    limit()
                    bread_cheesecake()
                    
                elif pieces != 1:
                    cls()
                    print("Here is your order:\n\n{} pieces of double sided Bread cheesecake." .format(pieces))
                    cart.append("{} pieces of Double sided Bread cheesecake.".format(pieces))
                    order2()
                    
                else:
                    empty_response()
                    bread_cheesecake()
                    
            except ValueError:
                empty_response()
                bread_cheesecake()
                
        if cart.count('10 pieces of Double sided Bread cheesecake.') > 0:
            limit_reached()
            bread_cheesecake()
            
        else:
            limit_reached()
            bread_cheesecake()
            
    elif choice  == 'b' or choice == 'B' or choice == 'b)' or choice == 'B)' and choice.isalpha() and len(choice) > 0:
        cls()
        try:
            pieces = int(input("And how many pieces of single sided bread cheesecake do you want?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Here is your order:\n\n{} piece single sided Bread cheesecake.".format(pieces))
                cart.append("{} piece single sided Bread cheesecake.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                bread_cheesecake()
                
            elif pieces > 10:
                limit()
                bread_cheesecake()
                
            elif pieces != 1:
                cls()
                print('Here is your order:\n\n{} pieces of single sided bread cheesecake.' .format(pieces))
                cart.append("{} pieces of single sided bread cheesecake." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                bread_cheesecake()
                
        except ValueError:
            empty_response()
            bread_cheesecake()
            
    elif choice != 'a' or choice != 'b':
        try:
            try:
                if int(choice) == 1:
                    order()
                    
                elif int(choice) > 1 or int(choice) < 1 or int(choice) == 0:
                    empty_response()
                    bread_cheesecake()
                    
            except choice !=1:
                empty_response()
                bread_cheesecake()
                
        except TypeError:
            empty_response()
            bread_cheesecake()
            
    elif choice != choice.isalpha():
        empty_response()
        bread_cheesecake()
        
    elif len(choice) == 0:
        empty_response()
        bread_cheesecake()
        
    else:
        print('Sorry I do not understand.')
        bread_cheesecake()


        
def no_egg_cheesecake():
    cls()
    choice = input("What flavour of cheesecake without egg do you want?\n\na) Chocolate \nb) Vanilla \nc) Strawberry \nd) Blackberry \n \nEnter the respective option \'a\', \'b\', \'c\', \'d\', or enter \'1\' to go back to menu.\n\n> ")
    
    if choice  == 'a' or choice == 'A' or choice == 'a)' or choice == 'A)' and choice.isalpha() and len(choice) > 0:
        cls()
        choco = input('And what type of chocolate flavour do you want?\n\na) Normal chocolate \nb) Dark chocolate\n\n> ')
        
        if choco == 'a' or choco == 'A' or choco == 'a)' or choco == 'A)':
            cls()
            
            while cart.count('10 piece of Normal chocolate cheesecake without eggs.') == 0:
                try:
                    pieces = int(input("And how many pieces of Normal chocolate cheesecake without eggs do you want?\n\n> "))
                    
                    if pieces == 1:
                        print('')
                        print("Here is your order:\n\n{} piece Normal chocolate cheesecake without eggs." .format(pieces))
                        cart.append("{} piece Normal chocolate cheesecake without eggs.".format(pieces))
                        order2()
                        return cart
                    
                    elif pieces == 0:
                        empty_response()
                        no_egg_cheesecake()
                        
                    elif pieces > 10:
                        limit()
                        no_egg_cheesecake()
                        
                    elif pieces != 1:
                        cls()
                        print("Here is your order:\n\n{} pieces of Normal chocolate cheesecake without eggs." .format(pieces))
                        cart.append("{} pieces of Normal chocolate cheesecake without eggs.".format(pieces))
                        order2()
                        return cart
                    
                    else:
                        empty_response()
                        no_egg_cheesecake()
                        
                except ValueError:
                    empty_response()
                    no_egg_cheesecake()
                    
            if cart.count('10 piece of Normal chocolate cheesecake without eggs.') > 0:
                limit_reached()
                no_egg_cheesecake()
                
            else:
                limit_reached()
                no_egg_cheesecake()
                
        elif choco == 'b' or choco == 'B' or choco == 'B)' or choco =='b)':
                unavailable()
                
        elif choco != choco.isalpha():
                empty_response()
                no_egg-cheesecake()
                
        elif len(choco) == 0:
                empty_response()
                no_egg_cheesecake()
                
        elif choco != 'a' or choco != 'b':
                empty_response()
                no_egg_cheesecake()
        else:
                print("Sorry I do not understand")
                no_egg_cheesecake()
                
    elif choice  == 'b' or choice == 'B' or choice == 'b)' or choice == 'B)' and choice.isalpha() and len(choice) > 0:
        cls()
        
        try:
            pieces = int(input("And how many pieces of Vanilla cheesecake without eggs do you want?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Here is your order:\n\n{} piece Vanilla cheesecake without eggs.".format(pieces))
                cart.append("{} piece single Vanilla cheesecake without eggs.".format(pieces))
                order2()
                return cart
            
            elif pieces > 10:
                limit()
                no_egg_cheesecake()
                
            elif pieces == 0:
                empty_response()
                no_egg_cheesecake()
                
            elif pieces != 1:
                cls()
                print('Here is your order:\n\n{} pieces of Vanilla cheesecake without eggs.' .format(pieces))
                cart.append("{} pieces of Vanilla cheesecake without eggs." .format(pieces))
                order2()
                
            elif len(pieces) >= 0:
                empty_response()
                no_egg_cheesecake()
                
        except ValueError:
            empty_response()
            no_egg_cheesecake()
            
    elif choice == 'c' or choice == 'C' or choice == 'c)' or choice == 'C)' and choice.isalpha() and len(choice) >0:
        cls()
        
        try:
            pieces = int(input("And how many pieces of Strawberry cheesecake without eggs do you want?\n\n> "))
            if pieces == 1:
                cls()
                print("Here is your order:\n\n{} piece Strawberry cheesecake without eggs.".format(pieces))
                cart.append("{} piece single Strawberry cheesecake without eggs.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                no_egg_cheesecake()
                
            elif pieces > 10:
                limit()
                no_egg_cheesecake()
                
            elif pieces != 1:
                cls()
                print('Here is your order:\n\n{} pieces of Strawberry cheesecake without eggs.' .format(pieces))
                cart.append("{} pieces of Strawberry cheesecake without eggs." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                no_egg_cheesecake()
                
        except ValueError:
            empty_response()
            no_egg_cheesecake()
            
    elif choice == 'd' or choice == 'D' or choice == "D)" or choice =='d)' and choice.isalpha() and len(choice) > 0:
        unavailable()
        
    elif choice != 'a' or choice != 'b' or choice != 'c' or choice != 'd':
        try:
            try:
                if int(choice) == 1:
                    order()
                    
                elif int(choice) > 1 or int(choice) < 1 or int(choice) == 0:
                    empty_response()
                    no_egg_cheesecake()
                    
            except choice !=1:
                empty_response()
                no_egg_cheesecake()
                
        except TypeError:
            empty_response()
            no_egg_cheesecake()
            
    elif choice != choice.isalpha():
        empty_response()
        no_egg_cheesecake()
        
    elif len(choice) == 0:
        empty_response()
        no_egg_cheesecake()
        
    else:
        print('Sorry, I do not understand.')



def low_amount_cheese():
    cls()
    choice = input("Which flavour of low amount cheese cheesecake do you want?\n\na) Chocolate \nb) Vanilla \n \nEnter the respective option \'a\', \'b\' or enter \'1\' to go back to menu.\n\n> ")
    
    if choice == 'a' or choice == 'A' or choice == 'A)' or choice == 'a)' and choice.isalpha() and len(choice) > 0:
        cls()
        
        p_choice  = input('And how much amount of cheese do you want?\n\na) 25% \nb) 50% \nc) 75% \n \nEnter the respective option \'a\', \'b\', \'c\', or enter \'1\' to go back to menu.\n\n> ')
        
        if p_choice == 'a' or p_choice == 'A' or p_choice == 'a)' or p_choice == 'A)' and p_choice.isalpha() and len(p_choice) > 0:
            cls()
            
            try:
                amount = int(input('And how many such cheesecakes do you want?\n\n> '))
                if amount == 1:
                    cls()
                    print('Here is your order:\n\n{} piece chocolate cheesecake with 25% cheese.' .format(amount))
                    cart.append('{} piece chocolate cheesecake with 25% cheese.' .format(amount))
                    order2()
                    return cart
                
                if amount == 0:
                    empty_response()
                    low_amount_cheese()
                    
                elif amount > 10:
                    limit()
                    low_amount_cheese()
                    
                elif amount != 1:
                    cls()
                    print('Here is your order:\n\n{} pieces of chocolate cheesecake with 25% cheese.' .format(amount))
                    cart.append('{} pieces of chocolate cheesecake with 25% cheese.' .format(amount))
                    order2()
                    return cart
                
                else:
                    empty_response()
                    low_amount_cheese()
                    
            except ValueError:
                empty_response()
                low_amount_cheese()
                
        elif p_choice == 'b' or p_choice == 'B' or p_choice == 'b)' or p_choice == 'B)' and p_choice.isalpha() and len(p_choice) > 0:
            cls()
            
            try:
                amount = int(input('And how many such cheesecakes do you want?\n\n> '))
                if amount == 1:
                    cls()
                    print('Here is your order:\n\n{} piece chocolate cheesecake with 50% cheese.' .format(amount))
                    cart.append('{} piece chocolate cheesecake with 50% cheese.' .format(amount))
                    order2()
                    return cart
                
                elif amount > 10:
                    limit()
                    low_amount_cheese()
                    
                elif amount > 1:
                    cls()
                    print('Here is your order:\n\n{} pieces of chocolate cheesecake with 50% cheese.' .format(amount))
                    cart.append('{} pieces of chocolate cheesecake with 50% cheese.' .format(amount))
                    order2()
                    return cart
                
                elif amount == 0:
                    empty_response()
                    low_amount_cheese()
                    
                else:
                    empty_response()
                    low_amount_cheese()
                    
            except ValueError:
                empty_response()
                low_amount_cheese()
                
        elif p_choice == 'c' or p_choice == 'C' or p_choice == 'c)' or p_choice == 'C)' and p_choice.isalpha() and len(p_choice) > 0:
            unavailable()
            
        elif p_choice != 'a' or p_choice != 'b' or p_choice != 'c':
            try:
                try:
                    if int(p_choice) == 1:
                        order()
                        
                    elif int(p_choice) > 1 or int(p_choice) < 1 or int(p_choice) == 0:
                        empty_response()
                        low_amount_cheese()
                        
                except p_choice !=1:
                    empty_response()
                    low_amount_cheese()
                    
            except TypeError:
                empty_response()
                low_amount_cheese()
                
        elif p_choice != p_choice.isalpha():
            print('Please enter only alphabets.')
            print('')
            low_amount_cheese()
            
        elif len(p_choice) == 0:
            empty_response()
            low_amount_cheese()
            
        else:
            print('Sorry I do not understand.')
            print('')
            low_amount_cheese()
            
    elif choice == 'b' or choice == 'B' or choice == 'b)' or choice == 'B)' and choice.isalpha() and len(choice) > 0:
        cls()
        p_choice  = input('And how much amount of cheese do you want?\n\na) 25% \nb) 50% \nc) 75%\n\n> ')
        
        if p_choice == 'a' or p_choice == 'A' or p_choice == 'a)' or p_choice == 'A)' and p_choice.isalpha() and len(p_choice) > 0:
            cls()
            try:
                amount = int(input('And how many such cheesecakes do you want?\n\n> '))
                if amount == 1:
                    cls()
                    print('Here is your order:\n\n{} piece Vanilla cheesecake with 25% cheese.' .format(amount))
                    cart.append('{} piece Vanilla cheesecake with 25% cheese.' .format(amount))
                    order2()
                    return cart
                
                elif amount > 10:
                    limit()
                    low_amount_cheese()
                    
                elif amount > 1:
                    cls()
                    print('Here is your order:\n\n{} pieces of Vanilla cheesecake with 25% cheese.' .format(amount))
                    cart.append('{} pieces of Vanilla cheesecake with 25% cheese.' .format(amount))
                    order2()
                    return cart
                
                elif amount == 0:
                    empty_response()
                    low_amount_cheese()
                    
                else:
                    empty_response()
                    low_amount_cheese()
                    
            except ValueError:
                empty_response()
                low_amount_cheese()
                
        elif p_choice == 'b' or p_choice == 'B' or p_choice == 'b)' or p_choice == 'B)' and p_choice.isalpha() and len(p_choice) > 0:
            cls()
            
            try:
                amount = int(input('And how many such cheesecakes do you want?\n\n> '))
                
                if amount == 1:
                    cls()
                    print('Here is your order:\n\n{} piece Vanilla cheesecake with 50% cheese.' .format(amount))
                    cart.append('{} piece Vanilla cheesecake with 50% cheese.' .format(amount))
                    order2()
                    return cart
                
                elif amount > 10:
                    limit()
                    low_amount_cheese()
                    
                elif amount > 1:
                    cls()
                    print('Here is your order:\n\n{} pieces of Vanilla cheesecake with 50% cheese.' .format(amount))
                    cart.append('{} pieces of Vanilla cheesecake with 50% cheese.' .format(amount))
                    order2()
                    return cart
                
                elif amount == 0:
                    empty_response()
                    low_amount_cheese()
                    
                else:
                    empty_response()
                    low_amount_cheese()
                    
            except ValueError:
                empty_response()
                low_amount_cheese()
                
        elif p_choice == 'c' or p_choice == 'C' or p_choice == 'c)' or p_choice == 'C)' and p_choice.isalpha() and len(p_choice) > 0:
            unavailable()
            
        elif p_choice != 'a' or p_choice != 'b' or p_choice != 'c' or p_choice != 'A' or p_choice != 'B' or p_choice != 'C':
            empty_response()
            low_amount_cheese()
            
    elif choice != 'a' or choice != 'b':
        try:
            try:
                
                if int(choice) == 1:
                    order()
                    
                elif int(choice) > 1 or int(choice) < 1 or int(choice) == 0:
                    empty_response()
                    low_amountcheese()
                    
            except choice !=1:
                empty_response()
                low_amount_cheese()
                
        except TypeError:
            empty_response()
            low_amount_cheese()
            
    elif choice != choice.isalpha():
        empty_response()
        low_amount_cheese()
        
    elif len(choice) == 0:
        empty_response()
        low_amount_cheese()
        
    else:
        print('Sorry, I do not understand.')
        print('')
        low_amount_cheese()



        
def egg_cheesecake():
    cls()
    choice = input("What flavour cheesecake do you want?\n\na) Chocolate \nb) Vanilla \nc) Strawberry \nd) Blackberry\n\n> ")
    
    if choice  == 'a' or choice == 'A' or choice == 'a)' or choice == 'A)' and choice.isalpha() and len(choice) > 0:
        cls()
        choco = input('And what type of chocolate flavour do you want?\n\na) Normal chocolate \nb) Dark chocolate\n\n> ')
        
        if choco == 'a' or choco == 'A' or choco == 'a)' or choco == 'A)':
            cls()
            
            try:
                pieces = int(input("And how many pieces of Normal chocolate cheesecake do you want?\n\n> "))
                
                if pieces == 1:
                    cls()
                    print("Here is your order:\n\n{} piece Normal chocolate cheesecake." .format(pieces))
                    cart.append("{} piece Normal chocolate cheesecake.".format(pieces))
                    order2()
                    return cart
                
                elif pieces == 0:
                    empty_response()
                    egg_cheesecake()
                    
                elif pieces > 10:
                    limit()
                    egg_cheesecake()
                    
                elif pieces != 1:
                    cls()
                    print("Here is your order:\n\n{} pieces of Normal chocolate cheesecake." .format(pieces))
                    cart.append("{} pieces of Normal chocolate cheesecake.".format(pieces))
                    order2()
                    return cart
                
                else:
                    empty_response()
                    egg_cheesecake()
                    
            except ValueError:
                empty_response()
                egg_cheesecake()
                
        elif choco == 'b' or choco == 'B' or choco == 'B)' or choco =='b)':
            cls()
            try:
                pieces = int(input("And how many pieces of Dark chocolate cheesecake do you want?\n\n> "))
                
                if pieces == 1:
                    cls()
                    print("Here is your order:\n\n{} piece Dark chocolate cheesecake." .format(pieces))
                    cart.append("{} piece Dark chocolate cheesecake.".format(pieces))
                    order2()
                    return cart
                
                elif pieces == 0:
                    empty_response()
                    egg_cheesecake()
                    
                elif pieces > 10:
                    limit()
                    egg_cheesecake()
                    
                elif pieces != 1:
                    cls()
                    print("Here is your order:\n\n{} pieces of Dark chocolate cheesecake." .format(pieces))
                    cart.append("{} pieces of Dark chocolate cheesecake.".format(pieces))
                    order2()
                    return cart
                
                else:
                    empty_response()
                    egg_cheesecake()
                    
            except ValueError:
                empty_response()
                egg_cheesecake()
                
        elif choco != choco.isalpha():
            empty_response()
            egg-cheesecake()
            
        elif len(choco) == 0:
            empty_response()
            egg_cheesecake()
            
        elif choco != 'a' or choco != 'b':
            empty_response()
            egg_cheesecake()
            
        else:
            print("Sorry I do not understand")
            egg_cheesecake()
            
    elif choice  == 'b' or choice == 'B' or choice == 'b)' or choice == 'B)' and choice.isalpha() and len(choice) > 0:
        cls()
        
        try:
            pieces = int(input("And how many pieces of Vanilla cheesecake do you want?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Here is your order:\n\n{} piece Vanilla cheesecake.".format(pieces))
                cart.append("{} piece single Vanilla cheesecake.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                egg_cheesecake()
                
            elif pieces > 10:
                limit()
                egg_cheesecake()
                
            elif pieces != 1:
                cls()
                print('Here is your order:\n\n{} pieces of Vanilla cheesecake.' .format(pieces))
                cart.append("{} pieces of Vanilla cheesecake." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                egg_cheesecake()
                
        except ValueError:
            empty_response()
            egg_cheesecake()
            
    elif choice == 'c' or choice == 'C' or choice == 'c)' or choice == 'C)' and choice.isalpha() and len(choice) >0:
        cls()
        
        try:
            pieces = int(input("And how many pieces of Strawberry cheesecake do you want?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Here is your order:\n\n{} piece Strawberry cheesecake.".format(pieces))
                cart.append("{} piece single Strawberry cheesecake.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                egg_cheesecake()
                
            elif pieces > 10:
                limit()
                egg_cheesecake()
                
            elif pieces != 1:
                cls()
                print('Here is your order:\n\n{} pieces of Strawberry cheesecake.' .format(pieces))
                cart.append("{} pieces of Strawberry cheesecake." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                egg_cheesecake()
                
        except ValueError:
            empty_response()
            egg_cheesecake()
            
    elif choice == 'd' or choice == 'D' or choice == "D)" or choice =='d)' and choice.isalpha() and len(choice) > 0:
        cls()
        
        try:
            pieces = int(input("And how many pieces of Blackberry cheesecake do you want?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Here is your order:\n\n{} piece Blackberry cheesecake.".format(pieces))
                cart.append("{} piece single Blackberry cheesecake.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                egg_cheesecake()
                
            elif pieces > 10:
                limit()
                egg_cheesecake()
                
            elif pieces != 1:
                cls()
                print('Here is your order:\n\n{} pieces of Blackberry cheesecake.' .format(pieces))
                cart.append("{} pieces of Blackberry cheesecake." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                egg_cheesecake()
                
        except ValueError:
            empty_response()
            egg_cheesecake()
            
    elif choice != 'a' or choice != 'b' or choice != 'c' or choice != 'd':
        empty_response()
        egg_cheesecake()
        
    elif choice != choice.isalpha():
        empty_response()
        egg_cheesecake()
        
    elif len(choice) == 0:
        empty_response()
        egg_cheesecake()
        
    else:
        print('Sorry, I do not understand.')
        egg_cheesecake()



        
def cappucino():
    cls()
    choice = input('What Cappucino size do you want?\n \na) Small \nb) Medium \nc) Large \n\nPlease enter either \'a\', \'b\' or \'c\'.\n\n> ')
    
    if choice  == 'a' or choice == 'A' or choice == 'a)' or choice == 'A)' and choice.isalpha() and len(choice) > 0:
        unavailable()
        
    elif choice == 'b' or choice == 'B' or choice == 'b)' or choice == 'B)' and choice.isalpha() and len(choice) > 0:
        cls()
        
        try:
            pieces = int(input("And how many Medium Cappucino glasses do you want?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Here is your order:\n\n{} Medium Cappucino glass.".format(pieces))
                cart.append("{} Medium Cappucino glass.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                cappucino()
                
            elif pieces > 10:
                limit()
                cappucino()
                
            elif pieces != 1:
                cls()
                print('Here is your order:\n\n{} Medium Cappucino glasses.' .format(pieces))
                cart.append("{} Medium Cappucino glasses." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                cappucino()
                
        except ValueError:
            empty_response()
            cappucino()
            
    elif choice == 'c' or choice == 'C' or choice == 'c)' or choice == 'C)' and choice.isalpha() and len(choice) > 0:
        cls()
        
        try:
            pieces = int(input("And how many Large Cappucino glasses do you want?\n\n> "))
            
            if pieces == 1:
                cls()
                print("Here is your order:\n\n{} Large Cappucino glass.".format(pieces))
                cart.append("{} Large Cappucino glass.".format(pieces))
                order2()
                return cart
            
            elif pieces == 0:
                empty_response()
                cappucino()
                
            elif pieces > 10:
                limit()
                cappucino()
                
            elif pieces != 1:
                cls()
                print('Here is your order:\n\n{} Large Cappucino glasses.' .format(pieces))
                cart.append("{} Large Cappucino glasses." .format(pieces))
                order2()
                return cart
            
            elif len(pieces) >= 0:
                empty_response()
                cappucino()
                
        except ValueError:
            empty_response()
            cappucino()
            
    elif choice != 'c' or choice != 'C':
        empty_response()
        cappucino()
        
    elif choice != choice.isalpha():
        print('Please enter only alphabets.')
        print('')
        cappucino()
        
    elif len(choice) == 0:
        empty_response()
        cappucino()
        
    else:
        print('Sorry, I do not understand.')
        print('')
        cappucino()



def order():
    print("Here is our menu: \n\na) Bread cheesecake \nb) No egg cheesecake \nc) Low amount cheese cheesecake \nd) Egg cheesecake \ne) Cappucino \nf) Suggest something random")
    print('')
    choice = input("Enter the respective option \'a\', \'b\', \'c\', \'d\', \'e\', \'f\' or enter \'1\' to exit program.\n\n> ")
    
    if choice == 'a' or choice == 'A' or choice == 'a)' or choice == 'A)' and choice.isalpha() and len(choice) > 0:
        bread_cheesecake()
        
    elif choice == 'b' or choice == 'B' or choice == 'b)' or choice == 'B)' and choice.isalpha() and len(choice) > 0:
        no_egg_cheesecake()
        
    elif choice == 'c' or choice == 'C' or choice == 'C)' or choice == 'c)' and choice.isalpha() and len(choice) > 0:
        low_amount_cheese()
        
    elif choice == 'd' or choice == 'D' or choice == 'D)' or choice == 'd)' and choice.isalpha() and len(choice) > 0:
        egg_cheesecake()
        
    elif choice == 'e' or choice == 'E' or choice == 'E)' or choice == 'e)' and choice.isalpha() and len(choice) > 0:
        cappucino()
        
    elif choice == 'f' or choice == 'F' or choice == 'f)' or choice == 'F)' and choice.isalpha() and len(choice) > 0:
        random_suggestion()
        
    elif choice != 'a' or choice != 'b' or choice != 'c' or choice != 'd' or choice != 'e' or choice != 'f':
        try:
            try:
                if choice == 1:
                    exit()
                    
                elif int(choice) > 1 or int(choice) < 1 or int(choice) == 0:
                    empty_response()
                    order()
                    
            except choice !=1:                                                                      # WHY ARE YOU HERE RN???
                empty_response()
                order()
                
        except TypeError:
            empty_response()
            order()
            
    elif choice != choice.isalpha():
        empty_response()
        print('')
        order()
        
    elif len(choice) == 0:
        empty_response()
        print('')
        order()

        
get_name()
