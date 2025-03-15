from flask import Flask, render_template,request,json
from cipher.ceasar import CaesarCipher

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

#ceasar
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')
@app.route("/encrypt",methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar_cipher = CaesarCipher()
    encrypt_text = caesar_cipher.encrypt_text(text,key)
    return f"text: {text} <br/> key:{key} <br/> encrypt_text: {encrypt_text}"


@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():   
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar_cipher = CaesarCipher()
    decrypt_text = caesar_cipher.decrypt_text(text,key)
    return f"text: {text} <br/> key:{key} <br/> decrypt_text: {decrypt_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050,debug=True)