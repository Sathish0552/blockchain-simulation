from blockchain import Blockchain  # Import the Blockchain class


def main():
    """
    Main execution logic:
    - Initializes blockchain.
    - Adds blocks with transactions.
    - Prints blockchain.
    - Validates before and after tampering.
    """
    # Create a blockchain instance with defined difficulty (Proof-of-Work)
    my_blockchain = Blockchain(difficulty=4)

    # Add blocks with dummy transaction data
    my_blockchain.add_block(["Transaction 1: Alice to Bob"])
    my_blockchain.add_block(["Transaction 2: Bob to Charlie"])
    my_blockchain.add_block(["Transaction 3: Charlie to Dave"])

    # Print all blocks in the chain
    print("Blockchain:")
    my_blockchain.print_chain()

    # Validate blockchain integrity (should be True)
    print("\nIs the blockchain valid?")
    print(my_blockchain.validate_chain())

    # Tamper with block data to simulate attack or error
    print("\nTampering with the blockchain...")
    my_blockchain.chain[1].transactions = ["Transaction 2: Alice to Eve"]

    # Validate again (should now be False)
    print("Is the blockchain valid after tampering?")
    print(my_blockchain.validate_chain())


if __name__ == "__main__":
    main()
