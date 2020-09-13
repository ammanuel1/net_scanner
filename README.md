# net_scanner
Simple python script that sends packets to IP addresses on a local network. Devices that are connected on the local network will return connectivity.

To Run application:

1.) Download folder, cd into directory containing net_scan Run using ./run.sh 
      - if unable to run using above command...
          - enter the command $ chmod +x run.sh into terminal while in the same directory
          - then the command ./run.sh should prompt the program to begin

 2.) Once open
      - the program will prompt the user for an IP address to use for testing the other IP's on the same local network
      - Will return a list of the working IP's that responded to the transmission of packets
