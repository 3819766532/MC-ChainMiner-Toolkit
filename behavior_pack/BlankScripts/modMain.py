# -*- coding: utf-8 -*-
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
import config


@Mod.Binding(name=config.mod_name, version="1.0.0")
class EnhancedToolsMod(object):
    def __init__(self):
        pass

    @Mod.InitServer()
    def InitServer(self):
        serverApi.RegisterSystem(config.mod_name, config.server_system_name, config.server_class_path)

    @Mod.DestroyServer()
    def DestroyServer(self):
        pass

    @Mod.InitClient()
    def InitClient(self):
        clientApi.RegisterSystem(config.mod_name, config.client_system_name, config.client_class_path)

    @Mod.DestroyClient()
    def DestroyClient(self):
        pass
