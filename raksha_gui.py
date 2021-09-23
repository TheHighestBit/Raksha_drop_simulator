import sys
from random import choice, randint
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QTimer
from raksha import calculate_drop

stats = {"spirit weed seeds": 0, "Carambola seeds": 0, "golden dragonfruit seeds": 0, "small blunt rune salvage": 0, "medium spiky orikalkum salvage": 0, "huge plated orikalkum salvage": 0, "black dragonhide": 0, "onyx dust": 0, "dinosaur bones": 0, "crystal keys": 0, "inert adrenaline crystals": 0, "sirenic scales": 0, "soul runes": 0, "dark/light animica stone spirits": 0, "Greater ricochet ability codex": 0, "Greater chain ability codex": 0, "Divert ability codex": 0, "Shadow spike": 0, "Laceration boots": 0, "Blast diffusion boots": 0, "Fleeting boots": 0}
format_str = '''
{} kills

{} laceration boots
{} blast diffusion boots
{} fleeting boots
{} shadow spikes
{} greater ricochet ability codices
{} greater chain ability codices
{} divert ability codices
-------------------------------------
{} onyx dust
{} spirit weed seeds
{} Carambola seeds
{} golden dragonfruit seeds
{} small blunt rune salvage
{} medium spiky orikalkum salvage
{} huge plated orikalkum salvage
{} black dragonhide
{} dinosaur bones
{} crystal keys
{} inert adrenaline crystals
{} sirenic scales
{} soul runes
{} dark/light animica stone spirits
'''
rare_drops = ["Shadow spike", "Divert ability codex", "Greater ricochet ability codex", "Greater chain ability codex", "Laceration boots", "Blast diffusion boots", "Fleeting boots"]

class Raksha(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Raksha')
        self.setGeometry(500, 200, 1000, 1000)
        self.kills = 0
        self.kills_per_turn = 1 #How many kills per button press, the default is 1

        v_box = QtWidgets.QVBoxLayout()

        self.button = QPushButton('Calculate drop', self)
        self.button.setToolTip("Kill {} Rakshas".format(self.kills_per_turn))
        self.button.resize(500, 100)
        self.button.move(self.frameGeometry().width() // 2 - 200, 100)
        self.button.setFont(QFont('Arial', 10))
        self.button.clicked.connect(self.on_click)

        self.label1 = QLabel(self)
        self.label1.setText("YOU GOT THIS!")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setStyleSheet("background-color:cyan")
        self.label1.setFont(QFont('Arial', 15))
        self.label1.show()

        self.label2 = QLabel(self)
        self.label2.setText(format_str.format(self.kills, stats["Laceration boots"], stats["Blast diffusion boots"], stats["Fleeting boots"], stats["Shadow spike"], stats["Greater ricochet ability codex"], stats["Greater chain ability codex"], stats["Divert ability codex"], stats["onyx dust"], stats["spirit weed seeds"], stats["Carambola seeds"], stats["golden dragonfruit seeds"], stats["small blunt rune salvage"], stats["medium spiky orikalkum salvage"], stats["huge plated orikalkum salvage"], stats["black dragonhide"], stats["dinosaur bones"], stats["crystal keys"], stats["inert adrenaline crystals"], stats["sirenic scales"], stats["soul runes"], stats["dark/light animica stone spirits"]))
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("background-color:cyan")
        self.label2.setFont(QFont('Arial', 12))
        self.label2.show()

        v_box.addWidget(self.button)
        v_box.addWidget(self.label1, 33)
        v_box.addWidget(self.label2)
        self.setLayout(v_box)
        self.show()

    def on_click(self):
        for _ in range(self.kills_per_turn):
            self.label1.setStyleSheet("background-color:cyan") #If last drop was a rare, the background is purple so we need to reset the color
            self.kills += 1
            drop = calculate_drop()
            drop2 = None
            if drop in rare_drops:
                drop2 = calculate_drop()
                while drop2 in rare_drops:
                    drop2 = calculate_drop()

                self.label1.setStyleSheet("background-color:pink")
                self.label1.setText("You received a {} drop!\nYou received {}".format(drop, drop2))
                stats[drop] += 1
                stats[drop2[drop2.index(' ') + 1:]] += int(drop2[:drop2.index(' ')])
                self.label2.setText(format_str.format(self.kills, stats["Laceration boots"], stats["Blast diffusion boots"], stats["Fleeting boots"], stats["Shadow spike"], stats["Greater ricochet ability codex"], stats["Greater chain ability codex"], stats["Divert ability codex"], stats["onyx dust"], stats["spirit weed seeds"], stats["Carambola seeds"], stats["golden dragonfruit seeds"], stats["small blunt rune salvage"], stats["medium spiky orikalkum salvage"], stats["huge plated orikalkum salvage"], stats["black dragonhide"], stats["dinosaur bones"], stats["crystal keys"], stats["inert adrenaline crystals"], stats["sirenic scales"], stats["soul runes"], stats["dark/light animica stone spirits"]))
                self.button.setEnabled(False)
                QTimer.singleShot(1000, lambda: self.button.setDisabled(False)) #After getting a rare drop, the button will go dromant for n amount of ms.
            else:
                self.label1.setText("You received {}".format(drop))
                stats[drop[drop.index(' ') + 1:]] += int(drop[:drop.index(' ')])
                self.label2.setText(format_str.format(self.kills, stats["Laceration boots"], stats["Blast diffusion boots"], stats["Fleeting boots"], stats["Shadow spike"], stats["Greater ricochet ability codex"], stats["Greater chain ability codex"], stats["Divert ability codex"], stats["onyx dust"], stats["spirit weed seeds"], stats["Carambola seeds"], stats["golden dragonfruit seeds"], stats["small blunt rune salvage"], stats["medium spiky orikalkum salvage"], stats["huge plated orikalkum salvage"], stats["black dragonhide"], stats["dinosaur bones"], stats["crystal keys"], stats["inert adrenaline crystals"], stats["sirenic scales"], stats["soul runes"], stats["dark/light animica stone spirits"]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Raksha()
    sys.exit(app.exec())