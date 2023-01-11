import sys
from random import randint

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QLabel)

class DiceGame(QWidget):
    def __init__(self):
        super().__init__()
        self.turn_score = 0
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1
        self.current_roll = 0
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Dice Game')
        
        # Create widgets
        self.roll_button = QPushButton('Roll')
        self.end_turn_button = QPushButton('Save Score / End Turn')
        self.current_roll_label = QLabel('Current Roll: 0')
        self.player1_score_label = QLabel('Player 1 Score: 0')
        self.player2_score_label = QLabel('Player 2 Score: 0')
        self.turn_score_label = QLabel('Player {} Turn Score: 0'.format(self.current_player))
        
        # Create layouts
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.roll_button)
        hbox1.addWidget(self.end_turn_button)
        
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.player1_score_label)
        hbox2.addWidget(self.player2_score_label)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addWidget(self.current_roll_label)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.turn_score_label)
        
        self.setLayout(vbox)
        
        # Connect signals and slots
        self.roll_button.clicked.connect(self.roll)
        self.end_turn_button.clicked.connect(self.endTurn)
        
    def roll(self):
        # Roll the dice and update the current roll and turn score
        self.current_roll = randint(1, 6)
        if self.current_roll == 6:
            self.turn_score = 0
            self.endTurn()
        else:
            self.turn_score += self.current_roll
        
        # Update the labels
        self.current_roll_label.setText('Current Roll: {}'.format(self.current_roll))
        self.turn_score_label.setText('Player {} Turn Score: {}'.format(self.current_player, self.turn_score))
        
    def endTurn(self):
        # Add the turn score to the appropriate player's score
        if self.current_player == 1:
            self.player1_score += self.turn_score
        else:
            self.player2_score += self.turn_score
        
        # Switch players and reset the turn score
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
        self.turn_score = 0
        
        # Update the labels
        self.current_roll_label.setText('Current Roll: 0')
        self.player1_score_label.setText('Player 1 Score: {}'.format(self.player1_score))
        self.player2_score_label.setText('Player 2 Score: {}'.format(self.player2_score))
        self.turn_score_label.setText('Player {} Turn Score: 0'.format(self.current_player))
    
    def checkForWinner(self):
        if self.player1_score >= 40:
            print('Player 1 wins!')
        elif self.player2_score >= 40:
            print('Player 2 wins!')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = DiceGame()
    game.show()
    sys.exit(app.exec_())
