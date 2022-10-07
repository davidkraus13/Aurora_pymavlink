from pymavlink.dialects.v20 import PX4Aurora as mavlink
from pymavlink import mavutil
import time

MAVLINK_DIALECT = "PX4Aurora"
MAVLINK20 = 1

mavutil.set_dialect(MAVLINK_DIALECT)
connection = mavutil.mavlink_connection('udpout:localhost:14540')
mav = connection.mav


while True:
    connection.mav.heartbeat_send(mavutil.mavlink.MAV_TYPE_ONBOARD_CONTROLLER,
                                                mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0)

    m=mavlink.MAVLink_aurora_meteo_temperature_message(0,0,15,1)
    mav.send(m)

    time.sleep(0.1)
