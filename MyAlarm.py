import datetime
import winsound             #pip install Playsounf

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    altime = altime[11:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done, alarm is set for {Timing}")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("Wake up")
                winsound.PlaySound('Jarvisalarm.wav', winsound.SND_FILENAME)

            elif Mireal<datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    alarm('11:53 AM')

