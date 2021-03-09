import qrcode
import random
import os
import shutil
import glob
from flask import Flask, render_template, request, redirect

#Folder for generated QR code
photofolder = os.path.join('static', 'photo')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = photofolder


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #Creating and naming the QR code file
        img = qrcode.make(request.form['generate'])
        stringint = str(random.randint(0, 1000000))
        img.save(f'{stringint}.png')

        with os.scandir('C:/Users/xxxde/PycharmProjects/flaskstuff') as entries:
            for entry in entries:
                if 'png' in entry.name[-3:]:
                    try:
                        shutil.move('C:/Users/xxxde/PycharmProjects/flaskstuff/{}'.format(entry.name),
                                    'C:/Users/xxxde/PycharmProjects/flaskstuff/static/photo/{}'.format(entry.name))
                    except:
                        pass
        return redirect('/yourqr')
    else:
        return render_template('index.html')


@app.route('/yourqr')
def qr():
    direc = glob.glob('C:/Users/xxxde/PycharmProjects/flaskstuff/static/photo/*')
    newest = max(direc, key=os.path.getctime)
    newest = os.path.basename(f"{newest}")
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], f'{newest}')
    return render_template('generatedqr.html', user_image=full_filename)


if __name__ == '__main__':
    app.run(debug=True)
