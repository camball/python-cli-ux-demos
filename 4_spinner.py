from time import sleep
from halo import Halo

spinner = Halo(text="Loading", spinner="dots")
spinner.start()

sleep(3)

spinner.stop()
