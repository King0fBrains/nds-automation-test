# Hardware
> [!CAUTION]
> This process requires dissasembly and hardware modification. I am not responsible for any damage you may cause to your console by attempting to replicate these modifcations. Modify at your own risk!

### Required Materials
- Any Arduino Board that has at least 13 GPIO Pins. I use the [Arduino Nano](https://store-usa.arduino.cc/products/arduino-nano?selectedStore=us)
- 1 - Soldering Iron 
- 1 - Solder wire (Rosin core is easier to work with)
- 1 - Breadboard (Double, long one)
- 1 - Phillips #00 Screwdriver
- 1 - Tri‑point Y00 Screwdriver
- 1 - 30 Gauge Stranded Tinned Copper Wire with Silicone Insulation
- 1 - Cutting Tweezers/Cuticle Cutter
- 1 - Small file
- 14 - BC546/547/548/549/550 NPN Transistor 
- 14 - 4.7k Ohm Resistors
### Optional Materials
- Spudger/Plastic Pry Tool (HIGHLY Recommended)
- Small Tweezers
- Electrical Tape
- De-Soldering Wick 
- Isopropyl Aclohol

## Installation
The basic idea of this installation is that we are sort of hijacking the console's button wires. Essentially what is happening that when any DS button is pressed, current is allowed to flow to the CPU for processing. It's definitely not that simple but that's how I visualize it. In my research, I observed a ~3.2 voltage drop across each switch. Since we are working with very low amperage, the BC546 NPN transistor is perfect for the job. (Also its included in a lot of Arduino kits). Each Arduino pin in this project is set as an output which supplies the circuit with 5V. Below is a rough diagram of the circuit. I am no expert in electronics so this may be incorrect (and oversimplified)
<p align="center">
<img src=/img/ds_circuit.png alt="circuit diagram" height="280px">
</p>

### Dissasembly
It is recommended to folow the dissambly instuctions as outlined in this [iFixit](https://www.ifixit.com/Guide/Nintendo+DS+Bottom+LCD+Screen+Replacement/1304) guide. There is no need to actually remove the lower screen from the housing, so follow this guide up until step 10.

Once you have the motherboard out of the housing set it aside for soldering.  

> [!NOTE] 
> Conduct a visual inspection of the board. While you have it out and there is noticeable gunk/goop, you might as well clean it up with some isopropyl. 


### Soldering

Below is a table with the touch points and their respective buttons:

| Component Name | Touch Point Label | Button       |
| -------------  | -------------     | :----------: |
| SW1            | PO0               |    A         |
| SW2            | PO1               |    B         |
| SW3            | PO8               |    R         |
| SW4            | PO3               |    Start     |
| SW5            | PO4               |    Right     |
| SW6            | PO5               |    Left      |
| SW7            | PO6               |    Up        |
| SW8            | PO7               |    Down      |
| SW9            | PO2               |    Select    |
| SW10           | PO9               |    L         |
| SW11           | RO0               |    X         |
| SW12           | RO1               |    Y         |
| SW13           | PWSW              |    Power     |


1. Locate all the touch points and clean them with ispropyl to create a clean sruface. 
2. Apply a small amount of solder to each touch point to mix in the leaded solder with the factory material.
3. Measure out your 13 wires to a desired length. The longer the better. Once the wires are secure, they can be cut to a more uniform length. 
4. Solder one wire per touch pad. It should not take much effort to secure the wire. My method is to press the wire against the fresh solder and place the iron on top of it for a brief second to let the solder melt, then quickly release once its fused together.
5. Finally, cut one last wire and solder it to the ground pin labeled `VGND` at the bottom of the power connector


> [!IMPORTANT]
> When creating a path for your wires, make sure they are not soldered to the board at an angle to which they overlap where the physical buttons are. If there is a wire that is laid across the push button, you most likely wont be able to press it once reassembled. 


This is how I routed my wires: 
<p align="center">
<img src=/img/NDS_Reg_Wiring_Drawing.png alt="drawing of wiring diagram" height="560px">
</p>

Before continuing, its good practice to test for continuity. Simply set your multimeter to its continuity mode and press one end to the touch point surface and the other to the end of the corresponding wire. This way we can eliminate the possibility of the wire itself being faulty. 

### DS Shell Modification
We need to cut out a small strip of plastic from the NDS Shell in order for the newly inserted wires to be accessible.  
1. Use your cutting tweezers to cut the plastic guard strip right above the GBA slot as shown in the image below:
<p align="center">
<img src=/img/wire_cut_assembled.jpg alt="cut out console shell" height="560px">
</p>

2. File down the rough plastic edges made from the cuts
3. Route the wires thru the newly cut slit then reassemble the console adjusting the wire positions so they dont intefere with internal components. 
<p align="center">
<img src=/img/wires_out.jpg alt="wires coming out of modded console" height="560px">
</p>
4. Once assembled, test each button by grounding the button wires to the ground pin wire to simulate a button press. If all the buttons are working, continue to the breadboard step. If at this point you have wires that do not simulate a button press, you most likely have a cold solder joint on one of the touch pins. Go back and reasses the wire contacts to see if they are properly secured to the touch pins. 

### Arduino + Breadboard Setup

The basic setup to connecting your wires to the Arduino is simple. 
1. Connect your ground wire from the DS to the breadboard ground rail.
2. Use a jumper cable to connect the ground rail to the ground pin on the Arduino
   
<p align="center">
<img src=/img/bread1.png alt="tinkercad breadboard" height="560px">
</p>

3. Place a transistor as shown in the diagram below then add a resistor to the base pin of the transistor. Then add a jumper wire from `pin 2` on the Arduino to the resistor. Finally add a jumper wire from the emitter pin to the breadboard ground rail.

<p align="center">
<img src=/img/bread2.png alt="tinkercad breadboard" height="560px">
</p>

4. Now connect the wire from the DS that is connected to the `A` button (SW1) to the collector pin of the transistor
5. Repeat this process for each button following this button to Arduino pin sequence. If you plan on never using certain buttons like X, Y, L, R then there is no reason to add these wires. As of the most recent update, the Arduino does not interact with the power button. I just wired it up to a push button so I could power cycle the console without pressing the onboard button.
   - Arduino Pin 2 = A
   - Pin 3 = B
   - Pin 4 = X
   - Pin 5 = Y
   - Pin 6 = Left
   - Pin 7 = Right
   - Pin 8 = Up
   - Pin 9 = Down
   - Pin 10 = L
   - Pin 11 = R
   - Pin 12 = Select
   - Pin 13 = Start
   - Pin 14 = Power


You are now ready to continue to flashing your Arduino!
