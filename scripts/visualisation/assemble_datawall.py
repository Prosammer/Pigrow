#!/usr/bin/python
import os
import sys
from PIL import Image, ImageDraw, ImageFont
sys.path.append('/home/pi/Pigrow/scripts/')
import pigrow_defs


print("--------- Pigrow -------")
print("  --Data Wall Assembler--")
print("   -- --------------- --")

print(" -- Still in basic version, doesn't use settings files or etc --")
loc_locs = '/home/pi/Pigrow/config/dirlocs.txt'
loc_dic = pigrow_defs.load_locs(loc_locs)
graph_path = loc_dic['graph_path']
nullimg = loc_dic["path"] + "resources/null.png"
output_path = graph_path + "datawall.jpg"       #default use o= to set via command line
caps_path = loc_dic['caps_path']
#left side
g1 = graph_path + "temp_graph.png"
if not os.path.exists(g1):
    g1 = nullimg
g2 = graph_path + "sec_since_up_graph.png"
if not os.path.exists(g2):
    g2 = nullimg
g3 = graph_path + "sec_between_up_graph.png"
if not os.path.exists(g3):
    g3 = nullimg
#right side
g4 = graph_path + "humid_graph.png"
if not os.path.exists(g4):
    g4 = nullimg
g5 = graph_path + "consecutive_pi_time_graph.png"
if not os.path.exists(g5):
    g5 = nullimg
g6 = graph_path + "sec_between_comps.png"
if not os.path.exists(g6):
    g6 = nullimg

photo_width = 800
graph_width = 450

for argu in sys.argv:
    thearg = str(argu).split('=')[0]
    if  thearg == 'o':
        output_path = str(argu).split('=')[1]
    elif thearg == "g1":
            g1 = str(argu).split('=')[1]
    elif thearg == "g2":
            g2 = str(argu).split('=')[1]
    elif thearg == "g3":
            g3 = str(argu).split('=')[1]
    elif thearg == "g4":
            g4 = str(argu).split('=')[1]
    elif thearg == "g5":
            g5 = str(argu).split('=')[1]
    elif thearg == "g6":
            g6 = str(argu).split('=')[1]
    elif thearg == "caps":
            caps_path = str(argu).split('=')[1]
    elif thearg == "pw":
            photo_width = int(str(argu).split('=')[1])
    elif thearg == "gw":
            graph_width = int(str(argu).split('=')[1])

if not os.path.exists(caps_path):
    print("Unable to locate graph directory, is the path correct?")
    caps_path = "./"

filelist = []
for filefound in os.listdir(caps_path):
    if filefound.endswith("jpg"):
        filelist.append(filefound)
filelist.sort()
if len(filelist) >= 1:
    newest_photo = str(caps_path+filelist[-1])
else:
    print("no images in caps folder")
    newest_photo = nullimg

##Making The Image
newest_photo = Image.open(newest_photo)
wpercent = (photo_width/float(newest_photo.size[0]))
hsize = int((float(newest_photo.size[1])*float(wpercent)))
newest_photo = newest_photo.resize((photo_width,hsize), Image.ANTIALIAS)

g1 = Image.open(g1)
wpercent = (graph_width/float(g1.size[0]))
hsize = int((float(g1.size[1])*float(wpercent)))
g1 = g1.resize((graph_width,hsize), Image.ANTIALIAS)

g2 = Image.open(g2)
wpercent = (graph_width/float(g2.size[0]))
hsize = int((float(g2.size[1])*float(wpercent)))
g2 = g2.resize((graph_width,hsize), Image.ANTIALIAS)

g3 = Image.open(g3)
wpercent = (graph_width/float(g3.size[0]))
hsize = int((float(g3.size[1])*float(wpercent)))
g3 = g3.resize((graph_width,hsize), Image.ANTIALIAS)

g4 = Image.open(g4)
wpercent = (graph_width/float(g4.size[0]))
hsize = int((float(g4.size[1])*float(wpercent)))
g4 = g4.resize((graph_width,hsize), Image.ANTIALIAS)

g5 = Image.open(g5)
wpercent = (graph_width/float(g5.size[0]))
hsize = int((float(g5.size[1])*float(wpercent)))
g5 = g5.resize((graph_width,hsize), Image.ANTIALIAS)

g6 = Image.open(g6)
wpercent = (graph_width/float(g6.size[0]))
hsize = int((float(g6.size[1])*float(wpercent)))
g6 = g6.resize((graph_width,hsize), Image.ANTIALIAS)

threegraphs = g1.size[1] + g2.size[1] + g3.size[1]
if newest_photo.size[1] >= threegraphs:
    base = Image.new("RGBA", (graph_width+photo_width+graph_width+15, 15+newest_photo.size[1]), "white")
    base.paste(newest_photo, (graph_width+15,2))
else:
    base = Image.new("RGBA", (graph_width+photo_width+graph_width+15, 15+threegraphs), "white")
    mid = threegraphs - newest_photo.size[1]
    mid = mid / 2
    base.paste(newest_photo, (graph_width+15,mid))

#left side
base.paste(g1,(0,0))
base.paste(g2,(0,g1.size[1]+1))
base.paste(g3,(0,g2.size[1]+g2.size[1]+1))
#right side
base.paste(g4,(graph_width+photo_width+30,0))
base.paste(g5,(graph_width+photo_width+30,g4.size[1]+1))
base.paste(g6,(graph_width+photo_width+30,g4.size[1]+g5.size[1]+1))

base.save(output_path)
print("File saved to " + str(output_path))
#base.show()
