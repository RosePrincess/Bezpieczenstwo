#-*- coding: utf-8 -*-

import collections

class Decryptor:
    def __init__(self):
        self.cryptographs = []
        self.letters_frequencies = dict()
        self.key = []

        self.get_frequencies()

    def get_frequencies(self):
        # with open('frequency.txt') as file:
        #     for line in file.readlines():
        #         line = line.rstrip("\n")
        #         l = line.split(" ;")
        #         print(line[0])
        #         self.letters_frequencies[line[0]] = l[-1]

        self.letters_frequencies = {
            'a': 83.1, 'i': 88.3, 'o': 78, 'e': 86.8, 'z': 56, 'n': 56.9, 'r': 47, 'w': 47, 's': 43, 't': 40, 'c': 38.9, 'y': 38,
            'k': 30.1, 'd': 33.5, 'p': 31, 'm': 28.1, 'u': 25, 'j': 22.8, 'l': 22.4, 'b': 19.3, 'g': 14.6, 'h': 12.5, 'f': 2.6, 'q': 1,
            'v': 1, 'x': 1, ' ': 100, ',': 50, '.': 10, '-': 10, '"': 5, '!': 7, '?': 5, ':': 10, ';': 10, '(': 0.1, ')': 0.1
             , 'ą': 7.9, 'ź': 0.78, 'ś': 8.14, 'ł': 23.8, 'ć': 6, 'ń': 1.6, 'ę': 11.3,'ó': 11.41 , 'ż': 9.3
        }
         # Big letters - 1% frequency
        for i in range(65, 91):
            self.letters_frequencies[chr(i)] = 0.1 * self.letters_frequencies[chr(i+32)]

        # Numbers - 1% frequency
        for i in range(48, 58):
            self.letters_frequencies[chr(i)] = 10

    def find_key(self):
        longest = self.find_the_longest_size_of_cryptograph()

        for column in range(0,longest):
            # dictonary with the most likely keys
            possible_keys = {}

            # array with length greater than 'column'
            right_cryptographs = self.find_cryptographs_longer_than(column)

            # find the most possible keys
            # go throught all characters signed in 'letters_frequencies'
            for letter in self.letters_frequencies.keys():
                for crypt in right_cryptographs:
                    # xor letter with character from critptogram at 'column' position 
                    xor_result = crypt[column]^ord(letter)

                    if xor_result in possible_keys.keys():
                        possible_keys[xor_result] += self.letters_frequencies[letter]
                    else:
                        possible_keys[xor_result] = self.letters_frequencies[letter]
                    
            # sort 'possible_keys' from biggest frequncy to smallest
            possible_keys = dict(sorted(possible_keys.items(), key=lambda x: x[1], reverse=True))
            self.key.append(self.find_best_key(possible_keys, right_cryptographs, column))

    def find_the_longest_size_of_cryptograph(self):
        #length of the longest cryptohraph
        longest = 0
        #find the longest cryptograph
        for cript in self.cryptographs:
            length = len(cript)
            if(length > longest):
                longest = length
        return longest

    def find_cryptographs_longer_than(self, number):
        cryptographs = []
        for crypt in self.cryptographs:
            length = len(crypt)
            if(length > number):
                cryptographs.append(crypt)
        return cryptographs

    def find_best_key(self, possible_keys, cryptographs, number):
        best_key = ord('A')
        best_counter = 0
        for key in possible_keys.keys():
            for crypt in cryptographs:
                counter = 0

                # Check if xor result is in set of proper characters
                if chr((crypt[number]^key)) in self.letters_frequencies.keys():
                    counter+=1
                else:
                    break
                # First letter of kryptographs is probably an upper letter
                if(number == 0):
                    if (crypt[number]^key) in range(66,90):
                        counter +=1000
            if counter>best_counter:
                best_counter=counter
                best_key = key
        return best_key

    def decode(self):
        self.find_key()
        title = "result" + str(self.cryptographs_number) + ".txt"
        with open(title, 'w') as file:
            for crypt in self.cryptographs:
                for i in range(0, len(crypt)):
                    file.write(chr(crypt[i] ^ self.key[i]))
                file.write('\n')
        print(self.cryptographs_number)
         
    def get_cryptographs_from_file(self, filename, number):
        count = 1
        self.cryptographs.clear()
        with open(filename) as file:
            for line in file.readlines():
                if count <= number:
                    seperate = line.split(" ")
                    characters = []
                    for s in seperate:
                        characters.append(int(s,2))
                    self.cryptographs.append(characters)
                    count += 1
                else:
                    break
        self.cryptographs_number = len(self.cryptographs)
        # print(self.cryptographs)
    
