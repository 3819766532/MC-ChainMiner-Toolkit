# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()

LIGHT_ITEMS = set([
    "minecraft:torch",
    "minecraft:lantern",
    "minecraft:soul_lantern",
    "minecraft:soul_torch",
    "minecraft:glowstone",
    "minecraft:shroomlight",
    "minecraft:jack_o_lantern",
    "minecraft:sea_lantern",
])


class BlankServer(ServerSystem):
    def __init__(self, namespace, systemName):
        super(BlankServer, self).__init__(namespace, systemName)
        self.chainEnabled = True
        self.chainRadius = 3
        self.lightEnabled = True
        self.lightPosMap = {}
        self._Listen()
        print("[EnhancedTools] Server started")

    def _Listen(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(),
                            serverApi.GetEngineSystemName(),
                            "DestroyBlockEvent", self, self.OnDestroyBlock)

    def OnDestroyBlock(self, event):
        if not self.chainEnabled:
            return
        try:
            x = event.get("x", 0)
            y = event.get("y", 0)
            z = event.get("z", 0)
            fullName = event.get("fullName", "")
            auxData = event.get("auxData", 0)
            playerId = event.get("playerId", "")
            dimId = event.get("dimensionId", 0)
            if not playerId or not fullName:
                return
            self._ChainMine(x, y, z, dimId, fullName, auxData)
        except Exception as e:
            print("[EnhancedTools] chain error: %s" % e)

    def _ChainMine(self, sx, sy, sz, dimId, targetName, targetAux):
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(dimId)
        r = self.chainRadius
        visited = set()
        queue = [(sx, sy, sz)]
        visited.add((sx, sy, sz))
        count = 0
        maxBlocks = r * r * r * 5
        while queue and count < maxBlocks:
            cx, cy, cz = queue.pop(0)
            for dx in range(-r, r + 1):
                for dy in range(-1, 2):
                    for dz in range(-r, r + 1):
                        nx, ny, nz = cx + dx, cy + dy, cz + dz
                        if (nx, ny, nz) in visited:
                            continue
                        visited.add((nx, ny, nz))
                        bi = comp.GetNewBlock((nx, ny, nz))
                        if bi is None:
                            continue
                        if bi.get("name", "") == targetName and bi.get("aux", 0) == targetAux:
                            comp.DestroyBlock((nx, ny, nz), True, True)
                            count += 1
                            queue.append((nx, ny, nz))
                            if count >= maxBlocks:
                                return

    def Update(self):
        pass

    def Destroy(self):
        pass
