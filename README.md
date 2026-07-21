Real-Time Parallel Log Aggregation Engine with Custom Socket Slicing

 Overview
This project is a Python-based log aggregation system that collects real-time logs from multiple servers using socket programming. Logs are categorized into **INFO**, **WARNING**, **ERROR**, and **DEBUG** levels and stored in separate binary files for efficient management.

 Features
- Real-time log collection
- Socket-based communication
- Binary log storage (.bin)
- Log classification
- Multiple city log simulation (Mumbai, Chennai, Bangalore)
- Binary log reader

 Technologies Used
- Python 3
- Socket Programming
- Binary File Handling
- VS Code

 Project Structure

RealTimeLogEngine/
│── read_binary.py
│── log_server_simulator.py
│── log_harvester_daemon.py
│── README.md
│── requirements.txt
│── *.bin log files


 How to Run

1. Start the log harvester:
bash
python log_harvester_daemon.py


2. Run the log server simulator:
bash
python log_server_simulator.py


3. Read the binary log files:
bash
python read_binary.py

 Output
The system receives logs, classifies them into INFO, WARNING, ERROR, and DEBUG categories, stores them in binary files, and displays them using the binary reader.

 Future Enhancements
- Multi-threaded log processing
- Database integration
- Web dashboard
- Cloud log storage
- AI-based log analysis


 Author
A. Dhivya Dharshni  
Bachelor of Computer Applications (BCA)
