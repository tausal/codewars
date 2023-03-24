# If one were to ask the total byte size of "hello", what would the answer be?
# It's not 5. It's 54; because of ASCII.
# This might be useful for sending something over a network, where you need to represent the memory size the item takes up.

# You need to return the number of bytes (memory size) a given object takes up.
# Different varaible types will be given, but they will all be valid. Also,
# random generation for strings takes out of Unicode, not the regular 255 ASCII letters.