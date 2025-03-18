from PyQt6.QtWidgets import QMainWindow
from calc import Ui_MainWindow

class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.expression = ""

    def initUI(self):
        self.btn_0.clicked.connect(lambda: self.append_number('0'))
        self.btn_1.clicked.connect(lambda: self.append_number('1'))
        self.btn_2.clicked.connect(lambda: self.append_number('2'))
        self.btn_3.clicked.connect(lambda: self.append_number('3'))
        self.btn_4.clicked.connect(lambda: self.append_number('4'))
        self.btn_5.clicked.connect(lambda: self.append_number('5'))
        self.btn_6.clicked.connect(lambda: self.append_number('6'))
        self.btn_7.clicked.connect(lambda: self.append_number('7'))
        self.btn_8.clicked.connect(lambda: self.append_number('8'))
        self.btn_9.clicked.connect(lambda: self.append_number('9'))
        self.btn_dot.clicked.connect(lambda: self.append_number('.'))
        self.btn_plus.clicked.connect(lambda: self.append_operator('+'))
        self.btn_minus.clicked.connect(lambda: self.append_operator('-'))
        self.btn_mul.clicked.connect(lambda: self.append_operator('*'))
        self.btn_div.clicked.connect(lambda: self.append_operator('/'))
        self.btn_equal.clicked.connect(self.calculate_result)
        self.btn_all_clear.clicked.connect(self.clear_display)

    def append_number(self, number):
        expression = self.answer_box.text()
        new_text = expression + number
        self.answer_box.setText(new_text)

    def append_operator(self, operator):
        current_text = self.answer_box.text()
        if current_text[-1] in ['+', '-', '*', '/']:
            self.answer_box.setText(current_text[:-1] + operator)
        else:
            self.answer_box.setText(current_text + operator)

    def calculate_result(self):
        try:
            expression = self.answer_box.text()
            if '/0' in expression:
                self.answer_box.setText("undefined")
            else:
                result = eval(expression)
                self.answer_box.setText(str(result))
        except Exception:
            self.answer_box.setText("undefined")

    def clear_display(self):
        self.answer_box.clear()

    def change_sign(self):
        current_text = self.answer_box.text()
        if current_text[0] == '-':
            self.answer_box.setText(current_text[1:])
        else:
            self.answer_box.setText('-' + current_text)

    def delete_number(self):
        current_text = self.answer_box.text()
        new_text = current_text[:-1]
        self.answer_box.setText(new_text)

    def get_expression(self):
        return self.expression