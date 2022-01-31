import socket_manager


# Main Program.
# Generates a simple menu on the console.
# Calls the appropriate service calls as per the user input.
while True:
    print("======================================")
    print("\tRTX2080 ATLAS SERVICES")
    print("======================================")
    print("(1) Turn On LED")
    print("(2) Turn Off LED")
    print("(3) Get soil moisture status")
    print("(4) Get pushbutton status")
    print("(5) Beep Buzzer")
    print("(6) Exit")
    print("\nEnter your choice:")
    choice = int(input())
    result = None

    if choice == 1:
        # Send call to Turn On LED
        result = socket_manager.send_service_call('TurnOnLED', 'LED', ())
    elif choice == 2:
        # Send call to Turn Off LED
        result = socket_manager.send_service_call('TurnOffLED', 'LED', ())
    elif choice == 3:
        # Send call to get status of the soil moisture sensor
        result = socket_manager.send_service_call('SMSStatus', 'SMS', ())
    elif choice == 4:
        # Send call to get the status of pushbutton
        result = socket_manager.send_service_call('BTNStatus', 'BTN', ())
    elif choice == 5:
        # Get the number of times the user wishes for the buzzer to beep
        print('Enter number of times you wish to beep: ')
        count = input()
        # Send call to beep the buzzer, pass count as parameter
        result = socket_manager.send_service_call(
            'BeepBuzzer', 'BUZZ', (int(count)))
    elif choice == 6:
        # Exit
        print("Bye!")
        break
    else:
        print("\nUnsupported choice!\n")

    if result is not None:
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if result[0]:
            # Print the result received from Atlas IoT
            print('EXECUTED Choice {}. Result was: {}.'.format(
                choice, result[1]["Status Description"]))
            if choice == 3:
                # If the service result of the soil moisture sensor status call was 1,
                # print that moisture is available, or not otherwise.
                if int(result[1]["Service Result"]) == 1:
                    print('Moisture available')
                else:
                    print('Moisture unavailable')
            elif choice == 4:
                # If the service result of the pushbutton press status call was 1,
                # print that pushbutton is pressed, or not otherwise.
                if int(result[1]["Service Result"]) == 1:
                    print('Button pressed')
                else:
                    print('Button not pressed')
        else:
            print('\nService {} execution failed due to a TCP error.'.format(choice))
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
