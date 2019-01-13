from flask import render_template

from wedding_gallery import app, forms


@app.route('/')
def index():
    photos = [
        'https://www.abc.net.au/news/image/9670912-3x2-700x467.jpg',
        'https://cdn.vox-cdn.com/thumbor/3ZoHPzXw1lI6_1bzIxT6AWMgrM0=/0x0:1920x1080/1200x800/filters:focal(573x260:879x566)/cdn.vox-cdn.com/uploads/chorus_image/image/61619931/Assassin_s_Creed__Odyssey__24.0.jpeg',
        'https://cdn.theatlantic.com/assets/media/img/photo/2018/07/photos-of-the-week/w01_RTS1VUP1/main_900.jpg?1531496186'
    ]
    template_args = {
        'photos': photos,
        'title': 'Wedding Gallery'
    }
    return render_template('index.html', **template_args)


@app.route('/login')
def login():
    form = forms.LoginForm()
    template_args = {
        'form': form,
        'title': 'Wedding Gallery'
    }
    return render_template('login.html', **template_args)
