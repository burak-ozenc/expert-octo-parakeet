import requests
import time
from pygame import mixer


def get_init_value():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
    # requesting data from url
    data = requests.get(key)
    data = data.json()
    # playsound('files/soundTest.mp3')
    print(data['price'])
    return data['price']


def get_values():
    init_value = get_init_value()
    mixer.init()
    mixer.music.load("files/soundTest.mp3")
    # p = multiprocessing.Process(target=playsound, args=("files/soundTest.mp3",))
    for i in range(150):
        # time.sleep(0.1)p
        key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

        # requesting data from url
        data = requests.get(key)
        data = data.json()
        temp_value = float(init_value) - float(data['price'])

        calculated_span = abs((float)("%0.1f" % temp_value))
        desired_span = (float)("%0.1f" % 0.3)

        if calculated_span > desired_span:
            combined = " ".join(["higher", data['price']])
            print(combined)
            print(calculated_span)
            new_sleep_time = abs(float(calculated_span)-float(desired_span))
            time.sleep(0.5)
            mixer.music.stop()
            mixer.music.play()
        else:
            combined = " ".join(["lower", data['price']])
            print(combined)
            time.sleep(1)
            mixer.music.stop()
            mixer.music.play()


get_values()