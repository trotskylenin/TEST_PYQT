from PyQt4 import uic
from PyQt4.QtCore import *

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.connect(self.ui.Boton, SIGNAL('clicked()'),SLOT('click()'))

    def __del__ ( self ):
        self.ui = None
    
    @pyqtSlot()  
    def click(self):
        self.ui.etiqueta.setText("Hola Mundo!!!")