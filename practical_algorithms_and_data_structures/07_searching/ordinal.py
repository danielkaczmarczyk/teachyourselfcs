"""
    Simple implementation of the modulo sum of ordinal values of string
    chars hashing function
"""

def hash(a_string, table_size):
    the_sum = sum(ord(char) for char in a_string)
    return the_sum % table_size

def hash_weighted(a_string, table_size):
    i = 0
    the_sum = 0
    
    while i < len(a_string):
        char = a_string[i]
        the_sum += ord(char) * i
        i += 1

    return the_sum


if __name__ == '__main__':

    h1 = hash('listen', 11)
    h2 = hash('silent', 11)

    if h1 == h2:
        print(h1, h2)
        print('both hashes have the same value - items are anagrams')

    h1 = hash_weighted('listen', 11)
    h2 = hash_weighted('silent', 11)

    print(h1, h2)
