from robots.controller import DobotControl

class DobotCOM3(DobotControl):
    def user_init(self):
        self.home_pose = (200, 0, 50, 0)
        self.reset_zero(self.home_pose)

        # Define motion profiles
        self.fast_speed = (100, 100)   # velocity, acceleration
        self.slow_speed = (30, 30)
        self.retreat_speed = (50, 50)

    def set_motion_profile(self, vel, acc):
        self.dobot.SetPTPCommonParams(vel, acc, isQueued=1)

    def work(self):
        print("Starting palletizing test on", self.addr)

        test_heights = [50, 80, 110]
        for z in test_heights:
            print(f"→ Moving to Z={z}")

            # Fast travel to above target
            self.set_motion_profile(*self.fast_speed)
            self.moveTo(x=200, y=0, z=z + 30, r=0)

            # Slow approach
            self.set_motion_profile(*self.slow_speed)
            self.moveInc(dz=-30)

            # Pick/place
            self.suck()
            self.set_motion_profile(*self.retreat_speed)
            self.moveInc(dz=20)
            self.unsuck()

            # Return home fast
            self.set_motion_profile(*self.fast_speed)
            self.moveTo(*self.home_pose)

        print("Palletizing test complete on", self.addr)

if __name__ == "__main__":
    bot = DobotCOM3()
    bot.setAddr("COM3")
    bot.start()
    bot.join()