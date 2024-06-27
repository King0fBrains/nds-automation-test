
<h3 align="center"><img src="/gui/ui/icon.png" alt="logo" height="120px"></h3>
<p align="center"> 
<a href="/docs/LICENSE.MD"><img src=https://img.shields.io/badge/License-GPL%20v3-yellow.svg></a>
<a href="https://github.com/10BenAgain/NDS-Automation/releases"><img src=https://img.shields.io/badge/release-version></a>
</p>
<h2 align="center">Nintendo DS Automation Project</h2>

Th primary purpose of this project is to automate Pokemon RNG sequences (specifically Generation 3 games) by simulating button presses through the use of microcontrollers such as the [Arduino](https://www.arduino.cc/). This project is more a proof of concept and is something I'd been theory crafting for a long time. My hope is that it could potentially be used and expanded to assist in researching these games on real hardware. This concept is not limited to just the Nintendo DS. Seemingly all of the older consoles work the same and the concepts here can definitely be applied to the GBA, GBA SP, NDS Lite, and DSi. Since the Arduino is very simple to write code in, this project is easily expandible to accomodate for lots and lots of different sequences. Doing only basic static encounters is just the easiest to simulate. 

<p align="center">
<img src=img\mod.jpg alt="modded console" height="360px">
<img src=img\janky_ds.jpg alt="first shiny" height="360px">
</p>

<p align="center">The image to the right is the first shiny I manipped using this setup.</p>

## How it Works
The Nintendo DS has 14 buttons on the mainboard. Each button has a corresponding touch point . For example, the `B` button touch point is labeled `PO1`, the `Start` button is labeled as `PO3`, and so on. When the corresponding touch point is grounded to the motherboard ground `VGND` point, the button is pressed. Using a simple transistor as a switch, we are able to ground the button touch points with incredible speed and accuracy. To actually send the singals to ground the connections, we use a Microcontroller as the brains of the operation. Given a set of instructions, the Microcontroller (Arduino) can press, hold, and wait buttons. The arduino script in this project is designed to accept specific instructions over serial communication and then execute them with the precision needed to succesfully perform an RNG manipulation in game.   

The components to make this work is threefold: 
```
1. Physical modifications (hardmodding) to the Nintendo DS 
2. Arduino program 
3. Timer and encounter GUI to send instructions to the Arduino. 
```

## Roadmap
- [ ] Optimize Arduino Sequences to reduce memory usage
- [ ] Unit tests for Arduino 
- [ ] Implement common/easy painting method routes
- [ ] Research more optimal timings for encounters
- [ ] Generation 4 RNG Sequences

## Credits
- [@King0fBrains](https://github.com/King0fBrains) for his help with Python and testing
- Everyone in Blisy's Retail RNG Server
- [@snesman99](https://www.tumblr.com/p0stalguy) for creating the logo 

### Links: \[[Hardware Guide](docs/hardware.md)] \[[Software Guide](docs/software.md)] \[[License](docs/LICENSE.MD)]  
