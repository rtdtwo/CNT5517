# Lab 4

## Part 1 - Microservices
### Directory structure
In the folder `part1`, you can find the following files:
- `part1.cpp` : Contains base code that allows usage of the microservice functions using a command line interface.
- `ThingManager.cpp` : Contains implementation of the functions defined in `ThingManager.h`.
- `ThingManager.h` : Contains the function blueprint that enables the microservices to be used as a header file.

### Running the code
With part1 as the current working directory, run the following commands to execute the code:

`g++ part1.cpp ThingManager.cpp ThingManager.h - lwiringPi`

`./a.out`

## Part 2 - Atlas IoT
### Directory structure
In the folder `part2`, you can find the following files:
- `part2.py` : The Python application that acts as an interface between the user and the Atlas IoT framework.
- `socket_manager.py` : Contains helper code that initiates connection with the Atlas IoT Framework. In the folder `AtlasConfiguration`, you can find the following files:
- `Atlas_IoTDDL.xml` : The configuration XML file that is generated using the Atlas IoT Framework Builder.
### Running the code
- Assuming that you have Atlas IoT framework installed and set up on your machine, copy the XML configuration file to the appropriate location.
- Then, run the following to start Atlas IoT Framework: `./Atlas`.
- Afterwards, in a different terminal window, set `part2` as the current working directory and run the following to start the Python application. `python3 part2.py`
