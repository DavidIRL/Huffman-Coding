import sys
import huffman_coding as hc

def as_expected():
    quote = """Riders of Theoden! Fell deeds awake, fire and slaughter!
    Spear shall be shaken, shield be splindered. A sword-day, a red day. 
    Ere the sun rises! Ride now, ride now! Ride to Gondor!"""

    encoded_quote, quote_key = hc.huffman_encoding(quote)
        
    print(f"The size of the data is: {sys.getsizeof(quote)}")
    print(f"The content of the data is: {quote[:18]}...{quote[-10:]}")

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_quote, base=2))}")
    print(f"The content of the encoded data is: {encoded_quote[:17]}...\n")

    decoded_data = hc.huffman_decoding(encoded_quote, quote_key)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print(f"The content of the decoded data is: {decoded_data[:18]}...{decoded_data[-10:]}")


def empty():
    empty_quote = ""
    print(hc.huffman_encoding(empty_quote))


def invalid_type():
    test = 1234567890
    print(hc.huffman_encoding(test))


def frankenstein():
    with open("frankenstein.txt","r") as file:
        frank = file.read()

    encoded_frank, frank_key = hc.huffman_encoding(frank)
        
    print(f"The size of the data is: {sys.getsizeof(frank)}")
    print(f"The content of the data is: {frank[:32]}...{frank[-18:]}")

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_frank, base=2))}")
    print(f"The content of the encoded data is: {encoded_frank[:17]}...\n")

    decoded_data = hc.huffman_decoding(encoded_frank, frank_key)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print(f"The content of the decoded data is: {decoded_data[:32]}...{decoded_data[-18:]}")



if __name__ == '__main__':
    as_expected()
    print("\nTesting Huffman with an empty string...")
    empty()
    print("\nTesting Huffman with an incorrect type input...")
    invalid_type()
    print("\n")
    frankenstein()
