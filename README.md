
# VulnScanner Pro

VulnScanner Pro is an advanced vulnerability scanner built using Python. It allows users to perform network scans and CVE vulnerability lookups using the NVD API. It features a professional dark-themed GUI built with Tkinter.

## Features

- Advanced dark-themed GUI
- Scans local subnet for open port 80
- Real-time CVE search using NVD API
- Displays CVE ID, description, and solutions
- Built with modular and clean code structure

## Getting Started

### Prerequisites

- Python 3.x
- Required packages: `requests`, `tkinter` (usually included in standard Python installations)

### Running the App

1. Clone the repository or download the ZIP.
2. Navigate to the folder and run:

```bash
python run_pro.py
```

3. Enter subnet (e.g., `192.168.29`) and keyword (e.g., `Apache`) to begin.

## File Structure

```
VulnScanner-Pro-GitHub/
│
├── core/
│   ├── scanner_pro.py     # Scanning and CVE search logic
│   └── gui.py             # GUI implementation
│
├── run_pro.py             # Entry point to start GUI
├── LICENSE
└── README.md
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
