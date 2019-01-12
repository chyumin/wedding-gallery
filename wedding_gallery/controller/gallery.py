from flask import render_template

from wedding_gallery import app


@app.route('/')
def index():
    photos = [
        'https://www.abc.net.au/news/image/9670912-3x2-700x467.jpg',
        'https://cdn.vox-cdn.com/thumbor/3ZoHPzXw1lI6_1bzIxT6AWMgrM0=/0x0:1920x1080/1200x800/filters:focal(573x260:879x566)/cdn.vox-cdn.com/uploads/chorus_image/image/61619931/Assassin_s_Creed__Odyssey__24.0.jpeg',
        'https://cdn.theatlantic.com/assets/media/img/photo/2018/07/photos-of-the-week/w01_RTS1VUP1/main_900.jpg?1531496186'
    ]
    return render_template('index.html', photos=photos)
