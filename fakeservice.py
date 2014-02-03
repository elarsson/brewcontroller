# Script that outputs fake sensor data to stdout.
# Separator between sensor outputs is semicolon, separator between sensor name and sensor value is colon, e.g.
# Temp1:241.4;Temp2:13.041;Temp2:12.4;

#TODO: read from stdin or something to simulate comms from pc to arduino

import time
import sys
import select

class State:
	Temp1 = 20.0
	Temp2 = 25.0
	DesiredTemp1 = 70.0
	DesiredTemp2 = 45.0
	
	PumpSpeed1 = 0.5
	PumpSpeed2 = 0.7
	
	ValveState1 = 1
	ValveState2 = 3
	ValveState3 = 0
	
def EncodeState(state):
	return "T1:" + str(state.Temp1) + ";T2:" + str(state.Temp2) + ";"

defState = State()
T1d = 0.7
T2d = 1.2
allchars = ""

while(1):
	sys.stdout.write(EncodeState(defState))
	sys.stdout.flush()
	time.sleep(1)
	
	if (defState.Temp1 < defState.DesiredTemp1):
		defState.Temp1 += T1d
	else:
		defState.Temp1 -= T1d

	if (defState.Temp2 < defState.DesiredTemp2):
		defState.Temp2 += T2d
	else:
		defState.Temp2 -= T2d

#	(rlist, _, _) = select.select([sys.stdin],[],[],0)
#	if len(rlist)>0:
#		allchars += sys.stdin.read(1)
#		print allchars
