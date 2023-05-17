
def encode(strings: list) -> str:
    result = ""
    for string in strings:
        result += f'{len(string)}#{string}'
    return result

def decode(string: str) -> list:
    result, i = [], 0
    
    while i < len(string):
        j = i
        while string[j] != '#':
            j += 1
        result.append(string[j + 1: j + 1 + int(string[i:j])])
        i = j + 1 + int(string[i:j])
    return result

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
encoded_names = encode(names)
decoded_names = decode(encoded_names)

print(encoded_names)
print(decoded_names)
