def drawing(rows,columns,field):
    for row in range(rows+rows-1):
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(columns+columns-1):
                if column%2 == 0:
                    practicalColumn = int(column/2)
                    if column != columns+columns - 2:
                        print(field[practicalColumn][practicalRow],end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|",end="")
        else:
            print("-"*(columns+column-1))
def updateCurrentField(gameColumn,gameRow):
    for column in range(gameColumn):
        columnField.append(" ")
    for row in range(gameRow):
        currentField.append(columnField)
gameColumn = int(input("Please insert the number of column: "))
gameRow = int(input("Plese insert the number of row: "))
currentField = []
columnField = []
updateCurrentField(gameColumn,gameRow)
#currentField = [[" "," "," "],[" "," "," "],[" "," "," "]]
drawing(gameRow,gameColumn,currentField)
Player = 1
while(True):
    moveColumn = int(input("Enter the column:\n "))
    moveRow = int(input("Enter the row:\n "))
    if Player == 1:
        #make move for plyer 1
        if currentField[moveColumn][moveRow] == " ":
            print(currentField[0])
            currentField[moveColumn][moveRow] = "X"
            print(currentField[0])
            print(currentField)
            Player = 2
    else:
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "O"
            print(moveColumn)
            print(moveRow)
            print(currentField)
            Player = 1
    drawing(gameRow,gameColumn,currentField)