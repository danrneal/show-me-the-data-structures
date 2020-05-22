"""Implement a blockchain as a linked list.

Usage: blockchain.py

Classes:
    Blockchain()
    Block()
"""

from datetime import datetime
import hashlib


class Blockchain:
    """Blockchain object that stores blocks as a linked list.

    Attributes:
        prev_block: A Block object representing the most recently added block
    """

    def __init__(self):
        """Set-up for the blockchain."""
        self.prev_block = None

    def add_block(self, data):
        """Add a block into the blockchain.

        Args:
            data: The data to store in the added block
        """
        self.prev_block = Block(data, self.prev_block)

    def print_blockchain(self):
        """Print a representation of the blockchain.

        The most recently added block will be printed first
        """
        print("-------BLOCKCHAIN--------")
        print("(Most recent block first)")
        block = self.prev_block
        while block is not None:
            print("=========================")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            block = block.prev_block


class Block:
    """Block object to store inside of a blockchain.

    Attributes:
        timestamp: A datetime representing the time the block was created
        data: The data the block is to store
        prev_hash: A str representing the previous block in the blockchain's
            hash
        hash: A str representing this block's hash
        prev_block: A Block object presenting the previous block in the
            blockchain
    """

    def __init__(self, data, prev_block):
        """Set-up for the block."""
        self.timestamp = datetime.utcnow()
        self.data = data
        self.prev_hash = None
        if prev_block is not None:
            self.prev_hash = prev_block.hash
        self.hash = self.calc_hash(self.timestamp, self.data, self.prev_hash)
        self.prev_block = prev_block

    def calc_hash(self, timestamp, data, prev_hash):
        """Calculate a SHA-256 hash for a block.

        Args:
            timestamp: A datetime representing the time the block was created
            data: The data the block is storing
            prev_hash: A str representing the previous block in the
                blockchain's hash

        Returns:
            hashed_str: A str representing the calculated hash
        """
        sha = hashlib.sha256()
        hash_str = f"{timestamp}{data}{prev_hash}".encode("utf-8")
        sha.update(hash_str)
        hashed_str = sha.hexdigest()

        return hashed_str


def main():
    """Main function call to test blockchain implementation."""
    blockchain = Blockchain()
    blockchain.add_block("hello")
    blockchain.add_block("world")
    blockchain.print_blockchain()


if __name__ == "__main__":
    main()
