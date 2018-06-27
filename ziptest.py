import zlib
s = 'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s.encode())
print(len(t))
print(zlib.decompress(t).decode())
print(zlib.crc32(s.encode()))



