# We are not currently using this, but we will eventually use it to convert the player's gold pieces into other coin types.
# For now, we are just using gold pieces.

class Coin_Types:
    copper = 1
    silver = 10
    electrum = 50
    gold = 100
    platinum = 1000

    def get_info(self):
        print(f"Copper Pieces: {self.copper}")
        print(f"Silver Pieces: {self.silver}")
        print(f"Electrum Pieces: {self.electrum}")
        print(f"Gold Pieces: {self.gold}")
        print(f"Platinum Pieces: {self.platinum}")
        return