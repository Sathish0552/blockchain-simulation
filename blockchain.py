from block import Block  # Import the Block class from block.py


class Blockchain:
    """
    Manages the chain of blocks and operations like mining and validation.
    """

    def __init__(self, difficulty=4):
        """
        Initializes the blockchain with:
        - A specified mining difficulty.
        - A genesis block.
        """
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]  # Start the chain with the genesis block

    def create_genesis_block(self):
        """
        Creates the first block (genesis block) in the chain.
        Returns:
            Block: The genesis block.
        """
        return Block(0, "0", ["Genesis Block"], self.difficulty)

    def add_block(self, transactions):
        """
        Adds a new block to the blockchain.
        
        Parameters:
        - transactions (list): A list of dummy transactions to store in the block.
        """
        previous_hash = self.chain[-1].hash  # Get hash of the last block
        new_block = Block(len(self.chain), previous_hash, transactions, self.difficulty)
        
        new_block.mine_block()  # Perform Proof-of-Work before adding to chain
        self.chain.append(new_block)  # Append the mined block to the chain

    def validate_chain(self):
        """
        Validates the entire blockchain by:
        - Checking hash integrity of each block.
        - Ensuring proper link to previous block.
        
        Returns:
            bool: True if valid, False if tampered.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Recalculate hash to detect tampering
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if current block links to previous one correctly
            if current_block.previous_hash != previous_block.hash:
                return False

        return True  # All blocks verified

    def print_chain(self):
        """
        Prints all blocks in the blockchain.
        """
        for block in self.chain:
            print(block)
