#Last Editor: Mateo Herrera 01/02/2024


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys
import operator

app = QApplication(sys.argv)


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


#Node Class- all items such as operations and numbers
class Node:
    def __init__(self,content):
        self.content = content
        self.next = None
        self.prev = None

#Queue Class
#Enqueue: adds node to queue
#Dequeue: removes node from queue
#peek: checks the top item in the queue
#Clear: clears the queue
#Check_len: checks the length of the queue
#Check_if_empty: checks if queue is empty and returns boolean
class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.len = 0
        
    def enqueue(self,content):
        node = Node(content)
        if self.top == None:
            self.top = node
            self.bottom = node
        else:
            self.bottom.prev = node
            node.next = self.bottom
            self.bottom = node
        self.len += 1

    
    def dequeue(self):
        item = self.top
        if self.top.prev == None:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.prev
        self.len -= 1
        return item

    def peek(self):
        print(self.top.content)

    def Clear(self):
        self.top = None
        self.bottom = None
        self.len = 0
    
    def Check_if_empty(self):
        if self.len == 0:
            return True
        else:
            return False
        
    def Check_len(self):
        return self.len




 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Calculator')
        self.setFixedSize(400, 400)

        #Queue
        self.q = Queue()


        #The current number and the string version
        self.curr_stringNUM = str()
        self.number = float()

        #display screen
        self.displayoutput = QLabel('0',self)
        self.displayoutput.setFont(QFont('Bold Arial font',12))
        self.displayoutput.setGeometry(0,0,220,50)
        self.displayoutput.move(27,25) 
        self.displayoutput.setStyleSheet("border: 1px solid black")       

        #Reset
        self.resetbutton = QPushButton('CE',self)
        self.resetbutton.setGeometry(0,0,75,75)
        self.resetbutton.move(25,300)

        self.resetbutton.clicked.connect(self.ClearFunc)

        #Operations
        self.multiplybutton = QPushButton('X',self)
        self.multiplybutton.setGeometry(0,0,75,75)
        self.multiplybutton.move(300,225)
        self.dividebutton = QPushButton('/',self)
        self.dividebutton.setGeometry(0,0,75,75)
        self.dividebutton.move(300,300)
        self.addbutton = QPushButton('+',self)
        self.addbutton.setGeometry(0,0,75,75)
        self.addbutton.move(300,75)
        self.subtractbutton = QPushButton('-',self)
        self.subtractbutton.setGeometry(0,0,75,75)
        self.subtractbutton.move(300,150)
        self.equalbutton = QPushButton('=',self)
        self.equalbutton.setGeometry(0,0,75,50)
        self.equalbutton.move(300,25)

        
        self.equalbutton.clicked.connect(lambda: self.calculate(self.curr_stringNUM))
        self.addbutton.clicked.connect(lambda: self.addition_op(self.curr_stringNUM))
        self.subtractbutton.clicked.connect(lambda: self.subtraction_op(self.curr_stringNUM))
        self.dividebutton.clicked.connect(lambda: self.division_op(self.curr_stringNUM))
        self.multiplybutton.clicked.connect(lambda: self.multiply_op(self.curr_stringNUM))
        

        #Numbers
        self.onebutton = QPushButton('1',self)
        self.onebutton.setGeometry(0,0,75,75)
        self.onebutton.move(25,75)
        self.twobutton = QPushButton('2',self)
        self.twobutton.setGeometry(0,0,75,75)
        self.twobutton.move(100,75)
        self.threebutton = QPushButton('3',self)
        self.threebutton.setGeometry(0,0,75,75)
        self.threebutton.move(175 ,75)

        self.onebutton.clicked.connect(lambda: self.number_clicked("1"))
        self.twobutton.clicked.connect(lambda: self.number_clicked("2"))
        self.threebutton.clicked.connect(lambda: self.number_clicked("3"))


        
        self.fourbutton = QPushButton('4',self)
        self.fourbutton.setGeometry(0,0,75,75)
        self.fourbutton.move(25,150)
        self.fivebutton = QPushButton('5',self)
        self.fivebutton.setGeometry(0,0,75,75)
        self.fivebutton.move(100,150)
        self.sixbutton = QPushButton('6',self)
        self.sixbutton.setGeometry(0,0,75,75)
        self.sixbutton.move(175 ,150)

        self.fourbutton.clicked.connect(lambda: self.number_clicked("4"))
        self.fivebutton.clicked.connect(lambda: self.number_clicked("5"))
        self.sixbutton.clicked.connect(lambda: self.number_clicked("6"))


        self.sevenbutton = QPushButton('7',self)
        self.sevenbutton.setGeometry(0,0,75,75)
        self.sevenbutton.move(25,225)
        self.eightbutton = QPushButton('8',self)
        self.eightbutton.setGeometry(0,0,75,75)
        self.eightbutton.move(100,225)
        self.ninebutton = QPushButton('9',self)
        self.ninebutton.setGeometry(0,0,75,75)
        self.ninebutton.move(175 ,225)

        self.sevenbutton.clicked.connect(lambda: self.number_clicked("7"))
        self.eightbutton.clicked.connect(lambda: self.number_clicked("8"))
        self.ninebutton.clicked.connect(lambda: self.number_clicked("9"))


        self.zerobutton = QPushButton('0',self)
        self.zerobutton.setGeometry(0,0,75,75)
        self.zerobutton.move(100,300)
        self.decimalbutton = QPushButton('.',self)
        self.decimalbutton.setGeometry(0,0,75,75)
        self.decimalbutton.move(175,300)

        self.zerobutton.clicked.connect(lambda: self.number_clicked('0'))
        self.decimalbutton.clicked.connect(lambda: self.number_clicked('.'))

#When CE button is clicked resests everything
    def ClearFunc(self):
        self.q.Clear()
        self.curr_stringNUM = str('0')
        self.displayoutput.setText(self.curr_stringNUM)
        self.number = float()

#function called when a number button is clicked
    def number_clicked(self,number): 
        if self.curr_stringNUM == str('0'):
            self.curr_stringNUM = str(number)
        else:
            self.curr_stringNUM = self.curr_stringNUM + str(number)
        self.displayoutput.setText(self.curr_stringNUM)
    
# function called when the equals button is pressed or the queue includes more than 2 nums 
    def calculate(self,lastnum):
        try:
            self.number = float(lastnum)
        except ValueError:
            self.number = float(0)
        self.q.enqueue(self.number)

        operation = None
        Total = None
        while self.q.Check_if_empty() == False:
            item = self.q.dequeue().content
            if item == '+':
                operation = operator.add
            elif item == '-':
                operation = operator.sub
            elif item == '/':
                operation = operator.truediv
            elif item == '*':
                operation = operator.mul
            else:
                if Total == None:
                    Total = float(item)
                else:
                    Total = operation(Total,item)

        self.curr_stringNUM = str(Total)
        self.displayoutput.setText(self.curr_stringNUM)
        return Total

        
        


#Opertation functions which are called when the OP button is clicked
    def addition_op(self,number):
        try:
            self.number = float(number)
        except ValueError:
            self.number = float(0)
        if self.q.Check_len() >= 2:
            self.number = self.calculate(self.number)
        self.q.enqueue(self.number)
        self.q.enqueue('+')
        self.curr_stringNUM = str()

    def subtraction_op(self,number):
        try:
            self.number = float(number)
        except ValueError:
            self.number = float(0)
        if self.q.Check_len() >= 2:
            self.number = self.calculate(self.number)  
        self.q.enqueue(self.number)
        self.q.enqueue('-')
        self.curr_stringNUM = str()

    def multiply_op(self,number):
        try:
            self.number = float(number)
        except ValueError:
            self.number = float(0)
        if self.q.Check_len() >= 2:
            self.number = self.calculate(self.number)
        self.q.enqueue(self.number)
        self.q.enqueue('*')
        self.curr_stringNUM = str()

    def division_op(self,number):
        try:
            self.number = float(number)
        except ValueError:
            self.number = float(0)
        if self.q.Check_len() >= 2:
            self.number = self.calculate(self.number)
        self.q.enqueue(self.number)
        self.q.enqueue('/')
        self.curr_stringNUM = str()
        
    

window = MainWindow()
window.show()
app.exec()