import DobotAPI as api
import time

def main():
    dType = api.dType

    # Connect to Dobot on COM3 (adjust if needed)
    state = dType.ConnectDobot("COM3", 115200)[0]
    if state != dType.DobotConnect.DobotConnect_NoError:
        print("Failed to connect:", state)
        return

    print("Connected to Dobot!")

    # Clear command queue
    dType.SetQueuedCmdClear(api.api)

    # Enable robot
    dType.SetQueuedCmdStartExec(api.api)

    # Move to position
    dType.SetPTPCmd(api.api, dType.PTPMode.PTPMOVLXYZMode, 200, 0, 50, 0)

    time.sleep(2)

    # Disconnect
    dType.DisconnectDobot(api.api)

if __name__ == "__main__":
    main()