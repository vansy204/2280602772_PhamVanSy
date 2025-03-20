import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit,
    QComboBox, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
)

class EncryptorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mã hóa/Giải mã - PyQt5")
        self.resize(400, 500)

        self.layout = QVBoxLayout()

        self.algorithm_label = QLabel("Chọn thuật toán:")
        self.algorithm_combo = QComboBox()
        self.algorithm_combo.addItems(["Caesar", "RSA", "ECC"])
        self.layout.addWidget(self.algorithm_label)
        self.layout.addWidget(self.algorithm_combo)

        self.key_label = QLabel("Key:")
        self.key_input = QLineEdit()
        self.layout.addWidget(self.key_label)
        self.layout.addWidget(self.key_input)

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Nhập văn bản cần mã hóa/giải mã...")
        self.layout.addWidget(self.text_input)

        # Buttons
        button_layout = QHBoxLayout()
        self.encrypt_btn = QPushButton("Mã hóa")
        self.decrypt_btn = QPushButton("Giải mã")
        button_layout.addWidget(self.encrypt_btn)
        button_layout.addWidget(self.decrypt_btn)
        self.layout.addLayout(button_layout)

        self.result_label = QLabel("Kết quả:")
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.result_output)

        self.setLayout(self.layout)

        # Connect signals
        self.encrypt_btn.clicked.connect(lambda: self.handle_api("encrypt"))
        self.decrypt_btn.clicked.connect(lambda: self.handle_api("decrypt"))

    def handle_api(self, action):
        algorithm = self.algorithm_combo.currentText().lower()
        text = self.text_input.toPlainText()
        key = self.key_input.text()

        url = f"http://localhost:5000/api/{algorithm}/{action}"
        payload = {}

        # Tùy thuộc vào thuật toán
        if algorithm == "caesar":
            if not key.isdigit():
                QMessageBox.warning(self, "Lỗi", "Key của Caesar phải là số nguyên.")
                return
            payload = {
                "plain_text" if action == "encrypt" else "cipher_text": text,
                "key": key
            }
        elif algorithm == "rsa":
            payload = {
                "plain_text" if action == "encrypt" else "cipher_text": text
            }
        elif algorithm == "ecc":
            payload = {
                "plain_text" if action == "encrypt" else "cipher_text": text
            }

        try:
            res = requests.post(url, json=payload)
            res.raise_for_status()
            result = res.json()
            self.result_output.setPlainText(
                result.get('encrypted_text') or result.get('decrypted_text', 'Không có kết quả.')
            )
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Lỗi kết nối", f"Không thể kết nối đến API:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncryptorApp()
    window.show()
    sys.exit(app.exec_())
