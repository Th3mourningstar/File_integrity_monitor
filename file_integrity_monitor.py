import hashlib
import os
import json
import time

# File to store baseline hashes
BASELINE_FILE = "file_baseline.json"

# Directory to monitor
MONITORED_DIR = "./monitored_files"

# Function to compute file hash
def compute_hash(file_path):
    hash_func = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"Error computing hash for {file_path}: {e}")
        return None

# Function to build a baseline of file hashes
def build_baseline():
    file_hashes = {}
    for root, _, files in os.walk(MONITORED_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = compute_hash(file_path)
            if file_hash:
                file_hashes[file_path] = file_hash
    with open(BASELINE_FILE, "w") as f:
        json.dump(file_hashes, f, indent=4)
    print("Baseline built successfully.")

# Function to monitor files for changes
def monitor_files():
    try:
        with open(BASELINE_FILE, "r") as f:
            baseline_hashes = json.load(f)
    except FileNotFoundError:
        print("Baseline file not found. Run the script with 'build' option to create one.")
        return

    current_hashes = {}
    for root, _, files in os.walk(MONITORED_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            current_hash = compute_hash(file_path)
            if current_hash:
                current_hashes[file_path] = current_hash

    for file_path, baseline_hash in baseline_hashes.items():
        if file_path not in current_hashes:
            print(f"File deleted: {file_path}")
        elif current_hashes[file_path] != baseline_hash:
            print(f"File modified: {file_path}")

    for file_path in current_hashes.keys():
        if file_path not in baseline_hashes:
            print(f"New file detected: {file_path}")

# Main function to handle user input
def main():
    import argparse

    parser = argparse.ArgumentParser(description="File Integrity Monitor")
    parser.add_argument("action", choices=["build", "monitor"], help="Action to perform: build baseline or monitor changes.")
    args = parser.parse_args()

    if args.action == "build":
        build_baseline()
    elif args.action == "monitor":
        monitor_files()

if __name__ == "__main__":
    main()
