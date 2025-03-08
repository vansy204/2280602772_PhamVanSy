from cipher.ceasar import CaesarCipher
from flask import Flask, request, jsonify
app = Flask(__name__)

ceasar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = ceasar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = ceasar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5000, debug=True)
    