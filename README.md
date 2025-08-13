# HandyVolume 🎛️🖐️

HandyVolume is a **real-time hand gesture-based volume controller** built with **OpenCV**, **MediaPipe**, and **PyCaw**.  
By simply moving your **thumb** and **index finger** closer or farther apart, you can adjust your system's volume instantly.  
When the distance between your fingers exceeds a set threshold, HandyVolume automatically boosts your volume to 100%.

---

## 📌 Features
- **Gesture-Based Volume Control** – Move your fingers to control system volume without touching the keyboard.
- **Max Volume Trigger** – Automatically sets volume to maximum when the gesture distance exceeds `120px`.
- **Real-Time Hand Tracking** – Uses **MediaPipe Hands** for fast and accurate detection.
- **Smooth Performance** – Runs at ~30 FPS for a seamless experience.

---

## 🎥 How It Works (Demonstration)
1. **Start the program**  
   The webcam opens and begins detecting your hand in real time.

2. **Show your hand to the camera**  
   Make sure your **thumb** and **index finger** are clearly visible.

3. **Adjust volume by changing distance**  
   - Move your **thumb** and **index finger** **closer** → Volume decreases.  
   - Move them **farther apart** → Volume increases.  

4. **Max Volume Mode**  
   If the distance between your thumb and index finger exceeds `120px` (on-screen measurement),  
   the system volume is instantly set to **100%**.

5. **Quit the program**  
   Press the **`q`** key at any time to exit.

---

## 📂 Project Structure
