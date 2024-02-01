import wikipedia

query = input("Enter the Name of Topic : \n")

result = wikipedia.summary(query)

print(result)