import base64
enc = base64.b64encode("Some")

print enc

dec = base64.b64decode(enc)
print dec