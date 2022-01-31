#include <iostream>
// include our header file
#include "ThingManager.h"

using namespace std;

/**
 * Main Program.
 * Generates a simple menu on the console.
 * Calls the appropriate functions from the header file, as per the user input.
 */
int main(int argc, char const *argv[])
{
    while (true)
    {
        int choice;
        int smsStatus;
        int btnStatus;
        int beepCount;

        cout << "Select option:\n";
        cout << "1. Turn on LED\n";
        cout << "2. Turn off LED\n";
        cout << "3. Get Soil Moisture Status\n";
        cout << "4. Beep Buzzer\n";
        cout << "5. Get pushbutton status\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            turnOnLed();
            cout << "\nLED turned ON\n\n";
            break;
        case 2:
            turnOffLed();
            cout << "\nLED turned OFF\n\n";
            break;
        case 3:
            smsStatus = getSoilMoistureStatus();
            if (smsStatus)
            {
                cout << "\nMoisture AVAILABLE in soil\n\n";
            }
            else
            {
                cout << "\nMoisture NOT AVAILABLE soil\n\n";
            }
            break;
        case 4:
            cout << "Enter number of times you wish to beep: ";
            cin >> beepCount;
            playBuzzer(beepCount);
            cout << "\nBuzzer Beeped\n\n";
            break;
        case 5:
            btnStatus = getButtonState();
            if (btnStatus)
            {
                cout << "\nPushbutton PRESSED\n\n";
            }
            else
            {
                cout << "\nPushbutton NOT PRESSED\n\n";
            }
            break;
        default:
            cout << "\nGoodbye!\n\n";
            return 0;
            break;
        }
    }

    return 0;
}
