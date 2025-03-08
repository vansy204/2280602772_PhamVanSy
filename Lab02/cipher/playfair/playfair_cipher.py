class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()  # Normalize key
        key_set = set()
        matrix = []
        
        # Add unique key letters first
        for letter in key:
            if letter not in key_set:
                key_set.add(letter)
                matrix.append(letter)

        # Add remaining letters of alphabet
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in key_set:
                matrix.append(letter)

        # Convert to 5x5 matrix
        playfair_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_position(self, letter, matrix):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == letter:
                    return i, j
        return None  # Should never happen

    def encrypt_text(self, plain_text, key):
        playfair_matrix = self.create_playfair_matrix(key)
        plain_text = plain_text.replace("J", "I").upper()
        plain_text = [char for char in plain_text if char.isalpha()]

        # Handle repeated letters in a pair (insert "X" if needed)
        i = 0
        while i < len(plain_text) - 1:
            if plain_text[i] == plain_text[i + 1]:
                plain_text.insert(i + 1, "X")
            i += 2

        # If odd length, append "X"
        if len(plain_text) % 2 == 1:
            plain_text.append("X")

        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            char1, char2 = plain_text[i], plain_text[i + 1]
            row1, col1 = self.find_letter_position(char1, playfair_matrix)
            row2, col2 = self.find_letter_position(char2, playfair_matrix)

            if row1 == row2:  # Same row
                encrypted_text += playfair_matrix[row1][(col1 + 1) % 5]
                encrypted_text += playfair_matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Same column
                encrypted_text += playfair_matrix[(row1 + 1) % 5][col1]
                encrypted_text += playfair_matrix[(row2 + 1) % 5][col2]
            else:  # Rectangle swap
                encrypted_text += playfair_matrix[row1][col2]
                encrypted_text += playfair_matrix[row2][col1]

        return encrypted_text

    def decrypt_text(self, cipher_text, key):
        playfair_matrix = self.create_playfair_matrix(key)
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            char1, char2 = cipher_text[i], cipher_text[i + 1]
            row1, col1 = self.find_letter_position(char1, playfair_matrix)
            row2, col2 = self.find_letter_position(char2, playfair_matrix)

            if row1 == row2:  # Same row
                decrypted_text += playfair_matrix[row1][(col1 - 1) % 5]
                decrypted_text += playfair_matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Same column
                decrypted_text += playfair_matrix[(row1 - 1) % 5][col1]
                decrypted_text += playfair_matrix[(row2 - 1) % 5][col2]
            else:  # Rectangle swap
                decrypted_text += playfair_matrix[row1][col2]
                decrypted_text += playfair_matrix[row2][col1]

        return decrypted_text
