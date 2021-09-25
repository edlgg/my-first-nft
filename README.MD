# My First NFT
This repo was created with the goal of learning how to create an nft.
You can see the result here:
https://opensea.io/assets/ethereum/0xe29ffe4010fd707442342dde5702e149443c6d05/0

Instructions:
Add this 2 system variables
PRIVATE_KEY: You can get this on your metamask wallet
WEB3_INFURA_PROJECT_ID: You can create one on the infura website

## Test on Rinkevy network
brownie run scripts/deploy_simple.py --network rinkeby
brownie run scripts/create_collectible.py --network rinkeby

## Deploy to MainNet
brownie run scripts/deploy_simple.py --network mainnet
brownie run scripts/create_collectible.py --network mainnet