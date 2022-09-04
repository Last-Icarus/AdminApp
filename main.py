import json
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui        
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QTableWidget, QTableWidgetItem,QHeaderView)

# Меню

class ARM:
    def __init__(self,phone_number,computer,cabinet,person,) -> None:
        pass

class Employee:
    def __init__(self,name,details):
        self.name = name
        self.details = details
        self.accounts = []
    
    def data_append(self,name,login,password):
        self.accounts.append({'Name:':name,'Login:':login,'Password:':password})


class Computer:
    def __init__(self,owner,CPU,GPU,disk,installed_programs,details,data):
        self.owner = owner
        self.CPU = CPU
        self.GPU = GPU
        self.disk = disk
        self.installed_programs = ','.join(installed_programs)
        self.details = details
        self.data = [self.owner,self.CPU,self.GPU,self.disk,self.installed_programs,self.details]

program_list = ['Dr.Web','MC Office','AIDA','AnyDesk','GitHub Desktop']


Human = Employee('Michael', None)
comp = Computer(Human.name,'IntelCore i5','RTX 2060','256GB SSD, 2TB HDD',program_list,'None','None')

Human.data_append('mail.ru','mishanik20021@mail.ru','password')
Human.data_append('vk.ru','mishanik20021@mail.ru','vk_password')




app = QApplication()

table = QTableWidget()
table.setRowCount(1)
table.setColumnCount(6)
table.setHorizontalHeaderLabels(["Owner", "CPU", "GPU","Disk","Installed Programms", 'Details'])
table.setColumnWidth(3, 150)
table.setColumnWidth(4, 290)


k = 0
for i in comp.data:
    print(i)
    table.setItem(0,k,QTableWidgetItem(i))
    k+=1




table.resize(900, 600)
table.show()
sys.exit(app.exec())
