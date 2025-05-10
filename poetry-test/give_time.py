import arrow
import pendulum


time_on = pendulum.now()
time_ar = arrow.now()

print(f"{time_on} (pendulum library) \n{time_ar} (arrow library)")
