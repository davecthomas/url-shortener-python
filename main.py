from shorten import shorten
from lengthen import lengthen
from store import store
import sys
# TO DO ask for a URL and insert or update it in a DB (with an expiry date)
# then use the ID of the new row as the thing we shorten
# url = input("enter a URL: ")
# store(url)
ID = int(input("enter a number: "))
short_list = shorten(ID)
print( short_list ) 
print(lengthen(short_list))
