# SnapAutomation

SnapAutomation is an ADB-powered automation script that enhances your Snapchat experience by automating snap sending. This project leverages Python and ADB to interact with your device and perform actions programmatically.

## ⚠ Disclaimer
This project is intended for educational purposes only. Misuse of this script may violate Snapchat's terms of service and result in account restrictions or bans. Use it responsibly at your own risk.However we have added some tweeks which snapchat may not notice.

## 📌 Features
- Automated snap sending
- Randomized tap locations to simulate human behavior
- Configurable delays to avoid detection
- Two modes: `exp` (exponential) and `reg` (regular)
- Break intervals to mimic natural usage patterns

## 🚀 Installation

### 1️⃣ Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- ADB (Android Debug Bridge)
- An Android device with Developer Mode and USB Debugging enabled

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/Anu27n/SnapAutomation.git
cd SnapAutomation
```

### 3️⃣ Install Dependencies
```bash
pip install pure-python-adb
```

### 4️⃣ Enable ADB Debugging
1. Connect your phone via USB.
2. Run the following command to check if the device is detected:
   ```bash
   adb devices
   ```
3. If your device appears in the list, proceed to the next step.

## 🛠 Usage

### 1️⃣ Start the ADB Server
```bash
adb start-server
```

### 2️⃣ Run the Script
You can run the script in either `exp` (exponential snaps) or `reg` (regular snaps) mode.

#### 🔹 Exponential Snap Mode
```bash
python snapscore.py exp
```
This mode sends a batch of snaps and gradually increases the pace.

#### 🔹 Regular Snap Mode
```bash
python snapscore.py reg
```
This mode sends snaps at a consistent pace with randomized intervals.

## 📌 Configuration
You can adjust the following values in `snapscore.py`:
- `main_cam_cords`: Coordinates for opening the camera.
- `cam_click_img_cord`: Coordinates for clicking a snap.
- `next_cord`: Coordinates for proceeding to the next screen.
- `friends_grp_cord`: Coordinates for selecting friends.
- `send_grp_cord`: Coordinates for sending snaps.
- `snap_limit`: Adjust the number of snaps sent per session.
- `random.uniform(min, max)`: Modify random sleep intervals for human-like behavior.

## ⚠ Precautions
- Avoid sending excessive snaps in a short period.
- Use randomized delays to minimize the risk of detection.
- Do not rely solely on automation; engage in normal activity on your account.

## 🛠 Troubleshooting
### 🔹 ADB Command Not Found
If you encounter an error like:
```
adb: command not found
```
Try adding ADB to your system's PATH variable or navigate to the ADB directory before running commands.

### 🔹 Device Not Found
Ensure:
- Your phone is connected properly.
- USB Debugging is enabled in Developer Options.
- You have authorized your PC for debugging.


⚡ **Use responsibly and have fun automating!** 🚀
