


text = "rita learn java , josephine learn python"
words = text.split()
words1 = text.split()
result = ""
result1 = ""

for word in words:
    result +=f" {word.capitalize()}" 
for word in words1:
    result1 +=f" {word.upper()}"

print(result.strip())
print(result1.strip())
