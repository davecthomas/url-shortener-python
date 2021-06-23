allowedchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
base_len = len(allowedchars)

def shorten(encode_value):
  e = encode_value
  short_url = []
  if e == 0:
    short_url = allowedchars[0]
  while(e > 0):
    index = (int)(e % base_len)
    short_url.append(allowedchars[index])
    # print("%d %s" % (index, allowedchars[index]))
    e = (int) (e / base_len)
  # Must reverse the string with [::-1]
  return ''.join(short_url[::-1])

