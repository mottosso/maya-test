from maya import standalone, cmds
standalone.initialize()
print(cmds.about(version=True))
