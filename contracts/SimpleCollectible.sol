// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    uint256 public tokenCounter;

    constructor() public ERC721("My First NTF", "My First NFT") {
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI)
        public
        returns (uint256)
    {
        // if (tokenCounter < 1) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newItemId;
        // }
        // return 1;
    }
}
