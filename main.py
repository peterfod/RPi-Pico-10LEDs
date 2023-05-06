from machine import Pin
import utime

leds = [Pin(i, Pin.OUT) for i in range(0,10)]

if __name__ == '__main__':
  while True:
    #Animation-1
    for n in range(0,10):
      leds[n].value(1)
      utime.sleep_ms(50)
    for n in range(0,10):
      leds[n].value(0)
      utime.sleep_ms(50)
    for n in range(9,-1,-1):
      leds[n].value(1)
      utime.sleep_ms(50)
    for n in range(9,-1,-1):
      leds[n].value(0)
      utime.sleep_ms(50)

    #Animation-2   
    for n in range(0,10):
      leds[n].value(1)
      utime.sleep(0.1)
      leds[n].value(0)
    for n in range(9,-1,-1):
      leds[n].value(1)
      utime.sleep(0.1)
      leds[n].value(0)

    #Animation-3  
    for n in range(0,10):
      leds[n].value(0)
      utime.sleep(0.1)
      leds[n].value(1)
    for n in range(9,-1,-1):
      leds[n].value(0)
      utime.sleep(0.1 )
      leds[n].value(1)

    #Animation-4   
    for n in range(0,10):
      leds[n].value(1)
      utime.sleep(0.1)
    for n in range(9,-1,-1):
      leds[n].value(0)
      utime.sleep(0.1)
    for n in range(9,-1,-1):
      leds[n].value(1)
      utime.sleep(0.1)
    for n in range(0,10):
      leds[n].value(0)
      utime.sleep(0.1)


    #Animation-5  
    for n in range(0,5):
      leds[n].value(1)
      leds[9-n].value(1)
      utime.sleep(0.1)
      leds[n].value(0)
      leds[9-n].value(0)


    #Animation-6   
    for n in range(0,5):
      leds[n].value(0)
      leds[9-n].value(0)
      utime.sleep(0.1)
      leds[n].value(1)
      leds[9-n].value(1)

    #Animation-6   
    for n in range(0,5):
      leds[4-n].value(1)
      leds[n+5].value(1)
      utime.sleep(0.1)
      leds[4-n].value(0)
      leds[n+5].value(0)

    #Animation-7
    for n in range(0,5):
      leds[4-n].value(0)
      leds[n+5].value(0)
      utime.sleep(0.1)
      leds[4-n].value(1)
      leds[n+5].value(1)

    #Animation-8
    for n in range(0,5 ):
      leds[n].value(1)
      leds[9-n].value(1)
      utime.sleep(0.1)
      leds[n].value(0)
      leds[9-n].value(0)
      for n in range(0, 5):
        leds[4-n].value(1)
        leds[n+5].value(1)
        utime.sleep(0.1)
        leds[4-n].value(0)
        leds[n+5].value(0)