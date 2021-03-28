import base64

with open('c:\\temp\\gt1.jpg', 'rb') as f:
    number=f.read()
    print (number)
    f.close()

    a = base64.b64encode(number, altchars=None)

    a=str(a, "utf-8")
    print("")
    print("")
    print("")
    print(a)

    a=bytes(a, 'utf-8')

    b = base64.b64decode(a, altchars=None)


    with open('c:\\temp\\out.jpg', 'wb') as f:
        f.write(b)
        f.close()
