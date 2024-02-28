from plyer import notification
import time

if __name__ == '__main__':
    while True:
          notification.notify(
                title="*** DRINK WATER ***",
                message="Water helps your body:Keep a normal temperature.Lubricate and cushion joints.Protect your spinal cord and other sensitive tissues.Get rid of wastes through urination, perspiration, and bowel movements.",
                #app_icon="E:\pythoncodes\.venv\download.png\download",
                timeout=10)
          time.sleep(3600)
