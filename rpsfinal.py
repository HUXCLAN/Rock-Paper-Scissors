import time
import os
import random
import json

choices = ('rock', 'paper', 'scissors')
namelist = ('James', 'Robert', 'John', 'Michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Christopher', 'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Jessica', 'Sarah', 'Karen', 'Lisa')
round = 0

def main():
    global data_dict
    global data_dict1
    global data_dict2
    global data_dict3
    global player_name
    os.system('cls')
    print ('Rock, Paper, Scissors, Shoot!')
    dd = data_dict['Games Played']
    d1d = data_dict1['Games Played']
    d2d = data_dict2['Games Played']
    d3d = data_dict3['Games Played']
    dint = dd + d1d + d2d + d3d
    if dint == 1:
        print('Welcome back, {}. You have logged in once'.format(player_name))
    elif dint > 0:
        print('Welcome back, {}. You have logged in {} times.'.format(player_name, dint))
    else:
        print('Welcome, {} to Rock, Paper, Scissors! This is your first time playing.'.format(player_name))
    print('''
    a. Play a game
    b. Leaderboards
    c. Exit the game
          ''')
    choice = input('Enter a choice: ').lower()
    if choice == 'a' or choice == 1:
        play()
    elif choice == 'b' or choice == 2:
        leaderboard()
    elif choice == 'c' or choice == 3:
        exit()     
    else:
        print ('INVALID CHOICE.')
        time.sleep(3)
        main()

def leaderboard():
    global data_dict
    global data_dict1
    global data_dict2
    global data_dict3
    print('Single Games')
    print('Name:', player_name)
    for key, value in data_dict.items():
        print ('{}: {}'.format(key, value))
    print('Best of Three')
    for key, value in data_dict1.items():
        print ('{}: {}'.format(key, value))
    print('Best of Five')
    for key, value in data_dict2.items():
        print ('{}: {}'.format(key, value))
    print('Best of Ten')
    for key, value in data_dict3.items():
        print ('{}: {}'.format(key, value))
    os.system('pause')
    main()

def play():
    os.system('cls')
    global player_num
    global gamemode
    print ('''
    a. Single Game
    b. Best of Three
    c. Best of Five
    d. Best of Ten
    ''')
    gamemode = input('Enter a gamemode: ').lower()
    if gamemode == 'a' or gamemode == 1:
        playeramount()
    elif gamemode == 'b' or gamemode == 2:
        playeramount()
    elif gamemode == 'c' or gamemode == 3:
        playeramount()
    elif gamemode == 'd' or gamemode == 4:
        playeramount()
    else:
        print ('INVALID CHOICE.')
        time.sleep(3)
        play()

def playeramount():
    global player_num
    global gamemode
    print ('''
        How many players do you want on
    each team? (Inputs 1 and 0 only work
    right now.)
    ''')
    try:
        player_num = int(input(': '))
    except ValueError:
        print ('INVALID CHOICE.')
        time.sleep(3)
        playeramount()
    if player_num < 0 or player_num > 5:
        print ('INVALID CHOICE.')
        time.sleep(3)
        playeramount()
    if gamemode == 'a' or gamemode == 1:
        single()
    if gamemode == 'b' or gamemode == 2:
        multiround()    
    if gamemode == 'c' or gamemode == 3:
        multiround()    
    if gamemode == 'd' or gamemode == 4:
        multiround()    
    else:
        print ('INVALID CHOICE.')
        time.sleep(3)
        playeramount()

def multiround_win():
    global player_name
    global round
    global gamemode
    global max_round
    print ('Congratulations {}, You Win!'.format(player_name))
    file = open('rpsdata.txt', 'w')
    if round == max_round:
        if gamemode == 'b' or gamemode == 2:
            gp_num = data_dict1['Games Played'] + 1
            gw_num = data_dict1['Games Won'] + 1
            data_dict1.update({'Games Played': gp_num, 'Games Won': gw_num})
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[1]))           
        if gamemode == 'c' or gamemode == 3:
            gp_num = data_dict2['Games Played'] + 1
            gw_num = data_dict2['Games Won'] + 1
            data_dict2.update({'Games Played': gp_num, 'Games Won': gw_num})
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[2]))
        if gamemode == 'd' or gamemode == 4:
            gp_num = data_dict3['Games Played'] + 1
            gw_num = data_dict3['Games Won'] + 1
            data_dict3.update({'Games Played': gp_num, 'Games Won': gw_num})
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[3]))
        os.system('pause')
        round = 0
    else:
        round = round + 1
        multiround()
    
    file.close()
    os.system('pause')
    main()

def multiround_lose():
    global player_name
    global round
    global gamemode
    global max_round
    print ('Sorry, {}, you lose.'.format(player_name))
    file = open('rpsdata.txt', 'w')
    if round == max_round:
        if gamemode == 'b' or gamemode == 2:
            gp_num = data_dict1['Games Played'] + 1
            gw_num = data_dict1['Games Lost'] + 1
            data_dict1.update({'Games Played': gp_num, 'Games Lost': gw_num})
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[1]))
        if gamemode == 'c' or gamemode == 3:
            gp_num = data_dict2['Games Played'] + 1
            gw_num = data_dict2['Games Lost'] + 1
            data_dict2.update({'Games Played': gp_num, 'Games Lost': gw_num})
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[2]))
        if gamemode == 'd' or gamemode == 4:
            gp_num = data_dict3['Games Played'] + 1
            gw_num = data_dict3['Games Lost'] + 1
            data_dict3.update({'Games Played': gp_num, 'Games Lost': gw_num})
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[3]))
        os.system('pause')
        round = 0
    else:
        round = round + 1
        multiround()

def multiround_tie():
    global player_name
    global round
    global gamemode
    global max_round
    print ('Sorry, {}, it was a tie!'.format(player_name))
    file = open('rpsdata.txt', 'w')
    if round == max_round:
        if gamemode == 'b' or gamemode == 2:
            gp_num = data_dict1['Games Played'] + 1
            gw_num = data_dict1['Games Drawn'] + 1
            data_dict1.update({'Games Played': gp_num, 'Games Drawn': gw_num})
            file.write(json.dumps(data_dict1))
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[1]))
        if gamemode == 'c' or gamemode == 3:
            gp_num = data_dict2['Games Played'] + 1
            gw_num = data_dict2['Games Won'] + 1
            data_dict2.update({'Games Played': gp_num, 'Games Drawn': gw_num})
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[2]))
        if gamemode == 'd' or gamemode == 4:
            gp_num = data_dict3['Games Played'] + 1
            gw_num = data_dict3['Games Won'] + 1
            data_dict3.update({'Games Played': gp_num, 'Games Drawn': gw_num})
            content = file.readlines()
            file = open('rpsdata.txt', 'w')
            file.write(json.dumps(content[3]))
        os.system('pause')
        round = 0
    else:
        round = round + 1
        multiround() 

def multiround():
    os.system('cls')
    global max_round
    global player_name
    global data_dict
    global choices
    global player_num
    global gamemode
    global round
    if gamemode == 'b' or gamemode == 2:
        max_round = 3    
    if gamemode == 'c' or gamemode == 3:
        max_round = 5   
    if gamemode == 'd' or gamemode == 4:
        max_round = 10
    os.system('cls')
    print('Best of {}, Round {}'.format(max_round, round))
    player_choice = input('Rock, Paper, or Scissors?: ').lower()
    if not(player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors'):
        print ('INVALID CHOICE.')
        time.sleep(3)
        single()
    if player_num == 1 or player_num == 0:
        print ('Waiting for opponents choice...')
        wait_time = random.randint(3,5)
        time.sleep(wait_time)
        opponent_choice=random.choice(choices)
        opponent_name=random.choice(namelist)
        print ('Your opponent, {}, chose {}.'.format(opponent_name, opponent_choice))
        if player_choice == opponent_choice:
            single_tie()
        elif player_choice == 'rock' and opponent_choice == 'scissors':
            single_win()
        elif player_choice == 'scissors' and opponent_choice == 'paper':
            single_win()
        elif player_choice == 'paper' and opponent_choice == 'rock':
            single_win()
        else:
            single_lose()
    else:
        data_list = []
        data_int = 0
        print('Your Team Members are:')
        team_num = player_num - 1
        for tmp_data in range(team_num):
            tc_str = 'team_choice{}=random.choice(choices)'.format(tmp_data)
            tn_str = 'team_name{}=random.choice(namelist)'.format(tmp_data)
            teamname_print = 'print(team_name{})'.format(tmp_data)
            exec(tc_str)
            exec(tn_str)
            exec(teamname_print)
        playername_num = team_num
        pn_str = 'team_name{}=player_name'.format(playername_num)
        pc_str = 'team_choice{}=player_choice'.format(playername_num)
        exec(pn_str)
        exec(pc_str)
        print(player_name)
        time.sleep(3)
        print('Your Opponents are:')
        for omp_data in range(player_num):
            oc_str = 'opponent_choice{}=random.choice(choices)'.format(omp_data)
            on_str = 'opponent_name{}=random.choice(namelist)'.format(omp_data)
            opponentname_print = 'print(opponent_name{})'.format(omp_data)
            exec(oc_str)
            exec(on_str)
            exec(opponentname_print)
        print('Players are choosing...')
        wait_time = random.randint(3,5)
        time.sleep(wait_time)
        os.system('cls')
        for i in range(player_num):
            teamname_print = 'print(team_name{}, end = \' VS \')'.format(i)
            opponentname_print = 'print(opponent_name{}, end = \':\')'.format(i)
            exec(teamname_print)
            exec(opponentname_print)
            time.sleep(3)
            print(' ')
            print(' ')
            teamchoice_print = 'print(team_name{}, \'chooses\', team_choice{})'.format(i, i)
            exec(teamchoice_print)
            time.sleep(1)
            opponentchoice_print = 'print(opponent_name{}, \'chooses\', opponent_choice{})'.format(i, i)
            exec(opponentchoice_print)
            time.sleep(1)
            condition = '''
if team_choice{} == opponent_choice{}:
    print(\'It was a tie!\')
    data_list.append(\'tie\')
elif team_choice{} == 'rock' and opponent_choice{} == 'scissors':
    print(\'It was a win!\')
    data_list.append(\'win\')
elif team_choice{} == 'paper' and opponent_choice{} == 'rock':
    print(\'It was a win!\')
    data_list.append(\'win\') 
elif team_choice{} == 'scissors' and opponent_choice{} == 'paper':
    print(\'It was a win!\')
    data_list.append(\'win\') 
else:
    print(\'It was a loss.\')
    data_list.append(\'loss\')
            '''.format(i, i, i, i, i, i, i, i)
            exec(condition)
            print(' ')
        for x in range(player_num):
            list_index = data_list[x]
            if list_index == 'win':
                data_int = data_int + 1
            elif list_index == 'loss':
                data_int = data_int - 1
        if data_int > 0:
            single_win()
        if data_int == 0:
            single_tie()
        if data_int < 0:
            single_lose()  

def single_win():
    global player_name
    print ('Congratulations {}, You Win!'.format(player_name))
    file = open('rpsdata.txt', 'w')
    gp_num = data_dict['Games Played'] + 1
    gw_num = data_dict['Games Won'] + 1
    data_dict.update({'Games Played': gp_num, 'Games Won': gw_num})
    content = file.readlines()
    file = open('rpsdata.txt', 'w')
    file.write(json.dumps(content[1]))
    file.close()
    os.system('pause')
    main()

def single_lose():
    global player_name
    print ('Sorry, {}, you lose.'.format(player_name))
    file = open('rpsdata.txt', 'w')
    gp_num = data_dict['Games Played'] + 1
    gw_num = data_dict['Games Lost'] + 1
    data_dict.update({'Games Played': gp_num, 'Games Lost': gw_num})
    content = file.readlines()
    file = open('rpsdata.txt', 'w')
    file.write(json.dumps(content[2]))
    file.close()
    os.system('pause')
    main()

def single_tie():
    global player_name
    print ('Sorry, {}, it was a tie!'.format(player_name))
    file = open('rpsdata.txt', 'w')
    gp_num = data_dict['Games Played'] + 1
    gd_num = data_dict['Games Drawn'] + 1
    data_dict.update({'Games Played': gp_num, 'Games Drawn': gd_num})
    content = file.readlines()
    file = open('rpsdata.txt', 'w')
    file.write(json.dumps(content[3]))
    file.close()
    os.system('pause')
    main()    

def single():
    os.system('cls')
    global player_name
    global data_dict
    global choices
    global player_num
    os.system('cls')
    player_choice = input('Rock, Paper, or Scissors?: ').lower()
    if not(player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors'):
        print ('INVALID CHOICE.')
        time.sleep(3)
        single()
    if player_num == 1 or player_num == 0 or player_num == '':
        print ('Waiting for opponents choice...')
        wait_time = random.randint(3,5)
        time.sleep(wait_time)
        opponent_choice=random.choice(choices)
        opponent_name=random.choice(namelist)
        print ('Your opponent, {}, chose {}.'.format(opponent_name, opponent_choice))
        if player_choice == opponent_choice:
            single_tie()
        elif player_choice == 'rock' and opponent_choice == 'scissors':
            single_win()
        elif player_choice == 'scissors' and opponent_choice == 'paper':
            single_win()
        elif player_choice == 'paper' and opponent_choice == 'rock':
            single_win()
        else:
            single_lose()
    else:
        data_list = []
        data_int = 0
        print('Your Team Members are:')
        team_num = player_num - 1
        for tmp_data in range(team_num):
            tc_str = 'team_choice{}=random.choice(choices)'.format(tmp_data)
            tn_str = 'team_name{}=random.choice(namelist)'.format(tmp_data)
            teamname_print = 'print(team_name{})'.format(tmp_data)
            exec(tc_str)
            exec(tn_str)
            exec(teamname_print)
        playername_num = team_num
        pn_str = 'team_name{}=player_name'.format(playername_num)
        pc_str = 'team_choice{}=player_choice'.format(playername_num)
        exec(pn_str)
        exec(pc_str)
        print(player_name)
        time.sleep(3)
        print('Your Opponents are:')
        for omp_data in range(player_num):
            oc_str = 'opponent_choice{}=random.choice(choices)'.format(omp_data)
            on_str = 'opponent_name{}=random.choice(namelist)'.format(omp_data)
            opponentname_print = 'print(opponent_name{})'.format(omp_data)
            exec(oc_str)
            exec(on_str)
            exec(opponentname_print)
        print('Players are choosing...')
        wait_time = random.randint(3,5)
        time.sleep(wait_time)
        os.system('cls')
        for i in range(player_num):
            teamname_print = 'print(team_name{}, end = \' VS \')'.format(i)
            opponentname_print = 'print(opponent_name{}, end = \':\')'.format(i)
            exec(teamname_print)
            exec(opponentname_print)
            time.sleep(3)
            print(' ')
            print(' ')
            teamchoice_print = 'print(team_name{}, \'chooses\', team_choice{})'.format(i, i)
            exec(teamchoice_print)
            time.sleep(1)
            opponentchoice_print = 'print(opponent_name{}, \'chooses\', opponent_choice{})'.format(i, i)
            exec(opponentchoice_print)
            time.sleep(1)
            condition = '''
if team_choice{} == opponent_choice{}:
    print(\'It was a tie!\')
    data_list.append(\'tie\')
elif team_choice{} == 'rock' and opponent_choice{} == 'scissors':
    print(\'It was a win!\')
    data_list.append(\'win\')
elif team_choice{} == 'paper' and opponent_choice{} == 'rock':
    print(\'It was a win!\')
    data_list.append(\'win\') 
elif team_choice{} == 'scissors' and opponent_choice{} == 'paper':
    print(\'It was a win!\')
    data_list.append(\'win\') 
else:
    print(\'It was a loss.\')
    data_list.append(\'loss\')
            '''.format(i, i, i, i, i, i, i, i)
            exec(condition)
            print(' ')
        for x in range(player_num):
            list_index = data_list[x]
            if list_index == 'win':
                data_int = data_int + 1
            elif list_index == 'loss':
                data_int = data_int - 1
        if data_int > 0:
            single_win()
        if data_int == 0:
            single_tie()
        if data_int < 0:
            single_lose()  

def check():
    global data_dict
    global data_dict1
    global data_dict2
    global data_dict3
    global player_name
    file_check = os.path.isfile('rpsdata.txt')
    if file_check == True:
        file = open('rpsdata.txt', 'r')
        content = file.readlines()
        data_dict = json.loads(content[0])
        data_dict1 = json.loads(content[1])
        data_dict2 = json.loads(content[2])
        data_dict3 = json.loads(content[3])
        player_name = data_dict['Name']
        del data_dict['Name']
        file.close()
        main()
    else:
        print ('Welcome to Rock, Paper, Scissors!')
        name = input('Please enter your name: ').lower()
        file = open('rpsdata.txt', 'w')
        data_dict = {'Name': player_name, 'Games Played': 0, 'Games Won': 0, 'Games Lost': 0, 'Games Drawn': 0}
        data_dict1 = {'Games Played': 0, 'Games Won': 0, 'Games Lost': 0, 'Games Drawn': 0}
        data_dict2 = {'Games Played': 0, 'Games Won': 0, 'Games Lost': 0, 'Games Drawn': 0}
        data_dict3 = {'Games Played': 0, 'Games Won': 0, 'Games Lost': 0, 'Games Drawn': 0}
        file.write(json.dumps(data_dict))
        file.write('\n')
        file.write(json.dumps(data_dict1))
        file.write('\n')
        file.write(json.dumps(data_dict2))
        file.write('\n')
        file.write(json.dumps(data_dict3))
        data_dict = {'Games Played': 0, 'Games Won': 0, 'Games Lost': 0, 'Games Drawn': 0}
        file.close()
        main()

check()
