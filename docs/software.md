# Software

## Requirements
1. The [Arduino IDE](https://www.arduino.cc/en/software)
2. Python [3.11](https://www.python.org/downloads/) or higher 
3. [Git](https://www.git-scm.com/) version 2.25 or higher (Optional)

### Arduino

1. Create a new folder where you want to place the Arduino files
2. Open a terminal window in that folder, or navigate to that folder in your desired terminal emulator
3. If you don't want to download the entire repository, run the following commands:
```shell
$ git clone --no-checkout https://github.com/10BenAgain/NDS-Automation.git
$ cd NDS-Automation
$ git sparse-checkout init --cone
$ git sparse-checkout set arduino/gen3
$ git checkout
```
Otherwise just run
```
$ git clone https://github.com/10BenAgain/NDS-Automation.git
```
You can also download the zipped version of the entire [repository](https://github.com/10BenAgain/NDS-Automation/archive/refs/heads/main.zip) straight from the GitHub 

4. Verify that your folder structure looks like this:
```shell
# Arduino folder structure is brittle
# *.ino file names must match parent dir
# src/ must be in .ino dir

[your folder]
└── gen3
    ├── src
    │   ├── console.cpp
    │   ├── console.h
    │   ├── emerald.cpp
    │   ├── emerald.h
    │   ├── frlg.cpp
    │   └── frlg.h
    └── gen3.ino

```
5. Open the Arduino IDE and insert your Arduino device into your computer via USB connection
6. Open the `gen3.ino` file you just downloaded in the Arduino IDE
7. Select the inserted device you want to upload the code into and press the upload button

Congradulations! You have succesfully flashed your Arduino 


## GUI

You can either download the `.exe` file in the [releases](https://github.com/10BenAgain/NDS-Automation/releases) tab for the program or run it from source.

To run from source:  
1. Again, if you don't want to clone the entire repository: 
```
$ git clone --no-checkout https://github.com/10BenAgain/NDS-Automation.git
$ cd NDS-Automation
$ git sparse-checkout init --cone
$ git sparse-checkout set gui/
$ git checkout
```
2. Navigate to the main folder `NDS-Automation` and create a new virtual environment then activate it
```shell
$ python -m venv

# Windows
$ .\venv\Scripts\activate

# *nix / MacOS
$ source venv/bin/activate
```
3. Install the required modules
```shell
$ cd gui/
$ pip install -r requirements.txt
```
4. Navigate to the program entry point if not alread there ` gui/main.py` and run it
```shell
$ cd gui/
$ python main.py
```
### User Interface - Device Selection
To select your Arduino, select the USB port from the list of devices in the `Port` dropdown. You can change the device name if you'd like. 
> Do not change the Baud Rate unless you have edited the Arduino source code to match.

Click the `add` button to add the target device to the device table. 

<p align="center">
<img src=/img/gui_dev.png alt="drawing of wiring diagram" height="560px">
</p>

When sending the instructions to the Arduino, make sure that the device number in the device dropdown matches the target device's index. If you have multiple devices/consoles, you can select which one to send it to using this dropdown. The rest of the program is very straightforward and self explanatory

