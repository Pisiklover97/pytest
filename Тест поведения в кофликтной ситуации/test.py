from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QPushButton
from inst import txt_hello, questions
from results import calculate_results

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        # Переменные для текущего вопроса и выбора пользователя
        self.current_question = 0
        self.user_answers = []

        # Контейнер для размещения виджетов
        self.layout = QVBoxLayout()

        # Отображение первого вопроса и вариантов ответа
        self.question_label = QLabel(questions[self.current_question]["question"])
        self.layout.addWidget(self.question_label)

        # Радиокнопки для вариантов
        self.option1 = QRadioButton(questions[self.current_question]["option1"])
        self.option2 = QRadioButton(questions[self.current_question]["option2"])
        self.layout.addWidget(self.option1)
        self.layout.addWidget(self.option2)

        # Кнопка для перехода к следующему вопросу
        self.next_button = QPushButton("Следующий")
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)

        # Устанавливаем layout для главного окна
        self.setLayout(self.layout)
        self.setWindowTitle("Тест Томаса-Килмана")
        self.show()

    def next_question(self):
        # Сохраняем ответ пользователя
        answer = 'А' if self.option1.isChecked() else 'Б' if self.option2.isChecked() else None
        if answer:
            self.user_answers.append((self.current_question + 1, answer))
            self.current_question += 1

            # Проверка на конец теста
            if self.current_question < len(questions):
                # Обновление вопроса и вариантов
                self.question_label.setText(questions[self.current_question]["question"])
                self.option1.setText(questions[self.current_question]["option1"])
                self.option2.setText(questions[self.current_question]["option2"])
                self.option1.setChecked(False)
                self.option2.setChecked(False)
            else:
                # Завершение теста и вывод результатов
                result_text = calculate_results(self.user_answers)
                self.question_label.setText(result_text)
                self.option1.hide()
                self.option2.hide()
                self.next_button.hide()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    testWin = TestWin()
    sys.exit(app.exec_())