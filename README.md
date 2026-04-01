🌍 Project Title
Smart Air Quality Monitoring System using Arduino, Python & MySQL


📌 Introduction

Air pollution is a serious environmental issue affecting health and safety.
This project develops a real-time air quality monitoring system that collects environmental data and stores it for analysis.

The system provides both live monitoring and data storage capabilities.

🎯 Objectives
Monitor air quality in real-time
Measure CO, temperature, and humidity
Display data on a live dashboard
Store data in a database
Provide alerts for unsafe conditions
Enable data analysis and download


🧰 Components Used

🔌 Hardware:
Arduino (Uno/Nano)
MQ135 (Air Quality Sensor)
MQ7 (CO Sensor)
DHT11 (Temperature & Humidity Sensor)

💻 Software:
Arduino IDE
Python
Streamlit
MySQL


⚙️ Working Principle
Sensors collect environmental data
Arduino processes sensor values
Data is sent to laptop via serial communication
Python reads and processes data
Data is:
Displayed on dashboard
Stored in MySQL database
User can monitor and download data


🔄 System Architecture
Sensors → Arduino → Serial Communication → Python → Streamlit Dashboard
                                                    ↓
                                                  MySQL Database


📊 Features
📡 Real-time monitoring
📈 Live graphs
🚨 Alert system
📋 Data table with timestamps
📥 CSV download
🗄️ Database storage (MySQL)
🔄 Auto-refresh dashboard


🗄️ Database Design
Table: sensor_data

Field	Type
id	INT (Primary Key)
time	DATETIME
air	INT
co	INT
temp	FLOAT
humidity	FLOAT


🚨 Alert System
Air Quality:
Good
Moderate
Dangerous
CO Level:
Warning if high


🖥️ Dashboard Output
Air Quality Index
CO Level
Temperature
Humidity
Real-time graphs
Status indicator
Historical data table


👍 Advantages
Real-time + historical monitoring
Data stored permanently
Easy visualization
Low cost system
Scalable for IoT applications


⚠️ Limitations
Requires continuous power
Sensor accuracy limitations
Local database (not cloud yet)


🚀 Future Scope
Cloud database integration
Mobile app access
AI-based prediction
Remote monitoring
Smart alert notifications


🎯 Conclusion

This project successfully implements a real-time air quality monitoring system with database storage.

It combines hardware and software to create a smart IoT solution capable of monitoring and analyzing environmental conditions