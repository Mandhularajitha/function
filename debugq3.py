# def numbers_less_than_twenty(list):
#   counter = 0
#   while counter < len(list):
#     item = list[counter]
#     if item > 20:
#       list.remove(item)
#     else:
#       counter += 1
#   return list

# num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

# num_list_sub_20 = numbers_less_than_twenty(num_list)

# print ("Initial list", num_list)
# print ("List that doesn't contain numbers greate than 20", num_list_sub_20)



from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice =[random_move]

    if player_choice == computer_choice:
        print ('Draw!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("rock")
    elif player_choice  == 'paper' and computer_choice == 'scisser':
        print("scissors")
    elif player_choice == 'rock' and computer_choice == 'paper':
        print("paper")
    elif player_choice == 'scissors' and computer_choice == 'scisser':
        print("tie")
    aGain = input('Do you want to play again? (y or n)').strip()
    if moves == 'n':
        break