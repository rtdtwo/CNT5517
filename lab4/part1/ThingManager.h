// A header file that defines the functions available to manage our things
// connected to our RPi. Implemented by {ThingManager.cpp} and used by {part1.cpp}.

// Standard header file declaration
#ifndef THINGMANAGER_H
#define THINGMANAGER_H

// Function to turn on our LED.
void turnOnLed();

// Function to turn off LED.
void turnOffLed();

// Function to get Pushbutton state.
bool getButtonState();

// Function to beep the buzzer for {count} number of times.
void playBuzzer(int count);

// Function to get the status of our soil moisture sensor.
bool getSoilMoistureStatus();

// Standard header file ending.
#endif
