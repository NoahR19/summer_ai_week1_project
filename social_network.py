#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()
            name = input('What is your name: ')
            if name == 'exit':
                print('Please choose a different name')
                name = input('What is your name: ')
            else:
                age = input('How old are you: ')
                pers = Person(name, age)
                ai_social_network.list_of_people.append(pers)
                ai_social_network.usernames.append(name)


        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            while True:
                if inner_menu_choice == "6":
                    break
                elif inner_menu_choice == '1':
                    print('\nYour name is: ' + pers.id + '\nYour age is: ' + pers.year)
                    change = input('\nWould you like to change your: \n 1. Name \n 2. Age \n 3. Exit \n \n')
                    if change == '1':
                        name = input('What is your name: ')
                        pers.id = name
                    elif change == '2':
                        age = input('How old are you: ')
                        pers.year = age
                    elif change == '3':
                        break
                    else:
                        print("Your input is invalid. Try Again!")
                elif inner_menu_choice == '2':
                    print(*ai_social_network.usernames, sep = "\n")
                    friend = input('Choose a friend from the following to add or write "exit" to leave:\n\n')
                    if friend == 'exit':
                        break
                    for i in ai_social_network.usernames:
                        if friend not in ai_social_network.usernames:
                            print('\nUser does not exist')
                            print(*ai_social_network.usernames, sep = "\n")
                            friend = input('Choose a friend from the following to add or write "exit" to leave:\n\n')
                    pers.friendlist.append(friend)
                    print('\n' + friend + ' has been added to your friends list!\n')
                elif inner_menu_choice == '3':
                    print('\n\nYou are currently friends with:')
                    print(*pers.friendlist, sep = ", ")
                    e = input('\nDo you wish to:\n1. Block a friend\n2. Exit\n\n')
                    if e == '2':
                        break
                    if e == '1':
                        print(*pers.friendlist, sep = ", ")
                        block = input('\nWhich friend do you wish to block?: ')
                        for i in pers.friendlist:
                            if block not in pers.friendlist:
                                 print('\nYou are not friends with this user')
                                 block = input('\nWhich friend do you wish to block?: ')
                        pers.friendlist.remove(block)
                        print('\n' + block + ' has been blocked!\n')
                elif inner_menu_choice == '4':
                    print(*pers.friendlist, sep = ", ")
                    write = input('\nWho do you wish to send a message to a friend or write "exit" to leave:\n\n')
                    if write == "exit":
                        break
                    for i in pers.friendlist:
                        if write not in pers.friendlist:
                            print('\nYou are not friends with this user')
                            write = input('\nWho do you wish to send a message to a friend or write "exit" to leave:\n\n')
                    message = input('\nPlease write the message you wish to send to ' + write + ':\n\n')
                    print('\nYour message to ' + write + ' has been sent!\n')
                    
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                
        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
