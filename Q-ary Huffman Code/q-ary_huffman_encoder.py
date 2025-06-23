from collections import Counter
import heapq
import math
import sys

class QaryHuffmanNode:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.children = []  

    def __lt__(self, other):
        return self.freq < other.freq

def build_qary_huffman_tree(freq, Q):
    heap = [QaryHuffmanNode(char, freq[char]) for char in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        group = []
        for _ in range(min(Q, len(heap))):
            group.append(heapq.heappop(heap))
        merged_freq = sum(node.freq for node in group)
        parent = QaryHuffmanNode(None, merged_freq)
        parent.children = group
        heapq.heappush(heap, parent)

    return heap[0]

def generate_qary_codes(node, prefix="", codebook=None, Q=2):
    if codebook is None:
        codebook = {}
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        for i, child in enumerate(node.children):
            generate_qary_codes(child, prefix + str(i), codebook, Q)
    return codebook

# ===== User Config =====
Q = 5  # Base-Q Huffman encoding, change this to your desired base (e.g., 2 for binary, 3 for ternary, etc.)
# =======================

# === Step 1: Read input ===
with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# === Step 2: Build Q-ary Huffman Tree and Codebook ===
freq = Counter(text)
root = build_qary_huffman_tree(freq, Q)
codebook = generate_qary_codes(root, Q=Q)

# === Step 3: Encode text ===
encoded_text = ''.join(codebook[c] for c in text)

# === Step 4: Save encoded text and codebook ===
with open('q-ary_huffman_encode.txt', 'w', encoding='utf-8') as f:
    f.write(encoded_text)

with open('q-ary_huffman_codebook.txt', 'w', encoding='utf-8') as f:
    for char, code in codebook.items():
        f.write(f"{repr(char)}: {code}\n")

# === Step 5: Print stats ===
entropy = -sum((freq[c] / len(text)) * math.log2(freq[c] / len(text)) for c in freq)
avg_length = sum(freq[c] * len(codebook[c]) for c in freq) / len(text)
efficiency = entropy / (avg_length * math.log2(Q))  

print(f"Base-Q Huffman Encoding (Q = {Q})")
print(f"Entropy H(X) = {entropy:.4f} bits/symbol")
print(f"Average Code Length L̄ = {avg_length:.4f} symbols (base-{Q})")
print(f"Code Efficiency η = {efficiency * 100:.2f}%")
