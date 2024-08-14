# Data Science & Communication 2024 Group 2

**Topic:** Electricity Monitoring and Coordination  
**Repo:** [https://github.com/G36maid/electricity_monitor](https://github.com/G36maid/electricity_monitor)

---

## Team Members

| Name                | English Name            | University | Major                     | Year |
|---------------------|-------------------------|------------|---------------------------|------|
| 羅願群               | Jethro                  | NTNU       | Computer Science          | 1    |
| 鍾詠傑               | Jie Chung               |            | Mechatronic Engineering   | 2    |
| 名嘉山 栞            | Shiori Nakayama         | KU         | ISI                       | 4    |
| ローイ ベンジャミン   | Benjamin Joshua Lowy    |  KU          | ISI                       | 2    |

---

## Project Ideas

- **Monitor power consumption and power generation:**
  - Use data from monitored power → map power consumption → Serve power during emergencies or during vulnerable, high usage times.
  - Power usage on personal devices (app) ← connected to a smart meter.
  - Use algorithms like max flow to visualize the electrical load in each city.
  - Combine with weather data to predict how electricity use varies with weather and season.

## usage

This project includes a Linux-based electricity monitoring system using MQTT to send and receive data. It consists of two main components:

1. **Linux Client**: Monitors power consumption and sends data to the server.
2. **Server**: Receives data from clients and logs it into a CSV file.

## Prerequisites

- **Python 3**: Ensure Python 3 is installed.
- **MQTT Broker**: An MQTT broker must be running and accessible. (e.g., `140.122.185.98` on port `1883`)
- **Dependencies**: Install the necessary Python library and tools:
  - `paho-mqtt`
  - `powerstat` (for Linux clients)

## Installation

### For Linux Client

1. **Install Python Dependencies**:
   ```bash
   pip install paho-mqtt
   ```

2. **Install `powerstat`**:
   ```bash
   sudo apt-get install powerstat
   ```

3. **Client Configuration**:
   - The client script will prompt for `Latitude`, `Longitude`, `Building ID`, and `Category`.
   - Make sure to modify the MQTT credentials and broker address as needed.

### For Server

1. **Install Python Dependencies**:
   ```bash
   pip install paho-mqtt
   ```

2. **Server Configuration**:
   - The server script listens for incoming data and logs it into `data/electricity_consumption.csv`.
   - Ensure the server script connects to the correct MQTT broker and topic.

## Running the System

### Start the Server

1. Open a terminal and navigate to the directory with the server script.
2. Run the server script:
   ```bash
   python server.py
   ```

### Start the Client

1. Open a terminal and navigate to the directory with the client script.
2. Run the client script:
   ```bash
   python linux_client.py
   ```
3. Enter the required information when prompted.

## Notes

- Make sure the MQTT broker is accessible and properly configured.
- Adjust the MQTT broker details and credentials in the scripts as needed.
- The `powerstat` tool is Linux-specific; alternative methods are needed for macOS or Windows.

---

This `README.md` provides a clear overview of setting up and running your electricity monitoring system without including the actual code.

### Potential Data Sources

- **Taiwan Power Open Data:**
  - Electricity consumption data.
  - Electricity supply data.
- **Additional Datasets:**
  - [Residential Power Usage 3 Years Data - Timeseries](https://www.kaggle.com/datasets/srinuti/residential-power-usage-3years-data-timeseries)
  - [Indian Cities Electricity Consumption 2017-19]{link}
  - [Energy Consumption of the Netherlands]{link}

---

### Team Skills and Specializations

- **Jie Chung:**
  - Network and system administrator.
  - Docker and Kubernetes deployment.
  - C, C++, Rust (not strong in Python).
- **Jethro:**
  - Data preprocessing, familiar with multiple programming languages.
- **Shiori:**
  - Data science (visualization), Python.

### Summary of Group Chat Day 4
  1. **Project Focus:**
   - The group agreed to focus on **electricity monitoring and coordination**.
   - The concept involves using power consumption and generation data to create visualizations that can aid in managing electricity, especially during emergencies or high usage times.

2. **Data Strategy:**
   - The group decided to **simulate fake data** for the project.
   - This data will be used for visualizing power consumption and generation on a smaller scale (e.g., a building or district) rather than an entire city, due to the complexity of generating realistic large-scale data.

3. **Visualization Tools:**
   - **Grafana** and **QGIS** were discussed as potential tools for visualization.
   - **QGIS** was favored, and the group will explore using it, particularly with data that includes geographic coordinates (longitude and latitude) and time series.

4. **Technical Considerations:**
   - Data will need to include specific power units (GW, MW, kW, W) and possibly be aligned with weather data to predict usage patterns.
   - The group acknowledged the challenge of managing large datasets, especially when simulating data for numerous buildings.

5. **GitHub Repository Setup:**
   - A GitHub repository was set up for the project: [https://github.com/G36maid/electricity_monitor](https://github.com/G36maid/electricity_monitor).
   - All group members shared their GitHub accounts and agreed to use Git for code management and collaboration.

#### Next Steps:

- **Data Preparation:** The group will focus on generating or collecting suitable data, preparing it for use in visualizations, and ensuring it can be integrated into QGIS.
- **Coding and Visualization:** Python code will be written to prepare for the demo, and the group will work on integrating the data into QGIS for visualization.
- **Collaboration:** The team will continue using GitHub for collaboration and code management.

**Time Remaining:**
- Approximately 20 minutes were left for the immediate tasks at the time of this discussion.