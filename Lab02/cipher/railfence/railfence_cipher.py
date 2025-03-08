class RailFenceCipher:
    def __init__(self):
        pass
    def encrypt_text(self, plain_text,num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        for char in plain_text:
            rails[rail_index].append(char)
            if(rail_index==0):
                direction = 1
            elif(rail_index==num_rails-1):
                direction = -1
            rail_index += direction
        encrypted_text = "".join(["".join(rail) for rail in rails])
        return encrypted_text
    def decrypt_text(self, cipher_text,num_rails):
        rail_length = [0] * num_rails
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            rail_length[rail_index] += 1
            if(rail_index==0):
                direction = 1
            elif(rail_index==num_rails-1):
                direction = -1
            rail_index += direction
        rails =[]
        start = 0
        for length in rail_length:
            rails.append(cipher_text[start:start+length])
            start += length
            plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index][0]
            rails[rail_index] = rails[rail_index][1:]
            if(rail_index==0):
                direction = 1
            elif(rail_index==num_rails-1):
                direction = -1
            rail_index += direction
        return plain_text
