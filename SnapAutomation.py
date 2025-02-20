class SnapAutomation:
    def __init__(self, device):
        self.device = device
    
    def press(self, x, y, delay=None):
       
        x += random.randint(-5, 5)  
        y += random.randint(-5, 5)
        self.device.shell(f'input touchscreen tap {x} {y}')
        
       
        if delay is None:
            delay = random.uniform(1.2, 2.5)
        time.sleep(delay)
    
    def rapid_shots(self):
        count = 0
        open_camera = (542, 2290)
        capture_button = (535, 2050)
        proceed_button = (925, 2280)
        select_friends = (910, 1225)
        send_button = (992, 2270)

        while count < 200:  
            count += 1
            print(f"Cycle: {count}")
            self.press(*open_camera)
            self.press(*capture_button)
            self.press(*proceed_button)
            self.press(*select_friends)
            self.press(*send_button)

           
            if count % 20 == 0:
                pause = random.uniform(10, 30)
                print(f"Taking a short break for {pause:.2f} seconds...")
                time.sleep(pause)
    
    def steady_shots(self):
        snaps_sent = 0
        cam_open = (550, 1782)
        snap_button = (600, 2055)
        send_location = (2450, 2280)
        
        while snaps_sent < 500:  
            snaps_sent += 1
            print(f"Total snaps sent: {snaps_sent}")
            self.press(*cam_open)
            self.press(*snap_button)
            self.press(*send_location)

            
            if snaps_sent % 25 == 0:
                pause = random.uniform(15, 45)
                print(f"Taking a break for {pause:.2f} seconds...")
                time.sleep(pause)

if __name__ == "__main__":
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    
    if not devices:
        print("No devices attached")
        sys.exit(1)
    
    device = devices[0]
    snap = SnapAutomation(device)
    
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode == 'rapid':
            snap.rapid_shots()
        elif mode == 'steady':
            snap.steady_shots()
        else:
            print("Invalid argument! Use 'rapid' for fast snaps or 'steady' for normal snaps.")
    else:
        print("No argument provided! Use 'rapid' or 'steady'.")