"""
*  ____           _
* |  _ \ ___   __| |_ __ _   _ _ __ ___
* | |_) / _ \ / _` | '__| | | | '_ ` _ \
* |  __/ (_) | (_| | |  | |_| | | | | | |
* |_|   \___/ \__,_|_|   \__,_|_| |_| |_|
*
* Licensed under the Mozilla Public License, Version 2.
* Permissions of this weak copyleft license are conditioned on making
* available source code of licensed files and modifications of those files 
* under the same license (or in certain cases, one of the GNU licenses).
* Copyright and license notices must be preserved. Contributors
* provide an express grant of patent rights. However, a larger work
* using the licensed work may be distributed under different terms and without 
* source code for files added in the larger work.
"""

class Info:
    mcpiProtocol = 9
    mcpiVersion = "v0.1.1"
    mcpiVersionNetwork = "0.1.1"
    loginPacket = 0x82
    loginStatusPacket = 0x83
    readyPacket = 0x84
    messagePacket = 0x85
    setTimePacket = 0x86
    startGamePacket = 0x87
    addMobPacket = 0x88
    addPlayerPacket = 0x89
    removePlayerPacket = 0x8a
    addEntityPacket = 0x8c
    removeEntityPacket = 0x8d
    addItemEntityPacket = 0x8e
    takeItemEntityPacket = 0x8f
    moveEntityPacket = 0x90
    moveEntityPosrotPacket = 0x93
    movePlayerPacket = 0x94
    placeBlockPacket = 0x95
    removeBlockPacket = 0x96
    updateBlockPacket = 0x97
    addPaintingPacket = 0x98
    explodePacket = 0x99
    levelEventPacket = 0x9a
    titleEventPacket = 0x9b
    entityEventPacket = 0x9c
    requestChunkPacket = 0x9d
    chunkDataPacket = 0x9e
    playerEquipmentPacket = 0x9f
    playerArmorEquipmentPacket = 0xa0
    interactPacket = 0xa1
    useItemPacket = 0xa2
    playerActionPacket = 0xa3
    hurtArmorPacket = 0xa5
    setEntityDataPacket = 0xa6
    setEntityMotionPacket = 0xa7
    setHealthPacket = 0xa8
    setSpawnPositionPacket = 0xa9
    animatePacket = 0xaa
    respawnPacket = 0xab
    sendInventoryPacket = 0xac
    dropItemPacket = 0xad
    containerOpenPacket = 0xae
    containerClosePacket = 0xaf
    containerSetSlotPacket = 0xb0
    containerSetDataPacket = 0xb1
    containerSetContentPacket = 0xb2
    containerAckPacket = 0xb3
    chatPacket = 0xb4
    signUpdatePacket = 0xb5
    adventureSettingsPacket = 0xb6  
