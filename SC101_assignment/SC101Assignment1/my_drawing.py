"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: 浮世繪．改

    不知道畫什麼的時候，偶然看到冰箱上貼著浮世繪的明信片，沒錯！就決定是它了
    """
    window = GWindow()

    background = GRect(500, 500)
    background.filled = True
    background.fill_color = 'lightgray'
    background.color = 'lightgray'
    window.add(background)
    size = 30

    for i in range(3):
        for j in range(25):
            sea = GOval(size, size)
            sea.filled = True
            sea.fill_color = 'steelblue'
            sea.color = 'steelblue'
            sea.x = j*20
            sea.y = 470-i*50
            window.add(sea)

            sea = GOval(size, size)
            sea.filled = True
            sea.fill_color = 'skyblue'
            sea.color = 'skyblue'
            sea.x = j*20
            sea.y = 445-i*50
            window.add(sea)

    for i in range(19):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'blue'
        wave_1.color = 'blue'
        wave_1.x = i*20
        wave_1.y = 370
        window.add(wave_1)

    for i in range(17):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'navy'
        wave_1.color = 'navy'
        wave_1.x = i*20
        wave_1.y = 350
        window.add(wave_1)

    for i in range(15):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'blue'
        wave_1.color = 'blue'
        wave_1.x = i*20
        wave_1.y = 330
        window.add(wave_1)
        wave_2 = GOval(size, size)
        wave_2.filled = True
        wave_2.fill_color = 'blue'
        wave_2.color = 'blue'
        wave_2.x = i*20+2**6.5
        wave_2.y = 50
        window.add(wave_2)

    for i in range(13):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'navy'
        wave_1.color = 'navy'
        wave_1.x = i*20
        wave_1.y = 310
        window.add(wave_1)
        wave_2 = GOval(size, size)
        wave_2.filled = True
        wave_2.fill_color = 'navy'
        wave_2.color = 'navy'
        wave_2.x = i*20+2**6
        wave_2.y = 70
        window.add(wave_2)

    for i in range(11):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'blue'
        wave_1.color = 'blue'
        wave_1.x = i*20
        wave_1.y = 290
        window.add(wave_1)
        wave_2 = GOval(size, size)
        wave_2.filled = True
        wave_2.fill_color = 'blue'
        wave_2.color = 'blue'
        wave_2.x = i*20+2**5
        wave_2.y = 90
        window.add(wave_2)

    for i in range(9):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'navy'
        wave_1.color = 'navy'
        wave_1.x = i*20
        wave_1.y = 270
        window.add(wave_1)
        wave_2 = GOval(size, size)
        wave_2.filled = True
        wave_2.fill_color = 'navy'
        wave_2.color = 'navy'
        wave_2.x = i*20+2**4
        wave_2.y = 110
        window.add(wave_2)

    for i in range(7):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'blue'
        wave_1.color = 'blue'
        wave_1.x = i*20
        wave_1.y = 250
        window.add(wave_1)
        wave_2 = GOval(size, size)
        wave_2.filled = True
        wave_2.fill_color = 'blue'
        wave_2.color = 'blue'
        wave_2.x = i*20+2**3
        wave_2.y = 130
        window.add(wave_2)

    for i in range(5):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'navy'
        wave_1.color = 'navy'
        wave_1.x = i*20
        wave_1.y = 230
        window.add(wave_1)
        wave_2 = GOval(size, size)
        wave_2.filled = True
        wave_2.fill_color = 'navy'
        wave_2.color = 'navy'
        wave_2.x = i*20+2**2
        wave_2.y = 150
        window.add(wave_2)

    for i in range(3):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'blue'
        wave_1.color = 'blue'
        wave_1.x = i*20
        wave_1.y = 210
        window.add(wave_1)
        wave_2 = GOval(size, size)
        wave_2.filled = True
        wave_2.fill_color = 'blue'
        wave_2.color = 'blue'
        wave_2.x = i*20
        wave_2.y = 170
        window.add(wave_2)

    for i in range(2):
        wave_1 = GOval(size, size)
        wave_1.filled = True
        wave_1.fill_color = 'navy'
        wave_1.color = 'navy'
        wave_1.x = i*20
        wave_1.y = 190
        window.add(wave_1)

    for i in range(4):
        wave_3 = GOval(size, size)
        wave_3.filled = True
        wave_3.fill_color = 'lightblue'
        wave_3.color = 'lightblue'
        wave_3.x = 370+i*20
        wave_3.y = 70
        window.add(wave_3)

        wave_3 = GOval(size, size)
        wave_3.filled = True
        wave_3.fill_color = 'aliceblue'
        wave_3.color = 'aliceblue'
        wave_3.x = 370+i*20
        wave_3.y = 90
        window.add(wave_3)

        wave_3 = GOval(size, size)
        wave_3.filled = True
        wave_3.fill_color = 'lightblue'
        wave_3.color = 'lightblue'
        wave_3.x = 350+i*20
        wave_3.y = 110
        window.add(wave_3)

        wave_3 = GOval(size, size)
        wave_3.filled = True
        wave_3.fill_color = 'aliceblue'
        wave_3.color = 'aliceblue'
        wave_3.x = 390+i*20
        wave_3.y = 50
        window.add(wave_3)

    for i in range(15):
        wave_4 = GOval(size, size)
        wave_4.filled = True
        wave_4.fill_color = 'lightblue'
        wave_4.color = 'lightblue'
        wave_4.x = i*20+2**7
        wave_4.y = 30
        window.add(wave_4)

    for i in range(9):
        wave_5 = GOval(size, size)
        wave_5.filled = True
        wave_5.fill_color = 'aliceblue'
        wave_5.color = 'aliceblue'
        wave_5.x = i*20+200
        wave_5.y = 10
        window.add(wave_5)


if __name__ == '__main__':
    main()
