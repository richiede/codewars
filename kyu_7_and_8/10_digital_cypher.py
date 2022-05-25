# Digital Cypher assigns to each letter of the alphabet unique number.
# Instead of letters in encrypted word we write the corresponding number, eg. The word scout:
# s  c  o  u  t
# 19  3 15 21 20
# Then we add to each obtained digit consecutive digits from the key. For example. In case of key equal to 1939 :
#   s  c  o  u  t
#  19  3 15 21 20
# + 1  9  3  9  1
# ---------------
#  20 12 18 30 21
#  
#   m  a  s  t  e  r  p  i  e  c  e
#  13  1 19 20  5 18 16  9  5  3  5
# + 1  9  3  9  1  9  3  9  1  9  3
#  --------------------------------
#  14 10 22 29  6 27 19 18  6  12 8



def encode(message, key):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
     'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u',
     'v', 'w', 'x', 'y', 'z']
    message_list = [x for x in message]
    key_list = [x for x in str(key)]
    ciphered_code = []
    key_count = 0
    for i in message_list:
        if key_count >= len(key_list):
            key_count = 0
        value = alpha.index(i) + 1 + int(key_list[key_count])
        ciphered_code.append(value)
        key_count += 1
    return ciphered_code
  
  # Examples
# encode("scout", 1939), [20, 12, 18, 30, 21])
# encode("masterpiece", 1939), [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])
