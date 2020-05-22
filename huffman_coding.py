"""Encode and decode data using the Huffman Coding compression algorithm.

Usage: huffman_coding.py

Classes:
    MinHeap()
    HuffmanNode()
"""

import sys


class MinHeap:
    """Creates a min-heap where the minimum value is at the root of the tree.

    Attributes:
        heap: A list representing the items in the heap
    """

    def __init__(self):
        """Set-up for the min-heap."""
        self.heap = []

    def push(self, item):
        """Push an item onto the heap.

        Args:
            item: The item to push onto the heap
        """
        idx = len(self.heap)
        parent_idx = (idx - 1) // 2
        self.heap.append(item)

        while idx > 0 and self.heap[parent_idx] > self.heap[idx]:
            self.heap[parent_idx], self.heap[idx] = (
                self.heap[idx],
                self.heap[parent_idx],
            )
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def pop(self):
        """Pop the smallest item off the top of the heap.

        Returns:
            min_node: The smallest item (located at the root of the node)
        """
        if len(self.heap) == 0:
            return

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_node = self.heap.pop()
        idx = 0
        child_idx = 2 * idx + 1

        while (
            child_idx < len(self.heap)
            and self.heap[idx] > self.heap[child_idx]
        ):
            if (
                len(self.heap) > child_idx + 1
                and self.heap[child_idx] > self.heap[child_idx + 1]
            ):
                child_idx += 1

            self.heap[child_idx], self.heap[idx] = (
                self.heap[idx],
                self.heap[child_idx],
            )
            idx = child_idx
            child_idx = 2 * idx + 1

        return min_node


class HuffmanNode:
    """Creates a Node object for a Huffman Tree.

    Attributes:
        char: A str of a single character the node is representing if it is a
            leaf node
        freq: An int representing the frequency the char appears in the data or
            the sum of all freqs in the leaf nodes under this node
        code: A str representing the Huffman Code for the leaf node or the
            prefix of the Huffman Code for all leaf nodes under this node
        left: A HuffmanNode object under and to the left of this node
        right: A HuffmanNode object under and to the right of this node
    """

    def __init__(self, char=None, freq=1, left=None, right=None):
        """Set-up for the Huffman Node."""
        self.char = char
        self.freq = freq
        self.code = ""
        self.left = left
        self.right = right


def main():
    """Main function call.

    Tests the functionality of huffman_encoding and huffman_decoding
    """
    a_great_sentence = "The bird is the word"
    data_size = sys.getsizeof(a_great_sentence)
    print(f"The size of the data is: {data_size}")
    print(f"The content of the data is: {a_great_sentence}\n")

    encoded_data, root = huffman_encoding(a_great_sentence)
    encoded_data_size = sys.getsizeof(int(encoded_data, base=2))
    print(f"The size of the encoded data is: {encoded_data_size}")
    print(f"The content of the encoded data is: {encoded_data}\n")

    decoded_data = huffman_decoding(encoded_data, root)
    decoded_data_size = sys.getsizeof(decoded_data)
    print(f"The size of the decoded data is: {decoded_data_size}")
    print(f"The content of the encoded data is: {decoded_data}\n")

    assert data_size > encoded_data_size
    assert data_size == decoded_data_size
    assert encoded_data == (
        "10101110111111010110000010101100000"
        "11011010001110111111001111001001010"
    )
    assert a_great_sentence == decoded_data

    print("All test cases passed!")


def huffman_encoding(data):
    """Encodes data using Huffman Coding compression algorithm.

    Args:
        data: A str to be encoded

    Returns:
        encoded_data: A str representing the data encoded into binary using the
            Huffman Coding compression algorithm
        root: A HuffmanNode object representing the root node of a Huffman Tree
    """
    root = build_huffman_tree(data)
    huffman_codes = get_huffman_codes(root, {})

    encoded_data = ""
    for char in data:
        encoded_data += huffman_codes[char]

    return encoded_data, root


def build_huffman_tree(data):
    """Builds a Huffman Tree from the provided data.

    Args:
        data: A str to use to build the Huffman Tree

    Returns:
        root: A HuffmanNode object representing the root node of a Huffman Tree
    """
    data_freq = {}
    for char in data:
        if char in data_freq:
            data_freq[char].freq += 1
        else:
            data_freq[char] = HuffmanNode(char)

    min_heap = MinHeap()
    entry_id = 0
    for char in data_freq:
        node = data_freq[char]
        min_heap.push((node.freq, entry_id, node))
        entry_id += 1

    while len(min_heap.heap) > 1:
        freq1, _, node1 = min_heap.pop()
        freq2, _, node2 = min_heap.pop()
        node = HuffmanNode(freq=freq1 + freq2, left=node1, right=node2)
        min_heap.push((node.freq, entry_id, node))
        entry_id += 1

    root = node

    return root


def get_huffman_codes(node, huffman_codes):
    """Creates a dict of chars and their cooresponding Huffman Codes.

    Args:
        node: A HuffmanNode object to find all Huffman Codes for the leaves
            under it
        huffman_codes: A dict to store the generated Huffman Codes

    Returns:
        huffman_codes: A dict containing all of the generated Huffman Codes
            thus far
    """
    if node.char is not None:
        huffman_codes[node.char] = node.code

    if node.left is not None:
        node.left.code = node.code + "0"
        get_huffman_codes(node.left, huffman_codes)

    if node.right is not None:
        node.right.code = node.code + "1"
        get_huffman_codes(node.right, huffman_codes)

    return huffman_codes


def huffman_decoding(data, root):
    """Decodes data using Huffman Coding compression algorithm.

    Args:
        data: A str in binary to be encoded using the provided Huffman Tree
        root: A HuffmanNode object representing the root node of a Huffman Tree
            to be used to decode the provided data

    Returns:
        decoded_data: A str representing the data decoded using the Huffman
            Coding compression algorithm
    """
    decoded_data = ""
    node = root
    for bit in data:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded_data += node.char
            node = root

    return decoded_data


if __name__ == "__main__":
    main()
