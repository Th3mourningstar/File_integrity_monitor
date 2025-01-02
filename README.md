# File_integrity_monitor
A python script to monitors the integrity of files/systems 

Features:
Hash-Based Integrity Check: Uses SHA-256 to compute file hashes.
Baseline Creation: Builds a JSON file storing hashes of monitored files.
Change Detection: Identifies new, modified, or deleted files.
Directory Monitoring: Recursively scans files in the specified directory.
Command-Line Options:
build: Create a baseline of current file hashes.
monitor: Compare current file hashes to the baseline and report changes.
Usage:
Save the script as file_integrity_monitor.py.
Install required packages (if any).
Run to build a baseline:
bash
Copy code
python file_integrity_monitor.py build
Run to monitor changes:
bash
Copy code
python file_integrity_monitor.py monitor
Customize:
Update MONITORED_DIR to set the directory to monitor.
Extend the script to send alerts (e.g., via email) for detected changes.
