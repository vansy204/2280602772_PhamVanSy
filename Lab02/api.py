from cipher.ceasar import CaesarCipher
from cipher.vingenere import VingenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
from flask import Flask, request, jsonify
app = Flask(__name__)


#ceasar
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


#vingenere
vigenere_cipher = VingenereCipher()
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})



#railfence
railfenceCipher = RailFenceCipher()
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    num_rails = int(data['num_rails'])
    encrypted_text = railfenceCipher.encrypt_text(plain_text, num_rails)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    num_rails = int(data['num_rails'])
    decrypted_text = railfenceCipher.decrypt_text(cipher_text, num_rails)
    return jsonify({'decrypted_text': decrypted_text})


#playfair
playfair_cipher = PlayFairCipher()
@app.route('/api/playfair/create_matrix', methods=['POST'])
def playfair_create_matrix():
    data = request.get_json()
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.encrypt_text(plain_text, key)
    
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/playfair/decrypt', methods=['POST']) 
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#transpositon
transpositionEncrypt = TranspositionCipher() 
@app.route("/api/transposition/encrypt",methods =['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int (data.get('key'))
    encrypted_text = transpositionEncrypt.encrypt(plain_text,key)
    return jsonify({'encrypted_text' : encrypted_text}) 


@app.route("/api/transposition/decrypt",methods =['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int (data.get('key'))
    decrypted_text = transpositionEncrypt.decrypt(cipher_text,key)
    return jsonify({'encrypted_text' : decrypted_text}) 
if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5000, debug=True)
    