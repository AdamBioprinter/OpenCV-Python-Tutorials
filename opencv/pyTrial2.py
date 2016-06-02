import numpy as np
import matplotlib.pyplot as plt

def anti_vowel(text):
  vowels = "aeiouAEIOU"
  for x in vowels:
    text = text.replace(x, "")
  return text

x = anti_vowel("Yab Gab to Trab Yab Yab Aeiouz")

print(x)
