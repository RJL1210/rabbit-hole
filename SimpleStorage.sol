// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

contract SimpleStorage {
    uint256 private storedData;

    event DataStored(uint256 data);

    function set(uint256 x) public {
        storedData = x;
        emit DataStored(x);
    }

    function get() public view returns (uint256) {
        return storedData;
    }

    struct Person {
        string name;
        uint256 age;
    }

    Person public pat = Person({name: "Patrick", age: 30});

    Person[] public people;
}
