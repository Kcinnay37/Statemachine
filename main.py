# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from VendingMachine import VendingMachine

if __name__ == "__main__":
    vending = VendingMachine(2)
    vending.insertCoin()
    vending.insertCoin()
    vending.dispense_product()
    print(vending.currCoins)
    vending.get_graph(show_roi=True).draw("my_roi_diagram", format="png")

    #app = QApplication(sys.argv)

    #sys.exit(app.exec_())
