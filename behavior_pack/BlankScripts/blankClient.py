# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class BlankClient(ClientSystem):
    def __init__(self, namespace, systemName):
        super(BlankClient, self).__init__(namespace, systemName)
        print("[EnhancedTools] Client started")

    def Update(self):
        pass

    def Destroy(self):
        pass
