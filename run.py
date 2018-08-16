from maya import standalone, cmds
standalone.initialize()

cmds.file(new=True, force=True)
cube, _ = cmds.polyCube(name="testCube")
print(cube)
