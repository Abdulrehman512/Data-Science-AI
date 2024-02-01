import pyshorteners 

url = input("Enter URL for Shortening \n")

print("Short URL is :",pyshorteners.Shortener().tinyurl.short(url) )