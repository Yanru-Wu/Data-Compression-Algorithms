import time
import ast

# === Step 1: Read encoded text ===
with open('shannon_encode.txt', 'r', encoding='utf-8') as f:
    encoded_text = f.read()

# === Step 2: Read codebook ===
codebook = {}
with open('shannon_codebook.txt', 'r', encoding='utf-8') as f:
    for line in f:
        char_repr, code = line.strip().split(': ')
        char = ast.literal_eval(char_repr)  # safely evaluate e.g., "'a'" -> 'a'
        codebook[char] = code

# === Step 3: Decode ===
def decode(encoded_str, codebook):
    reverse_map = {v: k for k, v in codebook.items()}
    temp, result = '', []
    for bit in encoded_str:
        temp += bit
        if temp in reverse_map:
            result.append(reverse_map[temp])
            temp = ''
    return ''.join(result)

start_time = time.time()
decoded_text = decode(encoded_text, codebook)
end_time = time.time()

# === Step 4: Write decoded text ===
with open('shannon_decode.txt', 'w', encoding='utf-8') as f:
    f.write(decoded_text)

# === Step 5: Accuracy check ===
with open('input.txt', 'r', encoding='utf-8') as f:
    original_text = f.read()

is_correct = decoded_text == original_text
correct_chars = sum(1 for a, b in zip(decoded_text, original_text) if a == b)
accuracy = correct_chars / len(original_text) * 100

print("Was the original text successfully restored:", is_correct)
print(f"Decoding Accuracy = {accuracy:.2f}%")
print(f"Decoding Time = {end_time - start_time:.4f} seconds")
