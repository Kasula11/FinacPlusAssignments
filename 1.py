def Cipher(s: str, rotation_number: int):
    encrypted_str = ''
    for char in s:
        if char.isalpha():
            if char.isupper():
                encrypted_str += (chr((ord(char) - 65 + rotation_number) % 26 + 65))
            else:
                encrypted_str += (chr((ord(char) - 97 + rotation_number) % 26 + 97))
        else:
            encrypted_str.append(char)
    return encrypted_str


def find_most_optimized_set(s: set, number: int):
    sorted_s = sorted(s)
    ans = []
    pointer = len(sorted_s) - 1
    while pointer >= 0 and number > 0:
        if number - sorted_s[pointer] >= 0:
            number -= sorted_s[pointer]
            ans.append(sorted_s[pointer])
        else:
            pointer -= 1
    ans.sort()
    return ans

'''
The metadata information that i will store for an item in database lets say if the item is one product than the information i will store is
product id, product name, product description, product price, product category, product dimensions, product weight,product sold by
I will use this information in various useful business cases for example showing the product to the customer/users, analyzing
what kind of products the customer is more interested and showing recommendations around that, showing the particular product which the customer has brought and get to know 
the experience with the product by getting to know the ratings of it etc.
'''

result = find_most_optimized_set({1,2,5,10,20,50}, 28)
print(result)

