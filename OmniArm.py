class ARM:
    def __init__(self, ADC_pose, ADC_temp):
        self.pose = ADC_pose
        self.temp = ADC_pose
        self.calirate = False

    def GetPose(): # TODO
        if not calibrate:
            print("Arm is not calibrated. Set the limits")
            return None
        Print("Add the FK fucntion")
        return 0
    
    def SetLimits(hipMax,hipMin, hightMax,hightMin, LateralMax, LateralMin, WristMax, WristMin):
        self.hipMax = hipMax
        self.hipMin = hipMin
        self.hightMax = hightMax
        self.hightMin = hightMin
        self.LateralMax = LateralMax
        self.LateralMin = LateralMin
        self.WristMax = WristMax
        self.WristMin = WristMin
        self.calibrate = True
    
    def GetTemp(): #TODO
        return 0
