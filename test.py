from urllib.parse import quote

a = "HAkTawsKfcyq5r)wo4NrCQ"
b = quote(a, 'utf-8')

print(b)