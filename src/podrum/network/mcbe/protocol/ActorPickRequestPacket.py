from podrum.utils.BinaryStream import BinaryStream
from podrum.network.mcbe.protocol.DataPacket import DataPacket
from podrum.network.mcbe.protocol.Info import Info

class ActorPickRequest(DataPacket, BinaryStream):
    networkId = Info.ACTOR_PICK_REQUEST_PACKET

    entityuniqueid = None
    hotbarSlot = None

    def decodePayload(self):
        self.entityuniqueid = BinaryStream.getLLong()
        self.hotbarSlot = BinaryStream.getByte()

    def encodePayload(self):
        self.putLLong(self.entityuniqueid)
        self.putByte(self.hotbarSlot)