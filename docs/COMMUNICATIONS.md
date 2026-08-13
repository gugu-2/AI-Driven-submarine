# Communications & Live Video Feeds

Transmitting live footage from underwater to Headquarters is one of the hardest physics problems in marine robotics. **Wi-Fi, Bluetooth, and standard Radio Waves (RF) are completely absorbed by water within inches.** 

If you want live video at HQ, you must select one of the following specialized equipment architectures:

## 1. The Tethered Wi-Fi Buoy (Most Reliable, Cheapest)
**How it works:** The submarine carries a spool of micro-thin fiber-optic cable attached to a small floating buoy. When HQ requests live video, the sub releases the buoy, which floats to the surface.
*   **Equipment:** Spooling mechanism, Fiber-optic tether, Surface Buoy with Wi-Fi/4G/Satellite antenna.
*   **Pros:** HQ gets crisp, 1080p 60FPS live video from anywhere on Earth via Satellite.
*   **Cons:** The tether can get snagged on rocks or kelp.

## 2. Blue-Light Optical Modems (Advanced, Expensive)
**How it works:** Uses high-powered Blue/Green lasers flashing millions of times a second to transmit data through the water.
*   **Equipment:** Optical Modem (e.g., Hydromea LUMA or Sonardyne BlueComm). 
*   **Pros:** Completely wireless live video underwater. Extremely stealthy.
*   **Cons:** Max range is ~100 to 150 meters. It requires a relay ship or another drone to be directly above the submarine to catch the laser light and forward it to HQ via satellite. Does not work in muddy/murky water.

## 3. Acoustic Modems (The Fallback / Stealth Mode)
**How it works:** Translates digital data into sound waves (like an old dial-up modem) and broadcasts it through the water.
*   **Equipment:** Acoustic Transceiver (e.g., Woods Hole Micromodem, Evologics).
*   **Pros:** Works over miles/kilometers. Does not require a tether.
*   **Cons:** Incredibly low bandwidth (measured in bits per second). **You cannot stream live video over acoustics.** You can only send small text files (e.g., `["x": 500, "status": "OK"]`) or an extremely compressed, grainy photo at a rate of 1 frame every few minutes.

## Implementation in this Codebase
Our `comms_uplink.py` module utilizes a hybrid approach:
1. **Underwater:** It relies on **Acoustics** for silent, low-bandwidth text updates.
2. **Surfaced:** It relies on **Satellite RF** for high-bandwidth data dumps (like error logs and video uploads) only when the sub breaks the surface.
