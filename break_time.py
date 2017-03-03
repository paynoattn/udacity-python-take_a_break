import time
import webbrowser

print('starting program at ', time.ctime())
timer = 0
while (timer < 3):
    print(timer)
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=MfoG3bty8z0')
    timer += 1
