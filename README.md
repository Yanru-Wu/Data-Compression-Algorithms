# Information Theory Coursework: Data Compression Algorithms

This repository contains Python implementations of three fundamental lossless data compression algorithms: Huffman Coding, Q-ary Huffman Coding, and Shannon-Fano Coding. 
This project serves as coursework for the Information Theory class.

## Implemented Algorithms

This project includes implementations for:

* **Huffman Coding (Binary)**: A widely used algorithm for optimal prefix coding based on character frequencies.
* **Q-ary Huffman Coding**: A generalization of Huffman coding that allows for codes with a base (alphabet size) of Q symbols.
* **Shannon-Fano Coding**: An early technique for constructing prefix codes based on symbol probabilities.

## Common Files and Workflow

* `input.txt`: This file serves as the input for all encoder scripts. Place the text you wish to compress/decompress here.

The general workflow for each algorithm is straightforward:

1.  **Prepare Input**: Place your desired text into `input.txt`.
2.  **Encode**: Run the respective encoder script (e.g., `huffman_encoder.py`, `q-ary_huffman_encoder.py`, `shannon_encoder.py`). This will generate an encoded file (e.g., `huffman_encode.txt`) and a codebook file (e.g., `huffman_codebook.txt`).
3.  **Decode**: Run the respective decoder script (e.g., `huffman_decoder.py`, `q-ary_huffman_decoder.py`, `shannon_decoder.py`). This will read the generated encoded file and codebook, then create a decoded file (e.g., `huffman_decode.txt`). Each decoder also performs an accuracy check against the original `input.txt`.


