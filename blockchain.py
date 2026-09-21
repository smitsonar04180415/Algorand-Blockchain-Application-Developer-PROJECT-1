"""A very basic blockchain for learning purposes."""

import hashlib
import json
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def mine(self, difficulty):
        """Proof of work: change nonce until the hash starts with `difficulty` zeros."""
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

    def calculate_hash(self):
        """SHA-256 over all the block's contents."""
        content = json.dumps(
            {
                "index": self.index,
                "timestamp": self.timestamp,
                "data": self.data,
                "previous_hash": self.previous_hash,
                "nonce": self.nonce,
            },
            sort_keys=True,
        )
        return hashlib.sha256(content.encode()).hexdigest()


class Blockchain:
    def __init__(self, difficulty=3):
        self.difficulty = difficulty
        genesis = Block(0, "Genesis Block", "0")
        genesis.mine(self.difficulty)
        self.chain = [genesis]

    def latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        block = Block(len(self.chain), data, self.latest_block().hash)
        block.mine(self.difficulty)
        self.chain.append(block)
        return block

    def is_valid(self):
        """Check every block's hash and its link to the previous block."""
        for i in range(1, len(self.chain)):
            current, previous = self.chain[i], self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if not current.hash.startswith("0" * self.difficulty):
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
