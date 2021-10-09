# Adding Information
# ab -> append byte
with open('car.jpg', 'ab') as img:
    img.write(b'Hey there!')

# Extracting Information
# ab -> read byte
with open('car.jpg', 'rb') as img:
    content = img.read()
    index = content.index(bytes.fromhex('FFD9')) # Image files end at FFD9

    # index -> starting index of 'FFD9' + 2 bytes (size of FFD9)
    img.seek(index + 2)
    print(img.read())
