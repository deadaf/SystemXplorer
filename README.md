# SystemXplorer

SystemXplorer is a comprehensive system information summary tool developed as a part of the OS Lab project. It provides a user-friendly interface to gather essential information about the system, including details about the operating system, CPU, disk, memory, network, processes, and battery (if applicable).

https://github.com/deadaf/SystemXplorer/assets/72350242/fd93c3a4-68db-466b-9f60-3dc484b0b4a3

## Features

- **OS Info**: Display detailed information about the operating system.
- **CPU Info**: Provide insights into CPU details, usage, and core information.
- **Disk Info**: Show information about the storage devices and their usage.
- **Memory Info**: Display information about RAM and swap memory.
- **Network Info**: Present details about network interfaces and usage statistics.
- **Processes Info**: List running processes with essential details.
- **Battery Info**: If running on a laptop or battery-powered device, display battery information such as charge level, remaining time, status, and health.
  
![diagram (4)](https://github.com/deadaf/SystemXplorer/assets/72350242/d8b85ac8-76bd-4e68-b0ca-920892e3aef3)

## Getting Started

### Prerequisites

```
- Python 3.11
- Tkinter
- psutil
- poetry
```

### Installation

> **Note**: The following instructions are for Linux-based systems. (_Tested on Ubuntu 23.04_)

1. Clone the repository:

   ```bash
   git clone https://github.com/deadaf/SystemXplorer.git
   ```

2. Change the working directory:

   ```bash
   cd SystemXplorer
   ```

3. Install the dependencies:

   ```bash
    poetry install
   ```

4. Activate the virtual environment:

   ```bash
   poetry shell
   ```

5. Run the application:

   ```bash
   python3 main.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
