class TV :
    def __init__(self,power,channel,volume):
        self.power = power
        self.channel = channel
        self.volume = volume
    def intro(self):
        print("Power :",self.power)
        print("Channel :",self.channel)
        print("Volume :",self.volume)
    def trun_off(self):
        print("Trun off")
    def trun_on(self):
        print("Trun on")
    def set_channel(self,v):
        self.channel = v
    def set_volume(self,v):
        self.volume = v        

lugo = TV("True","0","0")
lugo.set_channel("1")
lugo.set_volume("16")
lugo.intro()
lugo.trun_off()
lugo.trun_on()
