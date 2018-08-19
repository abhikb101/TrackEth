pragma solidity ^0.4.24;
// We have to specify what version of compiler this code will compile with
contract face
{
    uint8[] uid;
   // uint8[] systemid;
    mapping(uint8=>uint8[]) mapSystem;
    function addPerson(uint8 _uid, uint8 _systemid)
    {
        uid.push(_uid);
        mapSystem[_uid].push(_systemid);
    }
    function getPerson(uint8 _uid) view public returns (uint8[])
    {
        return mapSystem[_uid];
    }
}