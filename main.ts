bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Happy)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    msg = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    // zmiana trybu
    if (msg == "mode_dpad") {
        mode = 0
        basic.showString("D")
    } else if (msg == "mode_analog") {
        mode = 1
        basic.showString("A")
    } else if (msg == "mode_accelerometer") {
        mode = 2
        basic.showString("T")
    } else {
        // dpad
        if (mode == 0) {
            if (msg == "UP") {
            	
            } else if (msg == "DOWN") {
            	
            } else if (msg == "LEFT") {
            	
            } else if (msg == "RIGHT") {
            	
            } else if (msg == "left" || msg == "right" || msg == "up" || msg == "down") {
            	
            }
        }
        // analog + accelerometer
        if (mode == 1 || mode == 2) {
            parseAndDriveAxes(msg)
        }
    }
})
// format: X+05,Y-72
function parseAndDriveAxes (frame: string) {
    if (frame.length < 9) {
        return
    }
    if (frame.substr(0, 1) != "X") {
        return
    }
    if (frame.substr(4, 2) != ",Y") {
        return
    }
    x = parseFloat(frame.substr(1, 3))
    y = parseFloat(frame.substr(6, 3))
    driveFromAxes(x, y)
}
function driveFromAxes (ax: number, ay: number) {
    left = ay - ax
    right = ay + ax
}
let right = 0
let left = 0
let y = 0
let x = 0
let mode = 0
let msg = ""
basic.showIcon(IconNames.SmallDiamond)
bluetooth.startUartService()
