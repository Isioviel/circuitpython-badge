Hardware Overview
*****************

The badge consists of several main components:

Microcontroller
===============

The microcontroller controlling everything is an Atmel SAMD21, an ARM Cortex-M0
microcontroller running at 48MHz. It has native USB support, which lets us
expose the filesystem on the device as a USB disk and the REPL console as a
serial device. It's running a custom version of CircuitPython, an
implementation of the Python language for microcontrollers based on
MicroPython.

All of the GPIO pins are exposed in the ``board`` module, which lets us use
them from CircuitPython.


Buttons
=======

The device has eight buttons, arranged into two crosses, that can be used to
control the code running on it. The buttons are connected to GPIO pins on one
end, and to GND on the other, and they are scanned in the background by the
``gamepad`` module. The state of the buttons can be accessed with the
``badge.keys()`` function.


Display
=======

There is a display of 14×11 red pixels on the device, controlled by a
IS31FL3733 chip connected over an I²C bus to the ``board.SDA0`` and
``board.SCL0`` pins. It can be accessed with the ``badge.show()`` function and
its brightness can be adjusted with the ``badge.brightness()`` function. It's
capable of displaying 256 shades of red, however, since most of those shades
are very similar, the library selects only 16 distinct shades that you can use.


Accelerometer
=============

There is a LIS3DH accelerometer in the middle of the board, under the display,
which can be used to read the position and movement of the device. It is also
connected over an I²C protocol to the ``board.SDA0`` and ``board.SCL0`` pins.
It can be accessed with the ``badge.accel()`` function.


Radio
=====

There is an NRF24L01+ radio module on board, connected to the ``board.RADIO*``
pins. The connections are as follows:

    * ``RADIO0`` — ``CE``
    * ``RADIO1`` — ``CSN``
    * ``RADIO3`` — ``SCK``
    * ``RADIO4`` — ``MOSI``
    * ``RADIO5`` — ``MISO``

There are currently no built-in functions or libraries for handling the
communication with this module. And external library needs to be used.


Power
=====

The device is powered with three 1.5V AAA alkaline batteries or the USB port.
The source of power is switched with the power switch. In the "ON" position,
the power comes from the batteries, while in the "OFF" position, it's powered
from the USB port (if it's connected).
