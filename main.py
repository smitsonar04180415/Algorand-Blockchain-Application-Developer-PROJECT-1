from blockchain import Blockchain


def show(chain):
    for b in chain.chain:
        print(f"Block {b.index}")
        print(f"  data:      {b.data}")
        print(f"  prev hash: {b.previous_hash[:16]}...")
        print(f"  hash:      {b.hash[:16]}...  (nonce: {b.nonce})")
        print()


if __name__ == "__main__":
    bc = Blockchain()
    bc.add_block("Alice pays Bob 5 coins")
    bc.add_block("Bob pays Carol 2 coins")

    show(bc)
    print("Chain valid?", bc.is_valid())

    print("\n--- Tampering with block 1 ---")
    bc.chain[1].data = "Alice pays Bob 500 coins"
    print("Chain valid?", bc.is_valid())
