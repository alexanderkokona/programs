# import statements
from doctest import Example
import sys, os
import pandas as pd
from datetime import datetime
from pymongo import MongoClient
from PyQt5.QtCore import QDate, Qt, QRect
from PyQt5.QtGui import (
    QFont,
    QColor,
    QBrush,
    QPainter,
    QTextCharFormat,

)
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QTextEdit,
    QApplication,
    QTableWidget,
    QCalendarWidget,
    QTableWidgetItem,
)

# database of choice - MogoDb
# import MongoClient database from Pymongo
client = MongoClient("localhost", 27017)
db     = client["mydb"]
coll   = db["appointments"]

#build a calandar class
class Calendar(QCalendarWidget):     
    def __init__(self, parent=None):
        super(Calendar, self).__init__(parent)

# pulls all appointments from the database, sorts the entires in Date order
# and ignores all appointments before the current date.
# Also, the year is dropped from the date for ease in displaying
class Appointments():

    def appointments(self):
        appts = []
        now   = datetime.now()
        today = now.strftime('%m-%d-%Y')

        data = coll.find({}, {'_id': 0, 'date': 1, 'time': 1, 'place': 1, 'note': 1}).sort('date')        
        for _d in data:
            if _d['date'] < today:
                pass
            else:
                date, time, place, note = _d['date'][:5], _d['time'], _d['place'], _d['note']                
                appts.append([date, time, place, note])
        return appts
    
# creates the class for the GUI
# we define the where and size of the window and initialize class variables
    class Example(QWidget):    
        def __init__(self):
            super(Example, self).__init__()
            self.initUI()


    def initUI(self):
        self.left   = 1138
        self.top    = 30
        self.width  = 302
        self.height = 370
        self.appointments = Appointments()
        self.cal = QCalendarWidget( self )
        format = QTextCharFormat()

# define the window (all black, no window header, borders, or scroll bars)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

# button to exit the program
        qdim = "QPushButton {color: rgba(54, 136, 200, 250); background-color: black; }"

# define the fonts to be used
        canda_10 = QFont("Candalara", 10)
        canda_11 = QFont( "Candalara", 11 )
        segoe_9  = QFont('Segoe UI', 9)

# reformats color of numbers to designate weekend days
        format   = self.cal.weekdayTextFormat( Qt.Saturday)
        format.setForeground( QBrush( Qt.darkCyan, Qt.SolidPattern ) )
        self.cal.setWeekdayTextFormat( Qt.Saturday, format )
        self.cal.setWeekdayTextFormat( Qt.Sunday, format )

# format the words and numbers
        self.cal.setVerticalHeaderFormat( self.cal.NoVerticalHeader )
        self.cal.setGridVisible(False)
        self.cal.setGeometry(0, 0, 292, 221)
        self.cal.setFont(segoe_9)

# Customization 
# The first setting gives the widget its black background, date highlight color, date highlight background color, and font color. 
# The second setting alters the background of the day name header. 
# The third setting customizes the month, year header, 
# and the last two lines change the arrow graphics used for selecting the previous/next month.
        self.cal.setStyleSheet(
            "QCalendarWidget QAbstractItemView{background-color: black;  color: rgba(162,201,229,255); selection-background-color: rgb(20,20,20); selection-color: rgb(200,150,255); selection-border: 1px solid black;}"
   
            "QCalendarWidget QWidget{alternate-background-color: rgb(20, 20, 20); color: gray;}"
    
            "QCalendarWidget QToolButton{background-color: black; color: rgb(125,125,125); font-size: 14px; font: bold; width: 70px; border: none;}"
    
            "QCalendarWidget QToolButton#qt_calendar_prevmonth{qproperty-icon: url(left_arrow.png);}"
    
            "QCalendarWidget QToolButton#qt_calendar_nextmonth{qproperty-icon: url(right_arrow.png);}"
)
        
# initialize exit button and the functionthatruns when a date is clicked
# use the qdim style variable
        self.button = QPushButton(self)
        self.button.setStyleSheet(qdim)
        self.button.setFont(canda_11)
        self.button.setText("EXIT")
        self.button.setGeometry(10, 240, 281, 90)
        self.button.clicked.connect(self.exit)
        self.cal.clicked[QDate].connect(self.showDate)

# creates a section of GUI that shows upcoming appointments as a table
# shows next three appointments, is scrollable
        self.appt_table = QTableWidget( self )
        self.appt_table.setGeometry( QRect( 10, 240, 281, 90 ) )
        self.appt_table.setStyleSheet(
        "QTableWidget {color: rgb(135,135,135); background-color: black; border: none;}"
)
        self.appt_table.horizontalHeader().hide()
        self.appt_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.appt_table.setFont( canda_10 )
        self.appt_table.verticalHeader().setVisible( False )

# get the data from the database and input it into a Pandas DataFrame
        data = self.appointments.appointments()
        df = pd.DataFrame(data)
# builds the table for display from the Pandas DataFrame
        self.display_data(df)
        self.show()

# The function called in third line above
        def display_data(self, var):
            self.appt_table.setColumnCount( len( var.columns ) )
            self.appt_table.setRowCount( len( var.index ) )

            for i in range( len( var.index ) ):
                for j in range( len( var.columns ) ):
                    self.appt_table.setItem( i, j, QTableWidgetItem( str( var.iat[i, j] ) ) )
            self.appt_table.resizeColumnsToContents()

# showDate() is called
# If a past date is clicked on, nothing happens (besides the new date being highlighted). 
# If the present or future date is clicked, a new window is called
        def showDate(self, date):
            now =  QDate.currentDate()
            select_date = self.cal.selectedDate()
            if select_date < now:
                pass
            else:
                string_date = str(select_date.toPyDate())
                self.event_form(string_date)
# 