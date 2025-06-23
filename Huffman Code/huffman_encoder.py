from collections import Counter
import heapq
import math

class HuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq):
    heap = [HuffmanNode(char, freq[char]) for char in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

# === Step 1: Read input ===
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# === Step 2: Build Huffman Tree and Codebook ===
freq = Counter(text)
root = build_huffman_tree(freq)
codebook = generate_codes(root)

# === Step 3: Encode text ===
encoded_text = ''.join(codebook[c] for c in text)

# === Step 4: Save encoded text and codebook ===
with open('huffman_encode.txt', 'w', encoding='utf-8') as f:
    f.write(encoded_text)

with open('huffman_codebook.txt', 'w', encoding='utf-8') as f:
    for char, code in codebook.items():
        f.write(f"{repr(char)}: {code}\n")

# === Step 5: Print stats ===
entropy = -sum((freq[c] / len(text)) * math.log2(freq[c] / len(text)) for c in freq)
avg_length = sum(freq[c] * len(codebook[c]) for c in freq) / len(text)
efficiency = entropy / avg_length

print(f"Entropy H(X) = {entropy:.4f} bits/symbol")
print(f"Average Code Length L̄ = {avg_length:.4f} bits/symbol")
print(f"Code Efficiency η = {efficiency * 100:.2f}%")
