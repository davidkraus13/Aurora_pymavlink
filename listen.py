from pymavlink import mavutil
import os

MAVLINK_DIALECT = "PX4Aurora"
os.environ["MAVLINK20"] = "1"
mavutil.set_dialect(MAVLINK_DIALECT)

connection = mavutil.mavlink_connection('udpin:0.0.0.0:14540')

connection.wait_heartbeat()
print(f"Hearbeat from: {connection.target_system}, component: {connection.target_component}")

while 1:
    msg = connection.recv_match(blocking=True)
    if msg:
        print(msg)