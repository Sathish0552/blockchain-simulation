# Blockchain Simulation with Proof-of-Work

This project simulates a basic blockchain that mimics the core features of a blockchain system:
- Block Structure
- SHA-256 Hashing
- Blockchain Validation
- Proof-of-Work (Mining)
- Tampering Detection

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Code Structure](#code-structure)

## Installation

To get started with this project, you'll need Python 3.x installed on your machine.

### 1. Clone the Repository:

->git clone https://github.com/Sathish0552/blockchain-simulation.git
->cd blockchain-simulation


### 2. Run the Simulation:
Once everything is set up, run the main.py script to see the blockchain in action:

->python main.py

## Usage
What This Program Does:
Simulate a Blockchain:

Creates blocks with dummy transactions.

Hashes each block using the SHA-256 algorithm.

Links each block to the previous one, forming a chain.

Proof-of-Work Mining:

Each block is mined using Proof-of-Work.

The program tries different nonces until it finds a valid hash that satisfies the difficulty (e.g., starts with "0000").

Blockchain Validation:

After mining, the program validates the integrity of the blockchain.

It checks that the hash of each block and the link to the previous block are correct.

Tampering Detection:

If the blockchain is tampered with, such as modifying a block's transaction data, it will fail validation, detecting the change.

#### Example Output:
Block #1 mined with nonce 54582 and hash: 00002c2bb0...
Block #2 mined with nonce 1534 and hash: 00008d23a5...
Block #3 mined with nonce 22987 and hash: 00001f3f32...
Blockchain:
Block #0 | Timestamp: 1743440951.5942929 | Hash: 0315362158... | Previous Hash: 0...
Block #1 | Timestamp: 1743440951.5942929 | Hash: 00002c2bb0... | Previous Hash: 0315362158...
Block #2 | Timestamp: 1743440951.8113766 | Hash: 00008d23a5... | Previous Hash: 00002c2bb0...
Block #3 | Timestamp: 1743440951.821152 | Hash: 00001f3f32... | Previous Hash: 00008d23a5...

Is the blockchain valid?
True

Tampering with the blockchain...
Is the blockchain valid after tampering?
False


## How It Works
1. Block Structure:
Each block in the blockchain consists of:

Block Number (Index): The position of the block in the chain.

Timestamp: When the block was created.

Transactions: A list of dummy transaction data.

Previous Block's Hash: A reference to the previous block to maintain chain integrity.

Current Block's Hash: A hash calculated using the block's data.

2. Proof-of-Work:
The block mining process is computationally intensive and requires solving a "puzzle":

The block's hash must start with a specific number of zeros, defined by the difficulty level.

The program tries different nonce values (random numbers) until it finds one that produces a valid hash.

3. Chain Validation:
To ensure the blockchain’s integrity, each block is verified:

The current block’s hash must match the recalculated hash.

The current block’s previous_hash must link to the hash of the previous block.

4. Tampering Detection:
If a block is tampered with (e.g., changing a transaction), the hash will no longer match, and the blockchain will be invalidated.

## Code Structure
block.py: Defines the Block class, which represents a block in the blockchain. It includes functions for:

Calculating the hash (calculate_hash).

Mining the block using Proof-of-Work (mine_block).

blockchain.py: Defines the Blockchain class, which manages the blockchain, including:

Adding new blocks (add_block).

Validating the blockchain’s integrity (validate_chain).

Printing the chain’s blocks (print_chain).

main.py: The entry point to the program. It:

Creates a blockchain instance.

Adds blocks with transactions.

Validates the blockchain and demonstrates tampering detection.