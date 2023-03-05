from tabulate import tabulate

def instructions():
    print(f''' 
A simple program to print a tabular form of transactions 
Input names of users in the transactions. Flow of money is from Left to Top 
i.e Y- axis has to pay X - axis correspondent ''')
    print()

#  Inputs all the users in the transaction
def users_init():
    flag = True
    users = []
    while flag:
        inp = input("Enter user name : ")
        if inp != "":
            users.append(inp)
        else:
            flag = False
    
    return users
# Generating a board based off of user input
def generate_board():
    users = users_init()
    board = [[0 for i in range(len(users))] for i in range(len(users))]
    return board,users

# Visually representing the Expenses
def table_print(board,users):
    visual_board = [row.copy() for row in board]
    head = users[:]
    for i in range(len(users)):
        visual_board[i].insert(0,users[i])
    head.insert(0," ")
    print(tabulate(visual_board,headers=head,tablefmt="grid"))
    print()


# Function to input payments
def payments(board,users):
    flag = True
    while flag:
        col = input("Enter who paid (User name): ")
        if col != "":
            row = input("Enter who all has to pay (User/All): ")
            amount = int(input("Amount to be paid: "))
            col = users.index(col)
            if row != "All":
               row = users.index(row)
               board[row][col] += amount 
            else:
                for row in range(len(users)):
                    if row != col:
                        board[row][col] += amount
            table_print(board,users)
        else:
            flag = False
            print()

# Cancelling out redundant transfers
def simplify(board,users):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] > board[col][row]:
                board[row][col] -= board[col][row]
                board[col][row] = 0
            else:
                board[col][row] -= board[row][col]
                board[row][col] = 0
    table_print(board,users)

# Printing out the final transactions in readable output 
def final_msg(board,users):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != 0:
                print(f'{users[row]} has to pay {users[col]} - {board[row][col]}')
            

instructions()
board , users = generate_board()
table_print(board,users)
payments(board,users)
print(f'*** Final transaction *** ')
simplify(board,users)
final_msg(board,users)
