# Huffman Coding

## Design Choices

I implemented a min-head as a priority queue holding a tuple of frequency (priority), id (tie-breaker), and HuffmanNode. Using this heap I was able push and pop elements onto and off of the heap in the order needed to create the Huffman Tree. After the tree was created, I would then be able to traverse the tree encode each node with its Huffman Code. I implemented the internal Huffman Nodes as the same data structure distinguished by the fact their char was set to None. After that, getting the Huffman Codes was easy as traversing the tree to each leaf and storing the codes in a dictionary. Decoding the data involved moving along the Huffman Tree according to each bit until reaching a leaf and then starting over until all bits were consumed.

## Time Complexity

Push and pop on the min-heap data structure will happen in O(log(n)) in the worst case of having to move an element either all up or all the way down the heap.

The time complexity to build the Huffman Tree will be when it needs to push n elements onto the heap which will happen in O(n\*log(n)) time. The get_huffman_codes function will traverse the entire tree touching each node once which happens in O(n) time. In the huffman_encoding function building the huffman tree dominates all other time complexity operations so its time complexity is O(n\*log(n)).

The time complexity to decode the data will need to go through each bit which will take O(n) time and each time traverse down the entire tree to a leaf each time which will take O(log(n)) time. This means the entire decode process will happen in O(n\*log(n)) time.

## Space Complexity

The min-heap data structure will store a separate node for each character in the worst case when all characters are unique meaning its space complexity is O(n) (with a limit of all possible characters at which point its space complexity is a constant O(1)).

Building the Huffman Tree will create a dictionary and a min-heap which will take a space complexity of O(n). Getting the Huffman codes creates an additional data structure again with space complexity of O(n). Finally the encoding function then creates a string with with space complexity increasing with n, therefore the largest dominating factor for the space complexity of encoding is O(n).

Decoding only creates one additional string which increases in size in n therefore its space complexity too is O(n).
