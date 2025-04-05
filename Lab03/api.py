from flask import Flask, request, jsonify
from cipher.ceasar import CaesarCipher
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

ceasar = CaesarCipher()
rsa_cipher = RSACipher()
ecc_cipher = ECCCipher()

@app.route("/api/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    return jsonify({
        "encrypted_text": ceasar.encrypt_text(data["plain_text"], int(data["key"]))
    })

@app.route("/api/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    return jsonify({
        "decrypted_text": ceasar.decrypt_text(data["cipher_text"], int(data["key"]))
    })

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    encrypted_text = rsa_cipher.encrypt_text(plain_text)  # ✅ Dùng đúng tên biến và hàm
    return jsonify({'encrypted_text': encrypted_text})


@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    decrypted_text = rsa_cipher.decrypt_text(cipher_text)  # Dùng đúng hàm trong RSACipher
    return jsonify({'decrypted_text': decrypted_text})

@app.route("/api/ecc/encrypt", methods=["POST"])
def ecc_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    encrypted_text = ecc_cipher.encrypt_text(plain_text)  # Gọi đúng hàm trong ECCCipher
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/ecc/decrypt", methods=["POST"])
def ecc_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    decrypted_text = ecc_cipher.decrypt_text(cipher_text)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(debug=True)
