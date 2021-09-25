#!/usr/bin/python3
from brownie import SimpleCollectible, accounts, network, config
from scripts.helpful_scripts import OPENSEA_FORMAT

sample_token_uri = "https://firebasestorage.googleapis.com/v0/b/leybot-1566250977455.appspot.com/o/my-first-nft.json?alt=media&token=9e708052-e5ab-46de-98ce-fec6fdb7f265"


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    simple_collectible = SimpleCollectible[len(SimpleCollectible) - 1]
    token_id = simple_collectible.tokenCounter()
    transaction = simple_collectible.createCollectible(sample_token_uri, {"from": dev})
    transaction.wait(1)
    print(
        "Awesome! You can view your NFT at {}".format(
            OPENSEA_FORMAT.format(simple_collectible.address, token_id)
        )
    )
    print('Please give up to 20 minutes, and hit the "refresh metadata" button')
