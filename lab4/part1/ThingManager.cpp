#include <iostream>
#include <csignal>
// Including WiringPi library
#include <wiringPi.h>
// Including our ThingManager.h header file
#include "ThingManager.h"

// Constants that define what thing resides at which pin.
#define LED_PIN 4
#define BUZZER_PIN 16
#define SMS_PIN 21
#define BTN_PIN 23

/**
 * Turn ON the LED connected to our Raspberry Pi.
*/
void turnOnLed()
{
    wiringPiSetupGpio();
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, HIGH);
}

/**
 * Turn OFF the LED connected to our Raspberry Pi.
*/
void turnOffLed()
{
    wiringPiSetupGpio();
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);
}

/**
 * Get the status of the soil moisture sensor connect to our Raspberry Pi.
 * Soil moisture sensor detects if moisture is present or not in soil.
 * @return false if no moisutre present, true if moisture present.
 */
bool getSoilMoistureStatus()
{
    wiringPiSetupGpio();
    pinMode(SMS_PIN, INPUT);
    if (digitalRead(SMS_PIN) == HIGH)
    {
        return false;
    }
    else
    {
        return true;
    }
}

/**
 * Play the buzzer. The buzzer is an active buzzer.
 * @param count The number of times the buzzer should beep.
 */
void playBuzzer(int count)
{
    wiringPiSetupGpio();
    pinMode(BUZZER_PIN, OUTPUT);
    for (int i = 0; i < count; i++)
    {
        digitalWrite(BUZZER_PIN, HIGH);
        delay(100);
        digitalWrite(BUZZER_PIN, LOW);
        delay(100);
    }
}

/**
 * Get the pressed status of our Push button connected to our Raspberry Pi.
 * @return false if pushbutton is currently not pressed, true if pushbutton is pressed.
 */
bool getButtonState()
{
    wiringPiSetupGpio();
    pinMode(BTN_PIN, INPUT);
    if (digitalRead(BTN_PIN) == HIGH)
    {
        return false;
    }
    else
    {
        return true;
    }
}