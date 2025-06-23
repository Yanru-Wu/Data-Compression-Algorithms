from collections import Counter
import math

def shannon_fano(symbols):
    if len(symbols) == 1:
        return {symbols[0][0]: '0'}
    elif len(symbols) == 2:
        return {symbols[0][0]: '0', symbols[1][0]: '1'}
    total = sum(item[1] for item in symbols)
    acc = 0
    for i in range(len(symbols)):
        acc += symbols[i][1]
        if acc >= total / 2:
            break
    left = shannon_fano(symbols[:i+1])
    right = shannon_fano(symbols[i+1:])
    for k in left:
        left[k] = '0' + left[k]
    for k in right:
        right[k] = '1' + right[k]
    left.update(right)
    return left

# === Step 1: Read input ===
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# === Step 2: Frequency counting and encoding ===
freq = Counter(text)
sorted_symbols = sorted(freq.items(), key=lambda x: x[1], reverse=True)
codebook = shannon_fano(sorted_symbols)
encoded_text = ''.join(codebook[c] for c in text)

# === Step 3: Save results ===
with open('shannon_encode.txt', 'w', encoding='utf-8') as f:
    f.write(encoded_text)

with open('shannon_codebook.txt', 'w', encoding='utf-8') as f:
    for char, code in codebook.items():
        f.write(f"{repr(char)}: {code}\n")

# === Step 4: Print analysis ===
entropy = -sum((freq[c] / len(text)) * math.log2(freq[c] / len(text)) for c in freq)
avg_length = sum(freq[c] * len(codebook[c]) for c in freq) / len(text)
efficiency = entropy / avg_length

print(f"Entropy H(X) = {entropy:.4f} bits/symbol")
print(f"Average Code Length L̄ = {avg_length:.4f} bits/symbol")
print(f"Code Efficiency η = {efficiency*100:.2f}%")
