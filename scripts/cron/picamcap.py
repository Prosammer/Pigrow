#!/usr/bin/python
import time
import os, sys
sys.path.append('/home/pi/Pigrow/scripts/')
script = 'picamcap.py'
import pigrow_defs
try:
    from picamera import PiCamera
except:
    print("Picamera is not installed, is this even a raspberry pi?!")
    exit()
loc_locs = '/home/pi/Pigrow/config/dirlocs.txt'
loc_dic = pigrow_defs.load_locs(loc_locs)
caps_path = loc_dic["caps_path"]
picam_dic = {}
with open("/home/pi/Pigrow/config/picam_settings.txt", "r") as f:
    for line in f:
        s_item = line.split("=")
        picam_dic[s_item[0]]=s_item[1].rstrip('\n')
print picam_dic

# take and save photo
timenow = str(time.time())[0:10]
filename= "cap_"+str(timenow)+".jpg"
try:
    camera = PiCamera()
    #camera.resolution = (2592,1944)
    camera.brightness = int(picam_dic['b_val'])
    camera.contrast = int(picam_dic['c_val'])
    camera.resolution = (int(picam_dic['x_dim']),int(picam_dic['y_dim']))
    #camera.shutter_speed =
    camera.iso = 800
    time.sleep(2)
    print ("resolution = " + str(camera.resolution))
    print ("analog_gain = " + str(camera.analog_gain))
    print ("digital_gain = " + str(camera.digital_gain))
    print ("iso =" + str(camera.iso))
    print ("brightness = " + str(camera.brightness))
    print ("contrast =  " + str(camera.contrast))
    print ("saturation = " + str(camera.saturation))
    print ("sharpness = " + str(camera.sharpness))
    print ("zoom = " + str(camera.zoom))
    print ("drc_strength = " + str(camera.drc_strength))
    print ("exposure_compensation = " + str(camera.exposure_compensation))
    print ("exposure_mode = " + str(camera.exposure_mode))
    print ("exposure_speed = " + str(camera.exposure_speed))
    print ("hflip = " + str(camera.hflip))
    print ("vflip = " + str(camera.vflip))
    print ("rotation = " + str(camera.rotation))
    print ("meter_mode = " + str(camera.meter_mode))
    print ("image_denoise = " + str(camera.image_denoise))
    print ("image_effect = " + str(camera.image_effect))
    print ("image_effect_params = " + str(camera.image_effect_params))
    print ("awb_mode = " + str(camera.awb_mode))

    camera.capture(caps_path+filename)
    camera.close()
#os.system("raspistill -o "+path+filename+" "+extra_commands)
    print("Image taken and saved to "+caps_path+filename)
except:
    print("Sorry, picture not taken :(")
    raise
