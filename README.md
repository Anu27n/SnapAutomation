SnapAutomation 🎨🚀

SnapAutomation is an ADB-based automation script that helps in sending snaps automatically using Python and ADB (Android Debug Bridge). This tool is for educational purposes only—use responsibly!

⚠️ Disclaimer

This script automates Snapchat interactions. Use at your own risk! Snapchat may detect automated behavior and take action against your account. To reduce detection chances, random delays and position variations have been added.

🛠 Requirements

Before running this script, ensure you have the following installed:

Python 3.x (Recommended: 3.7 or later)

ADB (Android Debug Bridge) installed and added to system PATH

An Android device with:

Developer mode enabled

USB debugging enabled

Connected via USB or Wireless ADB

📌 Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/SnapAutomation.git
cd SnapAutomation

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Verify ADB Connection

adb devices

If your device appears in the list, you're good to go! If not, check that USB debugging is enabled and try again.

🚀 Usage

1️⃣ Connect Your Device

Ensure your phone is connected via USB or Wireless ADB and run:

adb devices

If prompted, allow USB debugging on your phone.

2️⃣ Run the Script

You can use either Exponential Mode or Regular Mode:

✅ Exponential Mode (Faster, Riskier)

python snapautomation.py exp

This mode takes snaps and sends them at a faster rate. Use cautiously.

✅ Regular Mode (Slower, Safer)

python snapautomation.py reg

This mode takes and sends snaps with delays to mimic human behavior.

⚡ Features

✔ Randomized delays to avoid detection✔ Human-like tapping behavior with slight position variation✔ Two modes: Regular (Safe) & Exponential (Fast)✔ Auto-sending snaps to friends/groups✔ Configurable snapping limits

📝 Configuration

You can modify the script variables for different snapping behaviors:

main_cam_cords = (542, 2290)  # Main camera button
cam_click_img_cord = (535, 2050)  # Capture button
next_cord = (925, 2280)  # Next button
friends_grp_cord = (910, 1225)  # Select friends/group
send_grp_cord = (992, 2270)  # Send button

To change the number of snaps sent:

while count < 200:  # Modify this value

❗ Important Notes

Running this script excessively may get your Snapchat account flagged or banned.

It is recommended to use the "reg" mode for safer automation.

Avoid sending too many snaps too quickly. Take breaks in between.

🛠 Troubleshooting

Issue: No devices attached✅ Solution: Ensure USB debugging is enabled on your phone and re-run:

adb devices

Issue: ADB command not found✅ Solution: Ensure ADB is installed and added to your system PATH.

Issue: Script stops unexpectedly✅ Solution: Restart your phone, reconnect ADB, and run the script again.

👨‍💻 Contributing

Pull requests are welcome! If you find any issues or have suggestions, feel free to open an issue in the repository.

🐟 License

This project is licensed under the MIT License.

📩 Contact

For any queries, feel free to reach out via GitHub issues.
