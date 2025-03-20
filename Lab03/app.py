from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

rsa_cipher = RSACipher()
ecc_cipher = ECCCipher()

# RSA
@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    encrypted_text = rsa_cipher.encrypt_text(plain_text)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    decrypted_text = rsa_cipher.decrypt_text(cipher_text)
    return jsonify({'decrypted_text': decrypted_text})

# ECC
@app.route("/api/ecc/encrypt", methods=["POST"])
def ecc_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    encrypted_text = ecc_cipher.encrypt_text(plain_text)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/ecc/decrypt", methods=["POST"])
def ecc_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    decrypted_text = ecc_cipher.decrypt_text(cipher_text)
    return jsonify({'decrypted_text': decrypted_text})
