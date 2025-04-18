#!/usr/bin/env -S uv run
# /// script
# dependencies = ["numpy", "pyusb"]
# ///

from pyrow import pyrow

ergs = pyrow.find()

for ergid in ergs:
    erg = pyrow.PyErg(ergid)
    print(erg.get_status())
    print(erg.get_erg())
