time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_split = time_string.split(',')
general_time = 0

for part in time_split:
    components = part.split()

    for component in components:
        if 'h' in component:
            hours = int(component.replace('h', ''))
            general_time += hours * 60
        elif 'm' in component:
            minutes = int(component.replace('m', ''))
            general_time += minutes
        elif 's' in component:
            sec = int(component.replace('s', ''))
            general_time += sec//60

print(general_time)
