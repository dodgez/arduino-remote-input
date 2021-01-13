# arduino-remote-input
This repository contains code for an Arduino to send input to a computer.
Currently the [controller code](controller/controller.ino) gets input from three buttons and presses and releases keys according to the provided key mapping ([example_keys.json](example_keys.json) by default).

Steps to use this software:
1. Connect a compatible Arduino to the computer via a USB cable (I use Arduino Mega 2560).
2. Upload [controller/controller.ino](controller/controller.ino) to the Arduino.
3. Obtain the port the Arduino is connected on, e.g. COM3 on Windows.
4. Launch the main python script (use `python main.py --help` for more information)
