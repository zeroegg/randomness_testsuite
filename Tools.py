class Tools:

    @staticmethod
    def string_to_binary(input:str):
        binary = []
        for char in input:
            binary.append(bin(ord(char))[2:])

        return ''.join(binary)

    @staticmethod
    def url_to_binary(input:str):
        binary = []
        url = input.split('/')[-1].split('.')[0]

        return url
