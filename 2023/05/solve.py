import sys

def get_location_by_seed(data, seed):
    soil = None
    for desc in data['seed_to_soil']:
        if desc[1] <= seed < desc[1] + desc[2]:
            soil = desc[0] + seed - desc[1]
            break
    if soil is None:
        soil = seed
    fertilizer = None
    for desc in data['soil_to_fertilizer']:
        if desc[1] <= soil < desc[1] + desc[2]:
            fertilizer = desc[0] + soil - desc[1]
            break
    if fertilizer is None:
        fertilizer = soil
    water = None
    for desc in data['fertilizer_to_water']:
        if desc[1] <= fertilizer < desc[1] + desc[2]:
            water = desc[0] + fertilizer - desc[1]
            break
    if water is None:
        water = fertilizer
    light = None
    for desc in data['water_to_light']:
        if desc[1] <= water < desc[1] + desc[2]:
            light = desc[0] + water - desc[1]
            break
    if light is None:
        light = water
    temperature = None
    for desc in data['light_to_temperature']:
        if desc[1] <= light < desc[1] + desc[2]:
            temperature = desc[0] + light - desc[1]
            break
    if temperature is None:
        temperature = light
    humidity = None
    for desc in data['temperature_to_humidity']:
        if desc[1] <= temperature < desc[1] + desc[2]:
            humidity = desc[0] + temperature - desc[1]
            break
    if humidity is None:
        humidity = temperature
    location = None
    for desc in data['humidity_to_location']:
        if desc[1] <= humidity < desc[1] + desc[2]:
            location = desc[0] + humidity - desc[1]
            break
    if location is None:
        location = humidity
    return location

def get_seed_by_location(data, location):
    humidity = None
    for desc in data['humidity_to_location']:
        if desc[0] <= location < desc[0] + desc[2]:
            humidity = location - desc[0] + desc[1]
            break
    if humidity is None:
        humidity = location
    temperature = None
    for desc in data['temperature_to_humidity']:
        if desc[0] <= humidity < desc[0] + desc[2]:
            temperature = humidity - desc[0] + desc[1]
            break
    if temperature is None:
        temperature = humidity
    light = None
    for desc in data['light_to_temperature']:
        if desc[0] <= temperature < desc[0] + desc[2]:
            light = temperature - desc[0] + desc[1]
            break
    if light is None:
        light = temperature
    water = None
    for desc in data['water_to_light']:
        if desc[0] <= light < desc[0] + desc[2]:
            water = light - desc[0] + desc[1]
            break
    if water is None:
        water = light
    fertilizer = None
    for desc in data['fertilizer_to_water']:
        if desc[0] <= water < desc[0] + desc[2]:
            fertilizer = water - desc[0] + desc[1]
            break
    if fertilizer is None:
        fertilizer = water
    soil = None
    for desc in data['soil_to_fertilizer']:
        if desc[0] <= fertilizer < desc[0] + desc[2]:
            soil = fertilizer - desc[0] + desc[1]
            break
    if soil is None:
        soil = fertilizer
    seed = None
    for desc in data['seed_to_soil']:
        if desc[0] <= soil < desc[0] + desc[2]:
            seed = soil - desc[0] + desc[1]
            break
    if seed is None:
        seed = soil
    
    seed_ranges = list(zip(data['seeds'][::2], data['seeds'][1::2]))
    for desc in seed_ranges:
        if desc[0] <= seed < desc[0] + desc[1]:
            return seed
    return None
    # return seed if seed in data['seeds'] else None

def part1(data): # 💀 cursed but kinda easy to understand
    locations = []
    for seed in data['seeds']:
        locations.append(get_location_by_seed(data, seed))
    return min(locations)

def part2(data): # 💀💀 both cursed and slow as fuck but works, eventually
    for i in range(1000000000):
        # took about 5 mins on my machine 😩
        if get_seed_by_location(data, i):
            return i

if __name__ == '__main__':
    filename = 'input' if '-t' not in sys.argv else 'test'
    with open(filename) as f:
        text = f.read().split('\n\n')
    data = {}
    data['seeds'] = [int(x) for x in text[0].split()[1:]]
    data['seed_to_soil'] = [[int(x) for x in line.split()] for line in text[1].split('\n')[1:]]
    data['soil_to_fertilizer'] = [[int(x) for x in line.split()] for line in text[2].split('\n')[1:]]
    data['fertilizer_to_water'] = [[int(x) for x in line.split()] for line in text[3].split('\n')[1:]]
    data['water_to_light'] = [[int(x) for x in line.split()] for line in text[4].split('\n')[1:]]
    data['light_to_temperature'] = [[int(x) for x in line.split()] for line in text[5].split('\n')[1:]]
    data['temperature_to_humidity'] = [[int(x) for x in line.split()] for line in text[6].split('\n')[1:]]
    data['humidity_to_location'] = [[int(x) for x in line.split()] for line in text[7].split('\n')[1:]]
    print(part1(data))


    import time
    start = time.time()
    print(part2(data))
    end = time.time()
    print(end - start)