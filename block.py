import hashlib  # Required for hashing block data
import time     # Used to timestamp each block


class Block:
    """
    Represents a single block in the blockchain.
    """

    def __init__(self, index, previous_hash, transactions, difficulty):
        """
        Initialize a new block with required properties.
        
        Parameters:
        - index (int): Position of block in the chain.
        - previous_hash (str): Hash of the previous block.
        - transactions (list): List of transactions to store.
        - difficulty (int): Mining difficulty (number of leading zeros required in hash).
        """
        self.index = index
        self.timestamp = time.time()  # Capture the time the block is created
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.difficulty = difficulty
        self.nonce = 0  # Nonce will be incremented during mining
        self.hash = self.calculate_hash()  # Initial hash (not yet mined)

    def calculate_hash(self):
        """
        Generates a SHA-256 hash based on the block's contents.
        Returns:
            str: The hash string.
        """
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()

    def mine_block(self):
        """
        Performs Proof-of-Work:
        Increment nonce until the block's hash starts with a specific number of zeros.
        """
        target = '0' * self.difficulty  # Target hash prefix (e.g., '0000')
        
        # Keep trying new nonce values until the hash meets the difficulty
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        print(f"Block #{self.index} mined with nonce {self.nonce} and hash: {self.hash[:10]}...")

    def __repr__(self):
        """
        String representation of the block (for printing).
        """
        return (f"Block #{self.index} | Timestamp: {self.timestamp} | "
                f"Hash: {self.hash[:10]}... | Previous Hash: {self.previous_hash[:10]}...")
