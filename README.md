# Robotics_Club_Segway
Repository to hold control algorithms for a self balancing Segway imitation



# Software Setup (Linux)

#### 1\. Download [Ubuntu Mate](https://ubuntu-mate.org/download/) for Raspberry Pi 3 (Use the torrent option)

#### 2 \. Extract the resulting archive and flash onto SD card
 - After extracting, the file should be of the type `.image`
 - At this point you can use the `dd` command or a tool like [Etcher](https://etcher.io/) to flash the SD card

#### 3\. Set up the RPi3 using an HDMI cable / TV
 - Ubuntu Mate needs to be set up for the first time using an HDMI connection to a monitor of some sort
 - After initial setup, create a new ethernet connection with a static IP address, and set the connection to automatically connect
 - See [this site](https://help.ubuntu.com/stable/ubuntu-help/net-fixed-ip-address.html) for help, but skip steps 6-7 as this is unnecessary for the time being
 - Remember the IP address and username for later

#### 4\. Enable SSH and SPI interfaces
 - While logged into RPi3, run `$ sudo systemctl enable ssh` to enable the ssh server at startup
 - Run `$ sudo raspi-config` and choose `Interfacing Options` -> `SPI` -> `Yes` to enable SPI
 - A restart or `$ sudo service ssh start` may be required to start the ssh service

#### 5\. Check that you can ssh into the RPi3 from your computer
 - If I chose my username/IP as rpi3/192.168.2.2, the command would be `$ ssh rpi3@192.168.2.2`
 - If this does not work, check that your ssh service is running, and the IP address was established correctly
    - To check ssh status: `$ sudo service ssh status`
    - To check IP address: `$ hostname -I` or `$ ifconfig`
 - Once logged in, create a new folder in the `~/` directory for placing code ex: `$ mkdir ~/segway`


#### 4\. Clone this repository and run [setup.py](setup.py)
 - Enter the username/IP from step 3, and the folder name from step 5
 - This script will automatically create a configuration file that allows for easy scp file transfers between the host computer and RPi3

#### 5\. Log into your Rpi3 and run the code!
 - At this point all code should be located on your RPi3 in the designated folder


# Hardware Setup

#### 1\. Required components:
 - Raspberry Pi 3
 - DE-ACCM Buffered ±5g Accelerometer
 - MCP3008 ADC converter

#### 2\. Wiring diagram
 - TODO: Create one

#### 3\. Helpful links
 - [RPi3 pin layout](https://myelectronicslab.com/raspberry-pi-3-gpio-model-b-block-pinout/)