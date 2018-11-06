class Const:
    doorName={'Large': 1835674, 'Small': 1881686}
    doorState={'DoorOpen':'1',
               'DoorClose': '2',
               'DoorStopInMiddle': '3',
               'GoingUp':'4',
               'GoingDown':'5',
               'NotClosed':'9' }

    errorMessages = {
        11: 'Something unexpected happened. Please wait a bit and try again.',
        12: 'MyQ service is currently down. Please wait a bit and try again.',
        13: 'Not logged in.',
        14: 'Email and/or password are incorrect.',
        15: 'Invalid parameter(s) provided.',
        16: 'User will be locked out due to too many tries. 1 try left.',
        17: 'User is locked out due to too many tries. Please reset password and try again.',
    },

    endpoint = 'https://myqexternal.myqdevice.com'
    appId = 'NWknvuBd7LoFHfXmKNMBcgajXtZEgKUh4V7WNzMidrpUUluDpVYVZx+xT4PCM5Kx'
    MyQDeviceTypeName = {
        'Gateway':1,
        'GarageDoorOpener': 2,
        'Thermostat':11
    }


