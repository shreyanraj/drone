### 📄 **README: Hand Gesture Controlled CoDrone EDU**

---

### ✅ **Project Overview**
This project uses **MediaPipe Hand Tracking** and **CoDrone EDU** to control a drone with hand gestures. The program captures video from your webcam, detects your hand, counts the number of extended fingers, and sends corresponding flight commands to the drone. 

---

### 🚀 **Features**
- **Hand Tracking:** Uses MediaPipe to detect and track hand landmarks in real-time.
- **Gesture-Based Drone Control:**
    - ✋ **5 fingers:** Takeoff  
    - ✊ **0 fingers:** Land  
    - ✌️ **2 fingers:** Move Right  
    - 🤟 **3 fingers:** Move Left  
    - ✋✋ **Any other gesture:** Hover  
- **Multi-threading:** Drone commands run in separate threads, preventing camera feed lag.  
- **Smooth Frame Display:** Flipped frame orientation for natural gesture control.  
- **Real-time Visualization:** Displays the current command on the video feed.  

---

### 🛠️ **Hardware and Software Requirements**
#### **Hardware:**
- **CoDrone EDU**  
- **Computer with webcam**  
- **Bluetooth connection** (for pairing the drone)  

#### **Software:**
- **Python 3.7+**
- **MediaPipe** (`pip install mediapipe`)  
- **OpenCV** (`pip install opencv-python`)  
- **CoDrone EDU SDK** (`pip install codrone-edu`)  

---

### 🔥 **Installation Instructions**

1. **Clone the Repository (Optional)**:
   ```bash
   git clone <repository_url>
   cd hand-gesture-drone
   ```

2. **Install Dependencies:**
   Make sure you have Python 3 and `pip` installed. Then, install the required libraries:
   ```bash
   pip install codrone-edu opencv-python mediapipe
   ```

3. **Pair the Drone:**
   - Turn on the **CoDrone EDU** and pair it with your system.
   - The program automatically pairs using the `drone.pair()` function.

4. **Run the Program:**
   ```bash
   python gesture_drone.py
   ```

---

### ✋ **How to Use**
1. **Start the program** – The webcam will open and display your video feed.
2. **Control the drone with hand gestures:**
   - **5 fingers** → Drone takes off.  
   - **0 fingers** → Drone lands.  
   - **2 fingers** → Moves the drone **right**.  
   - **3 fingers** → Moves the drone **left**.  
   - **Any other gesture** → Hovers the drone.  
3. **Press `q`** to quit the program and land the drone.

---

### ⚙️ **Code Explanation**
1. **Hand Detection:**  
   - MediaPipe detects hands and landmarks.  
   - The program counts the number of extended fingers by checking if the tip of each finger is above the second joint.

2. **Multi-threaded Commands:**  
   - Drone commands execute in a **separate thread** to avoid frame processing delays.

3. **Camera Feed:**  
   - Flipped horizontally for a natural orientation.  
   - Displays the current command on the video feed.

---

### 🛠️ **Customization Options**
- **Drone Speed:**  
   You can modify the drone's speed by changing the roll values:  
   ```python
   drone.set_roll(20)  # Faster  
   drone.set_roll(10)  # Slower  
   ```

- **Additional Gestures:**  
   Add more gestures by checking specific hand landmark positions and assigning new commands.  
   Example:
   ```python
   elif num_fingers == 4:
       command = "MOVE FORWARD"
       drone.set_pitch(15) 
       drone.move(1)
   ```

---

### 🛡️ **Safety Tips**
- Always fly the drone in an **open area** with no obstacles.  
- Keep a **safe distance** from the drone.  
- If the drone behaves unexpectedly, press `q` to safely land and stop the program.  

---

### 🔥 **Troubleshooting**
- **Lag or Frame Delay:**  
   If you experience lag, lower the camera resolution:  
   ```python
   cap.set(3, 480)  # Width  
   cap.set(4, 360)  # Height  
   ```

- **Drone Not Responding:**  
   - Ensure the drone is paired properly.  
   - Restart the drone and reconnect.  
   - Check Bluetooth connection stability.  

---

### 📚 **Future Improvements**
- Add **more gestures** (e.g., move forward/backward, rotate).
- Use **voice commands** alongside gestures.
- Optimize gesture recognition with **machine learning models**.

---

### ✅ **Author**
**Project by:** Shreyan Lankapalli  
**Date:** March 2025  
**Language:** Python 3  
**Libraries:** OpenCV, MediaPipe, CoDrone EDU SDK  

---

🎯 **Enjoy flying your CoDrone with hand gestures!** 🚀
