import math


class ShennonDecoder:
    def __init__(self):
        self.alphabet = self.get_alphabet()
        self.code = self.create_code()

    def get_alphabet():
        dictionary = dict()
        try:
            with open('text.txt', encoding='utf8') as f:
                lines = f.readlines()
                if not lines:
                    return
                line_1 = lines[0].split()
                line_2 = lines[1].split()
                if len(line_1) != len(line_2):
                    return
                for num_1, symbol in enumerate(line_1):
                    for num_2, probability in enumerate(line_2):
                        if num_1 == num_2:
                            dictionary[symbol] = probability
            dict_sort = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
        except:
            return
        return dict_sort

    def float2bin(num):
        exponent = 0
        shifted_num = num
        while shifted_num != int(shifted_num):
            shifted_num *= 2
            exponent += 1
        if exponent == 0:
            return '{0:0b}'.format(int(shifted_num))
        binary = '{0:0{1}b}'.format(int(shifted_num), exponent + 1)
        integer_part = binary[:-exponent]
        fractional_part = binary[-exponent:].rstrip('0')
        return '{0}.{1}'.format(integer_part, fractional_part)

    def get_binary_code(self):
        binary_dict = dict()
        list_of_sums = [sum(map(float, list(self.alphabet.values())[:i])) for i in range(len(self.alphabet))]
        for i in range(len(self.alphabet)):
            number = self.float2bin(list_of_sums[i]).replace("0.", "")
            if number == "0":
                number = "000000000000000"
            binary_dict[list(self.alphabet.keys())[i]] = number
        return binary_dict

    def get_lenghts(self):
        lst_length_i = []
        for i in self.alphabet:
            length_i = math.ceil(math.log2(1 / float(self.alphabet[i])))
            lst_length_i.append(length_i)
        return lst_length_i

    def create_code(self):
        binary_code = self.get_binary_code()
        lenghts = self.get_lenghts()
        code = dict()
        for index, key in enumerate(self.alphabet.keys()):
            code.update({key: binary_code[key][:lenghts[index]]})
        return {y: x for x, y in code.items()}

    def decode(self, encoded_text):
        decoded_text = ""
        encoded_text = [i for i in encoded_text.split(" ")]
        for i in encoded_text:
            if i in self.code:
                decoded_text += self.code[i] + " "
        return decoded_text


if __name__ == '__main__':
    sh = ShennonDecoder()
    n = input("Введите закодированную строку: ")
    print(sh.decode(n))