    from tabulate import tabulate
    def instructions():
        print(f''' 
    A simple program to print a tabular form of transactions 
    Input names of users in the transactions. Flow of money is from Left to Top 
    i.e Y- axis has to pay X - axis correspondent ''')
        print()

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

    def generate_board():
        users = users_init()
        board = [[0 for i in range(len(users))] for i in range(len(users))]
        return board,users


    def print_board(board,users):
        print("  "*2 , end = "")
        print(*users,sep = "   ")
        i = 0
        for row in board:
            print(users[i],end = " ")
            for item in row:
                print(f'| {item} ' ,end = "")
            print('|')
            i += 1


    def payments(board,users):
        head = users
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
                print(tabulate(board,headers=head,tablefmt="grid"))
            else:
                flag = False
    instructions()
    board , users = generate_board()
    # print_board(board,users)
    print(tabulate(board,headers=users,tablefmt="grid"))
    payments(board,users)
    # print_board(board,users)
    print(tabulate(board,headers=users,tablefmt="grid"))

