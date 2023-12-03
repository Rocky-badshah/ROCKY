import os,platform
os.system("git pull")
a=platform.architecture()[0]
if "64" in a:
    import ROCKY
    ROCKY.run()
elif "32" in a:
    import ROCKY32
    ROCKY32.run()