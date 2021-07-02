#########################################################
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################

from podrum.block.default.bedrock import bedrock
from podrum.block.default.stone import stone
from podrum.block.default.dirt import dirt
from podrum.block.default.grass import grass
from podrum.world.chunk.chunk import chunk
import random, math

class Perlin:
    # probably redo this and move this to geometry/maths folder
    def __call__(self,x,y): 
        return int(sum(self.noise(x*s,y*s)*h for s,h in self.perlins)*self.avg)
    def __init__(self, seed):
        self.m = 60000 # 100-70000 are most stable values
        p = list(range(self.m))
        random.Random(seed).shuffle(p) # seeded shuffle
        self.p = p+p
        p = self.perlins = tuple((1/i,i) for i in (16,20,22,31,32,64,512) for j in range(2))
        self.avg = 8*len(p)/sum(f+i for f,i in p)

    def fade(self,t): 
        return t*t*t*(t*(t*6-15)+10)
    def lerp(self,t,a,b): 
        return a+t*(b-a)
    def grad(self,hash,x,y,z):
        h = hash&15
        u = y if h&8 else x
        v = (x if h==12 or h==14 else z) if h&12 else y
        return (u if h&1 else -u)+(v if h&2 else -v)

    def noise(self,x,y,z=0):
        p,fade,lerp,grad = self.p,self.fade,self.lerp,self.grad
        xf,yf,zf = math.floor(x),math.floor(y),math.floor(z)
        X,Y,Z = xf%self.m,yf%self.m,zf%self.m
        x-=xf; y-=yf; z-=zf
        u,v,w = fade(x),fade(y),fade(z)
        A = p[X  ]+Y; AA = p[A]+Z; AB = p[A+1]+Z
        B = p[X+1]+Y; BA = p[B]+Z; BB = p[B+1]+Z
        return lerp(w,lerp(v,lerp(u,grad(p[AA],x,y,z),grad(p[BA],x-1,y,z)),lerp(u,grad(p[AB],x,y-1,z),grad(p[BB],x-1,y-1,z))),
                      lerp(v,lerp(u,grad(p[AA+1],x,y,z-1),grad(p[BA+1],x-1,y,z-1)),lerp(u,grad(p[AB+1],x,y-1,z-1),grad(p[BB+1],x-1,y-1,z-1))))

class default:
    generator_name: str = "default"

    @staticmethod
    def generate(chunk_x: int, chunk_z: int, world: object) -> object:
        result: object = chunk(chunk_x, chunk_z)
        spawn_position: object = world.get_spawn_position()
        # Default: 62, Reduced to 20 for faster load time
        sea_level: int = 20
        seed: int = 2151901553968352745

        # generates perlin noise
        perlin = Perlin(seed=seed)

        # chunk generation
        for x in range(0, 16):
            for z in range(0, 16):
                y = perlin((chunk_x*16)+x, (chunk_z*16)+z)
                result.set_block_runtime_id(x, sea_level+y, z, grass().runtime_id)

                # fills in gaps underneath grass
                for i in range(sea_level+y+1):
                    if (sea_level + (y-i)) == 0: 
                        result.set_block_runtime_id(x, (sea_level + (y - i)), z, bedrock().runtime_id)
                    elif (sea_level + (y-i)) <= 2: 
                        result.set_block_runtime_id(x, (sea_level + (y - i)), z, random.choice([bedrock().runtime_id, stone().runtime_id]))
                    elif (i <= 2): 
                        result.set_block_runtime_id(x, (sea_level + (y-i))-1, z, dirt().runtime_id)
                    else: 
                        result.set_block_runtime_id(x, (sea_level + (y-i))-1, z, stone().runtime_id)

        if chunk_x == spawn_position.x >> 4 and chunk_z == spawn_position.z:
            spawn_position.y = 256
            world.set_spawn_position(spawn_position)
        return result
