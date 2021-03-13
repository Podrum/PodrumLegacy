################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

class raknet_packet_ids:
    online_ping: int = 0x00
    offline_ping: int = 0x01
    offline_ping_open_connections: int = 0x02
    online_pong: int = 0x03
    open_connection_request_1: int = 0x05
    open_connection_reply_1: int = 0x06
    open_connection_request_2: int = 0x07
    open_connection_reply_2: int = 0x08
    connection_request: int = 0x09
    connection_request_accepted: int = 0x10
    new_incoming_connection: int = 0x13
    disconnect: int = 0x15
    incompatible_protocol_version: int = 0x19
    offline_pong: int = 0x1c
    frame_set_0: int = 0x80
    frame_set_1: int = 0x81
    frame_set_2: int = 0x82
    frame_set_3: int = 0x83
    frame_set_4: int = 0x84
    frame_set_5: int = 0x85
    frame_set_6: int = 0x86
    frame_set_7: int = 0x87
    frame_set_8: int = 0x88
    frame_set_9: int = 0x89
    frame_set_a: int = 0x8a
    frame_set_b: int = 0x8b
    frame_set_c: int = 0x8c
    frame_set_d: int = 0x8d
    frame_set_e: int = 0x8e
    frame_set_f: int = 0x8f
    nack: int = 0xa0
    ack: int = 0xc0
