import math

class Matrix:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.size = self.row * self.col
        self.elements = []

    def createmat(self):
        for i in range(self.row):
            self.elements.append([])
            for j in input().split():
                if "." in j:
                    self.elements[i].append(float(j))
                else:
                    self.elements[i].append(int(j))

    def addMat(self, MatB):
        if self.row == MatB.row and self.col == MatB.col:
            print("The Result is: ")
            for i in range(self.row):
                for j in range(self.col):
                    print(self.elements[i][j] + MatB.elements[i][j], end=" ")
                print()
        else:
            print("Error!! Matrix Cannot be Added")
        print()

    def scalmul(self, scal):
        for i in range(self.row):
            for j in range(self.col):
                self.elements[i][j] = self.elements[i][j] * scal

    def zeromat(self):
        self.elements = []
        for i in range(self.row):
            self.elements.append([])
            for j in range(self.col):
                self.elements[i].append(0)

    def multmat(self, matB):
        if self.col == matB.row:
            zmat = Matrix(self.row, matB.col)
            zmat.zeromat()
            print("The Result is: ")
            for i in range(self.row):
                for j in range(matB.col):
                    for k in range(self.col):
                        zmat.elements[i][j] += self.elements[i][k] * matB.elements[k][j]
            zmat.printmat()
        else:
            print("Error!! Matrix Cannot be Multiplied")
        print()

    def transmndg(self):
        trmat = Matrix(self.col, self.row)
        trmat.zeromat()
        for i in range(self.row):
            for j in range(self.col):
                trmat.elements[j][i] = self.elements[i][j]
        return trmat

    def transsddg(self):
        trmat = Matrix(self.col, self.row)
        trmat.zeromat()
        for i in range(self.row):
            for j in range(self.col):
                trmat.elements[i][j] = self.elements[self.row - j - 1][self.col - i - 1]
        trmat.printmat()

    def transverln(self):
        trmat = Matrix(self.row, self.col)
        trmat.zeromat()
        for i in range(self.row):
            for j in range(self.col):
                trmat.elements[i][j] = self.elements[i][self.col - j - 1]
        trmat.printmat()

    def transhorln(self):
        trmat = Matrix(self.row, self.col)
        trmat.zeromat()
        for i in range(self.row):
            for j in range(self.col):
                trmat.elements[i][j] = self.elements[self.row - i - 1][j]
        trmat.printmat()

    def printmat(self):
        print("The Result is: ")
        for i in range(self.row):
            for j in range(self.col):
                print('{:6.2f}'.format(truncate(self.elements[i][j], 2)), end=" ")
            print()
        print()

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def determinant(matlist, dtmt=0):
    matord = len(matlist)
    if matord == 2:
        return matlist[0][0] * matlist[1][1] - matlist[0][1] * matlist[1][0]
    else:
        for j in range(matord):
            submat = cheat_copy(matlist)
            submat.pop(0)
            for col in submat:
                col.pop(j)
            dtmt += pow(-1, 0 + j) * matlist[0][j] * determinant(submat)
    return dtmt

def cofactormat(matlst, comat, ord):
    if ord == 2:
        for r in range(ord):
            for k in range(ord):
                comat.elements[r][k] = pow(-1, r + k) * matlst[ord - r - 1][ord - k - 1]
    else:
        for r in range(ord):
            for k in range(ord):
                submat = cheat_copy(matlst)
                submat.pop(r)
                for col in submat:
                    col.pop(k)
                comat.elements[r][k] = pow(-1, r+k) * determinant(submat)
    return comat

def cheat_copy(nested_content):
    return eval(repr(nested_content))

def display():
    print("1.  Add Matrices")
    print("2.  Multiply matrix by a constant")
    print("3.  Multiply matrices")
    print("4.  Transpose Matrix")
    print("5.  Calculate a Determinant")
    print("6.  Inverse Matrix")
    print("0.  Exit")

def readmatrix(instr):
    r, c = [int(num) for num in input(instr).split()]
    mat1 = Matrix(r, c)
    return mat1

def disptrans():
    print("\n1.   Main diagonal")
    print("2.   Side diagonal")
    print("3.   Vertical line")
    print("4.   Horizontal line")
    trch = int(input("Your choice: > ").strip())
    instr = "Enter Size of Matrix: > "
    matt = readmatrix(instr)
    print("Enter Matrix Values: ")
    matt.createmat()
    if trch == 1:
        matt = matt.transmndg()
        matt.printmat()
    elif trch == 2:
        matt.transsddg()
    elif trch == 3:
        matt.transverln()
    elif trch == 4:
        matt.transhorln()
    else:
        print("Wrong choice ... back tp main screen")


# Main Body Starts
user_ch = 1

while user_ch != 0:  # loop continues until user enters "0"
    display()
    user_ch = int(input("Your choice: > ").strip())
    if user_ch == 1:  # addition of two matrices
        str1 = "Enter Size of First Matrix: > "
        matA = readmatrix(str1)
        print("Enter First Matrix Values: ")
        matA.createmat()
        str1 = "Enter Size of Second Matrix: > "
        matB = readmatrix(str1)
        print("Enter Second Matrix Values: ")
        matB.createmat()
        matA.addMat(matB)
    elif user_ch == 2:  # scalar multiplication of a matrix
        str1 = "Enter Size of Matrix: > "
        matA = readmatrix(str1)
        print("Enter Matrix Values: ")
        matA.createmat()
        consts = input("Enter constant: > ").strip()
        if "." in consts:
            const = float(consts)
        else:
            const = int(consts)
        matA.scalmul(const)
        matA.printmat()
    elif user_ch == 3:      # matrix multiplication of two matrices
        str1 = "Enter Size of First Matrix: > "
        matA = readmatrix(str1)
        print("Enter First Matrix Values: ")
        matA.createmat()
        str1 = "Enter Size of Second Matrix: > "
        matB = readmatrix(str1)
        print("Enter Second Matrix Values: ")
        matB.createmat()
        matA.multmat(matB)
    elif user_ch == 4:      # transpose of a matrix
        disptrans()
    elif user_ch == 5:      # determinant of a square matrix
        str1 = "Enter Size of Matrix: > "
        matD = readmatrix(str1)
        print("Enter Matrix Values: ")
        matD.createmat()
        if matD.row == matD.col >= 2:
            matlist = matD.elements
            print("The Result is: ")
            print(determinant(matlist), '\n')
        elif matD.row == matD.col == 1:
            me = matD.elements
            dtmt = me[0][0]
            print("The result is : ", '\n', dtmt)
        else:
            print("Error!! No Determinant exists")
    elif user_ch == 6:      # Inverse of a square matrix
        str1 = "Enter Size of Matrix: > "
        matI = readmatrix(str1)
        print("Enter Matrix Values: ")
        matI.createmat()
        if matI.row == matI.col >= 2:
            matlist = matI.elements
            dtmt = determinant(matlist)
            if dtmt == 0:
                print("This matrix doesn't have a inverse")
            else:
                comatz = Matrix(matI.row, matI.col)
                comatz.zeromat()
                adjmat = cofactormat(matlist, comatz, matI.row).transmndg()
                adjmat.scalmul(1 / dtmt)
                adjmat.printmat()
        else:
            dtmt = matI.elements[0][0]
            if dtmt == 0:
                print("This matrix doesn't have a inverse")
            else:
                invmat = Matrix(matI.row, matI.col)
                invmat.zeromat()
                invmat.elements[0][0] = matI.elements[0][0] / dtmt
                invmat.printmat()

print("Thank you for using my Matrix program")
