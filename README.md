# VoiceOverSocket
An attempt to implement Walky-Talky like system as a mini project in the subject 'Computer-Networks'

To run the project:
1. Run phone_server.py on first computer
2. Run phone_client.py on second computer
3. Inside both the programs IP_ADDRESS variable will have to be set to the current ip address of the machine.
4. The PORT_NUMBER must be same for both the programs.

Note: The computers must be connected on the same network and should be able to perfrom a simple ping to eachother (Firewall might have to be relaxed).

The Programs running on different machines will automatically connect. To speak press Space Bar and talk. Once the space bar is lifted the recorded audio will be sent to the receving end. This can be done on both the client and server computers. Hence, making both the computers connect like a walky-talky.
