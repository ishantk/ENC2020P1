"""

    String
    Set
    Dictionary

"""

# johnsShop = 'Johns Coffee Shop'
# johnsShop = 'John's Coffee Shop' # err
# johnsShop = 'John\'s Coffee Shop'  # Escape Sequence [Google Them for More examples]
# johnsShop = "John's Coffee Shop"

# RAW String [which will ignore escape sequences in a string]
johnsShop = r'John\'s Coffee Shop'
print(johnsShop, type(johnsShop))

# quote = "Work Hard, Get Luckier\n-Anonymous"
quote = r"Work Hard, Get Luckier\n-Anonymous"
print(quote)


message = "This is an Awesome Day" \
          "We will Code Together" \
          "Thank You :)"

print(message)


quotes = """Work Hard, Get Luckier
Search the Candle, rather than cursing the darkness
"""

print(quotes, type(quotes))

# HW: Likewise we have put r in front of string, what else we can put :)


