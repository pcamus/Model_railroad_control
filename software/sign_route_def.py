# File sign_route_def.py
# Definition of the mcp circuits interfaces, signals and routes.
# 
# MCP23017 : https://github.com/mcauser/micropython-mcp23017
# info@pcamus.be
# 26/01/24

from machine import Pin, I2C,
import mcp23017

i2c = I2C(0,scl=Pin(9), sda=Pin(8))
mcp0 = mcp23017.MCP23017(i2c, 0x20) # all ports of mcp0 are input with pull-up
# mcp[0] = track 1, mcp[1] = track 2... mcp[13] = track 14    = 0 means track is occupied
# mcp[14] = route cancelation push button
for i in range(0,15):
    mcp0[i].input(pull=1)

# all ports of following circuits are output to drive signals leds
mcp1 = mcp23017.MCP23017(i2c, 0x21)
mcp2 = mcp23017.MCP23017(i2c, 0x22)
mcp3 = mcp23017.MCP23017(i2c, 0x23)

# dictionnaries definition
# Signals definition: port assignment and led pins
signals_def={}
signals_def["C5"]=[mcp1, {"R":0, "V":1, "Jh":2, "Jv":3, "Bl":4, "Vl":5}]
signals_def["M5"]=[mcp1, {"R":6, "J":7}]
signals_def["D5"]=[mcp1, {"R":8, "V":9, "Bl":10}]
signals_def["H5"]=[mcp1, {"R":11, "V":12, "Bl":13}]
signals_def["N5"]=[mcp1, {"R":14, "J":15}]

signals_def["J5"]=[mcp2, {"R":0, "V":1, "Jh":2, "Jv":3, "Bl":4, "Vl":5}]
signals_def["K5"]=[mcp2, {"R":6, "J":7}]
signals_def["F5"]=[mcp2, {"R":8, "V":9, "Jh":10, "Jv":11, "Bl":12}]
signals_def["L5"]=[mcp2, {"R":13, "V":14, "Bl":15}]

signals_def["E5"]=[mcp3, {"R":0, "V":1, "Bl":2}]
signals_def["G5"]=[mcp3, {"R":3, "V":4, "Bl":5}]
signals_def["I5"]=[mcp3, {"R":6, "V":7, "Bl":8}]
signals_def["P5"]=[mcp3, {"R":9, "V":10, "Jh":11, "Jv":12}]

# Routes definition: dictionnary.
# Each value is a list containing a list of signals and the id route on ECoS.
# Each signal is a list containing the name of the signal, a list
# of all led name and the track used to switch the signal to red 
routes={}
routes["LuLg1"]=[[["C5", ["V"], 1],["E5", ["V"], 8]],30004]
routes["Lu1"]=[[["C5", ["Jh","Jv"], 1]],30005]
routes["Lu1pm"]=[[["C5", ["R","Bl"],1]],30005]
routes["LuLg2"]=[[["C5", ["V","Vl"],2],["G5", ["V"],8]],30001]
routes["Lu2"]=[[["C5", ["Jh","Jv","Vl"],2]],30006]
routes["Lu2pm"]=[[["C5", ["R","Bl"],2]],30006]
routes["LuAc2"]=[[["C5", ["V","Vl"],2] ,["G5", ["V"],7]],30002]
routes["Luv3"]=[[["C5", ["R","Bl"],3]],30003]
routes["1Lg"]=[[["E5", ["V"],8]],30007]
routes["1Lgpm"]=[[["E5", ["R","Bl"],8]],30007]
routes["2Lg"]=[[["G5", ["V"],8]],30008]
routes["2Lgpm"]=[[["G5", ["R","Bl"],8]],30008]
routes["2Ac"]=[[["G5", ["V"],7]],30009]
routes["2Acpm"]=[[["G5", ["R","Bl"],7]],30009]

routes["LgLu1"]=[[["J5", ["V"],1],["D5", ["V"],6]],30010]
routes["Lg1"]=[[["J5", ["Jh","Jv"],1]],30011]
routes["Lg1pm"]=[[["J5", ["R","Bl"],1]],30011]
routes["LgLu2"]=[[["J5", ["V","Vl"],2] ,["H5", ["V"],6]],30012]
routes["Lg2"]=[[["J5", ["Jh","Jv","Vl"],2]],30013]
routes["Lg2pm"]=[[["J5", ["R","Bl"],2]],30013]
routes["AcLu2"]=[[["F5", ["V"],2] ,["H5", ["V"],6]],30014]
routes["Ac2"]=[[["F5", ["Jh","Jv"],2]],30015]
routes["Ac2pm"]=[[["F5", ["R","Bl"],2]],30015]
routes["1Lu"]=[[["D5", ["V"],6]],30016]
routes["1Lupm"]=[[["D5", ["R","Bl"],6]],30016]
routes["2Lu"]=[[["H5", ["V"],6]],30017]
routes["2Lupm"]=[[["H5", ["R","Bl"],6]],30017]

routes["v4v3"]=[[["N5", ["J"],3]],30018]
routes["v5v3"]=[[["M5", ["J"],3]],30019]
routes["v3v4"]=[[["I5", ["R","Bl"],4]],30024]
routes["v3v5"]=[[["I5", ["R","Bl"],5]],30025]
routes["v3Lu"]=[[["I5", ["V"],6]],30026]
routes["v3Lupm"]=[[["I5", ["R","Bl"],6]],30026]
routes["v4Ac"]=[[["N5", ["J"],2],["G5", ["V"],7]],30020]
routes["v4Acpm"]=[[["N5", ["J"],2],["G5", ["R","Bl"],7]],30020]
routes["v4Lg"]=[[["N5", ["J"],2],["G5", ["V"],8]],30021]
routes["v4Lgpm"]=[[["N5", ["J"],2],["G5", ["R","Bl"],8]],30021]
routes["v5Ac"]=[[["M5", ["J"],2],["G5", ["V"],7]],30022]
routes["v5Acpm"]=[[["M5", ["J"],2],["G5", ["R","Bl"],7]],30022]
routes["v5Lg"]=[[["M5", ["J"],2],["G5", ["V"],8]],30023]
routes["v5Lgpm"]=[[["M5", ["J"],2],["G5", ["R","Bl"],8]],30023]

routes["Acv4"]=[[["F5", ["R","Bl"],2]],30027]
routes["Lgv4"]=[[["J5", ["R","Bl"],2]],30028]
routes["Acv5"]=[[["F5", ["R","Bl"],2]],30029]
routes["Lgv5"]=[[["J5", ["R","Bl"],2]],30030]

routes["Ac-droit"]=[[],30040]
routes["Ac-dev"]=[[],30041]
routes["AcMo"]=[[["P5", ["V"],9]],0]

routes["tir-car"]=[[["L5", ["R","Bl"],11]],30046]
routes["car-tir"]=[[["K5", ["J"],10]],30047]
routes["CoLg"]=[[["L5", ["V"],8]],30045]
routes["LgCo"]=[[],30044]
routes["LgMoLg"]=[[],30000]

routes["gc1"]=[[],30034]
routes["gc1-tir"]=[[],30035]
routes["gc2"]=[[],30036]
routes["gc2-tir"]=[[],30037]
routes["gc3"]=[[],30038]
routes["gc3-tir"]=[[],30039]

# Association of code sent by Nextion display and route names
decode_dico_mo={}
decode_dico_mo[1]="Lu"
decode_dico_mo[2]="Lg"
decode_dico_mo[4]="Ac"
decode_dico_mo[8]="1"
decode_dico_mo[16]="2"
decode_dico_mo[32]="v3"
decode_dico_mo[64]="v4"
decode_dico_mo[128]="v5"

decode_dico_gc={}
decode_dico_gc[1]="gc1"
decode_dico_gc[2]="gc1-tir"
decode_dico_gc[4]="gc2"
decode_dico_gc[8]="gc2-tir"
decode_dico_gc[16]="gc3"
decode_dico_gc[32]="gc3-tir"

decode_dico_co={}
decode_dico_co[1]="LgCo"
decode_dico_co[2]="CoLg"
decode_dico_co[4]="tir-car"
decode_dico_co[8]="car-tir"
decode_dico_co[16]="LgMoLg"

decode_dico_ac={}
decode_dico_ac[1]="Ac-droit"
decode_dico_ac[2]="Ac-dev"
decode_dico_ac[4]="AcMo"
decode_dico_ac[5]="AcMo"
decode_dico_ac[6]="AcMo"