class ProtocolInfo:
    # Versions info
    CURRENT_PROTOCOL = 753
    VERSION = "v1.16.3"
    VERSION_NETWORK = "1.16.3"

    # Handshake Protocol info
    HANDSHAKING = 0x00
    LEGACY_SERVER_LIST = 0xfe
    RESPONSE = 0x00
    PONG = 0x01
    REQUEST = 0x00
    PING = 0x01
    
    # Login Protocol info
    DISCONNECT = 0x00
    ENCRYPTION_REQUEST = 0x01
    LOGIN_SUCCESS = 0x02
    SET_COMPRESSION = 0x03
    LOGIN_PLUGIN_REQUEST = 0x04
    LOGIN_START = 0x00
    ENCRYPTION_RESPONSE = 0x01
    LOGIN_PLUGIN_RESPONSE = 0x02

    # Play Protocol info
    SPAWN_ENTITY = 0x00
    SPAWN_EXPERIENCE_ORB = 0x01
    SPAWN_LIVING_ENTITY = 0x02
    SPAWN_PAINTING = 0x03
