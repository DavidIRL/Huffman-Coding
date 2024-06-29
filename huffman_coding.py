import sys
import huffman_helpers as huff

  
def huffman_encoding(message):
    """ 
    Syntax: 'coded_message_variable',  'key_variable' = func(message)
    \n
    Enter your message to be compressed as a variable or a string object
    \n
    Will return coded message and key
    """
    # would typically raise error, but using return for manual test.py
    if type(message) != str:
        return TypeError("input data must be of type string")
    if len(message) <= 0:
        return Exception("data to encode must not be empty")

    freq = huff.freq_dict(message)
    #print(freq)
    heap = huff.make_heap(freq)
    #print(heap)
    code = huff.make_code(heap)
    key = huff.make_key(code)
    coded_message = huff.encode(message, key)
    #print(coded_message)
    #print(key)
    return coded_message, key


#--------------------------------------------------------------------------#
#                               Decode Below                               #
#--------------------------------------------------------------------------#


def huffman_decoding(encoded_message, key):
    """ 
    Syntax: 'decoded_data_variable' = func(coded_message, key)
    \n
    Takes previously encoded message and companion key to output
    \n
    Decompress and decoded message/info
    """
    keys = key.keys()
    values = key.values()
    cypher = dict(zip(values, keys))
    #print(cypher)
    current_code = ''
    decoded_message = ''

    for digit in encoded_message:
        current_code += digit
        # use code value as key in de_codes to get char
        if current_code in cypher:
            char = cypher[current_code]
            decoded_message += char
            current_code = ''

    return decoded_message


if __name__ == "__main__":    

    a_great_sentence = "The bird is the word"

    print (f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print (f"The content of the data is: {a_great_sentence}")

    encoded_data, key = huffman_encoding(a_great_sentence)

    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print (f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, key)

    print (f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print (f"The content of the encoded data is: {decoded_data}")
