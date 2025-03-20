from flask import Flask, request, jsonify
from cipher.ceasar import CaesarCipher
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

ceasar = CaesarCipher()
rsa = RSACipher()
ecc = ECCCipher()

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

@app.route("/api/rsa/encrypt", methods=['POST'])
def rsa_encrypt():
    data = request.get_json()
    encrypted = rsa.encrypt(data["plain_text"])
    return jsonify({"encrypted_text": encrypted})

@app.route("/api/rsa/decrypt", methods=['POST'])
def rsa_decrypt():
    data = request.get_json()
    decrypted = rsa.decrypt(data["cipher_text"])
    return jsonify({"decrypted_text": decrypted})

@app.route("/api/ecc/encrypt", methods=['POST'])
def ecc_encrypt():
    data = request.get_json()
    encrypted = ecc.encrypt(data["plain_text"])
    return jsonify({"encrypted_text": encrypted})

@app.route("/api/ecc/decrypt", methods=['POST'])
def ecc_decrypt():
    data = request.get_json()
    decrypted = ecc.decrypt(data["cipher_text"])
    return jsonify({"decrypted_text": decrypted})

if __name__ == '__main__':
    app.run(debug=True)
