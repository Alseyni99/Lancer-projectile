from numpy import sin, cos, tan
import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QFrame, QPushButton, QRadioButton, QVBoxLayout, QWidget, QLabel, QSlider, QDial, QMenuBar, QMenu, QStatusBar, QAction, QMessageBox
from PyQt5.QtGui import QFont, QColor
from PyQt5 import QtCore 
import pyqtgraph as pg
import numpy as np
from functions import *


class quadratic(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.fram1()
        self.graphics()
        self.fram_input()
        self.fram_plot()
        self.fram2()
        
        

    def initUI(self):
        # this function initiates the graphic interface and sets the parameters of the main window
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle('Trajectoire d\'un projectile')
        self.setGeometry(300, 300, 600, 500)
        
        self.hlayoutgen=QHBoxLayout(self.centralWidget)

    def fram1(self):
        self.frame1=QFrame(self.centralWidget)
        
        self.hlayoutgen.addWidget(self.frame1)

        self.vlayout1=QVBoxLayout(self.frame1)

    def graphics(self):
        self.framegraph=QFrame(self.frame1)
        self.framegraph.setFrameShape(QFrame.StyledPanel)
        self.framegraph.setFrameShadow(QFrame.Raised)
        self.vlayout1.addWidget(self.framegraph)

        self.graph = pg.PlotWidget(self.framegraph)
        self.graph.setGeometry(QtCore.QRect(10, 10, 425, 315))

        self.framegraphlayouthor = QHBoxLayout(self.framegraph)
        self.framegraphlayouthor.addWidget(self.graph)

        self.graph.setLabel('left', 'y')
        self.graph.setLabel('bottom' , 'x')
        self.graph.showGrid(x=True, y=True)


    def fram_input(self):
        self.frame_input = QFrame(self.frame1)
        self.frame_input.setMaximumSize(QtCore.QSize(16777215, 75))
        

        self.frame_a = QFrame(self.frame_input)
        
        self.alabel=QLabel(self.frame_a)
        self.alabel.setText('v0')

        self.lineEdit_a = QLineEdit(self.frame_a)
        self.lineEdit_a.setPlaceholderText("en m/s")
        
        self.hlayout_a=QHBoxLayout(self.frame_a)
        self.hlayout_a.addWidget(self.alabel)
        self.hlayout_a.addWidget(self.lineEdit_a)


        self.frame_b = QFrame(self.frame_input)   #b=alpha
        

        self.blabel=QLabel(self.frame_b)
        self.blabel.setText('alpha')

        self.lineEdit_b = QLineEdit(self.frame_b)
        self.lineEdit_b.setPlaceholderText("en degré")
        
        self.hlayout_b=QHBoxLayout(self.frame_b)
        self.hlayout_b.addWidget(self.blabel)
        self.hlayout_b.addWidget(self.lineEdit_b)

        self.frame_c = QFrame(self.frame_input)
        

        self.clabel=QLabel(self.frame_c)
        self.clabel.setText('h')

        self.lineEdit_c = QLineEdit(self.frame_c)
        self.lineEdit_c.setPlaceholderText("en m")
        
        self.hlayout_c=QHBoxLayout(self.frame_c)
        self.hlayout_c.addWidget(self.clabel)
        self.hlayout_c.addWidget(self.lineEdit_c)

        self.hlayout_abc=QHBoxLayout(self.frame_input)
        self.hlayout_abc.addWidget(self.frame_a)
        self.hlayout_abc.addWidget(self.frame_b)
        self.hlayout_abc.addWidget(self.frame_c)

        self.vlayout1.addWidget(self.frame_input)

    def fram_plot(self):
        self.frame_plot=QFrame(self.frame1)
        self.frame_plot.setMaximumSize(QtCore.QSize(16777215, 50))

        self.vlayout1.addWidget(self.frame_plot)

        self.hlayoutplot=QHBoxLayout(self.frame_plot)

        self.plotbutton=QPushButton(self.frame_plot)
        self.plotbutton.setText('Plot')
        self.plotbutton.clicked.connect(self.plotgraph)

        self.clearbutton = QPushButton(self.frame_plot)
        self.clearbutton.setText("Clear")
        self.clearbutton.clicked.connect(self.clearzer)
        
        self.hlayoutplot.addWidget(self.plotbutton)
        self.hlayoutplot.addWidget(self.clearbutton)

        

    def fram2(self):
        self.frame2=QFrame(self.centralWidget)
        self.frame2.setMaximumSize(QtCore.QSize(300, 16777215))

        self.hlayoutgen.addWidget(self.frame2)
        
        self.vlayout2=QVBoxLayout(self.frame2)


        self.frameys = QFrame(self.frame2)
        self.vlayout2.addWidget(self.frameys)

        self.yslabel=QLabel(self.frameys)        
        self.yslabel.setText('ys')
        self.lineEdit_ys=QLineEdit(self.frameys)
        self.lineEdit_ys.setReadOnly(True)
        self.lineEdit_ys.resize(80,20)

        self.hlayoutys=QHBoxLayout(self.frameys)
        self.hlayoutys.addWidget(self.yslabel)
        self.hlayoutys.addWidget(self.lineEdit_ys)

    
        self.framexs=QFrame(self.frame2)
        self.vlayout2.addWidget(self.framexs)

        self.xslabel=QLabel(self.frame2)
        self.xslabel.setText('xs')
        self.lineEdit_xs=QLineEdit(self.framexs)
        self.lineEdit_xs.setReadOnly(True)
        
        self.hlayoutxs = QHBoxLayout(self.framexs)
        self.hlayoutxs.addWidget(self.xslabel)
        self.hlayoutxs.addWidget(self.lineEdit_xs)

        self.framets=QFrame(self.frame2)
        self.vlayout2.addWidget(self.framets)

        self.tslabel=QLabel(self.frame2)
        self.tslabel.setText('ts')
        self.lineEdit_ts=QLineEdit(self.framets)
        self.lineEdit_ts.setReadOnly(True)
        
        self.hlayoutts = QHBoxLayout(self.framets)
        self.hlayoutts.addWidget(self.tslabel)
        self.hlayoutts.addWidget(self.lineEdit_ts)

        self.rootbutton = QPushButton(self.frame2)
        self.rootbutton.setText('Roots')

        self.vlayout2.addWidget(self.rootbutton)
        self.rootbutton.clicked.connect(self.roots)

    def roots(self):
        listline_Editabc = [self.lineEdit_a,self.lineEdit_b,self.lineEdit_c]
        for i in listline_Editabc:
            if i.text() == '':
                i.setText('0')

        self.value_a = int(self.lineEdit_a.text())
        self.value_b = int(self.lineEdit_b.text())
        self.value_c = int(self.lineEdit_c.text())

        if (self.value_a == 0 and self.value_b == 0 and self.value_c == 0):
            self.message = QMessageBox().information(self,"information","Il n'y a pas de mouvement si la vitesse initiale est nulle",QMessageBox.Ok)

        if (self.value_a == 0 and self.value_b != 0):
            self.message = QMessageBox().information(self,"information","Il n'y a pas de mouvement si la vitesse initiale est nulle",QMessageBox.Ok)


        if (self.value_a == 0 and self.value_b == 0 and self.value_c != 0):
            self.message1 = QMessageBox().information(self,"information","There are no solutions to the equation",QMessageBox.Ok)
        
        if (self.value_a != 0) :
            v = self.value_a
            alph = (np.pi*self.value_b)/180
            h = self.value_c
            value_ys = 0.5*((v*sin(alph))**2)/10
            self.lineEdit_ys.setText(str(value_ys))

            roots = solve(trans_quad(-10/(2*(v*cos(alph))**2), tan(alph),value_ys-h))
            for elmt in roots:
                if elmt > 0:
                    xs = elmt
            self.lineEdit_xs.setText(str(xs))

            ts = xs/(v*cos(alph))
            self.lineEdit_ts.setText(str(ts))


            #self.lineEdit_x2.setText(str(rootscompute[1]))

    def clearzer(self):
        listline_Edit=[self.lineEdit_a,self.lineEdit_b,self.lineEdit_c,self.lineEdit_x1,self.lineEdit_x2]
        for i in listline_Edit:
            i.clear()
        
    
    def plotgraph(self):
        listline_Editabc = [self.lineEdit_a,self.lineEdit_b,self.lineEdit_c]
        for i in listline_Editabc:
            if i.text() == '':
                i.setText('0')
        

        self.value_a = int(self.lineEdit_a.text())
        self.value_b = int(self.lineEdit_b.text())
        self.value_c = int(self.lineEdit_c.text())

        if (self.value_a == 0 and self.value_b == 0 and self.value_c != 0):
            self.message1 = QMessageBox().information(self,"Error","Graph can't be displayed")
        else:
            v0 = self.value_a
            alph = (np.pi*self.value_b)/180
            h = self.value_c
            a = -10/(2*(v0*cos(alph))**2)
            b = tan(alph)
            c = h
            value_ys = 0.5*((v0*sin(alph))**2)/10
            xp = (2*v0**2*sin(2*alph))/10
            

            range_x = np.linspace(0,xp,1000)
            y = obtainequation(trans_quad(a, b, c),range_x)
            self.graph.setBackground('w')
            pen = pg.mkPen(color=(255, 0, 0))
            self.graph.setYRange(0, value_ys+2, padding=0)
            self.graph.setXRange(0, xp+1, padding=0)

            self.graph.plot(range_x,y,pen=pen)



