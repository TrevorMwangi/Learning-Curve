from solders.keypair import Keypair

keypair = Keypair()
print(f"Public Key (Address): {keypair.pubkey()}")
