from datetime import datetime
import time
'''data_e_hora_passadas = datetime.now()
time.sleep(100)
data_e_hora_atuais = datetime.now()

diferença = data_e_hora_atuais - data_e_hora_passadas

print(data_e_hora_atuais)
print(data_e_hora_passadas)'''


last_time = now()
while on:
    on = check_if_online()
time_online = now() - last_time

last_time = now()
while not on:
    on = check_if_online()
time_offline = now() - last_time

while True:
    check_time_online()
    check_time_offline()
