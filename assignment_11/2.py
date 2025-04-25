import pandas as pd

# Example series
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert strings and find their lengths
print("Uppercase:", s.str.upper())
print("Lowercase:", s.str.lower())
print("String Lengths:", s.str.len())
