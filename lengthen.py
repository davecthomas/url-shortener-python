import math

allowedchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
base_len = len(allowedchars)

def lengthen(decode_str):
  decode_len = len(decode_str)

  decoded = 0
  counter = 1

  for i, decode_char in enumerate(decode_str):
    index = allowedchars.find(decode_str[i])
    decoded = decoded + index * math.pow(base_len, decode_len - counter)
    counter = counter + 1
  return decoded
