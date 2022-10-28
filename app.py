from flask import Flask, render_template, request
from models import PersonalForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '@#123456&*()'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PersonalForm()
    if request.method == 'POST':
        nama = form.nama.data
        alamat = form.alamat.data
        jenisKelamin = form.jenisKelamin.data
        agama = int(form.agama.data)
        hobi1 = form.hobi1.data
        hobi2 = form.hobi2.data
        hobi3 = form.hobi3.data
        return render_template('response.html', nama=nama,
                               alamat=alamat, jenisKelamin=jenisKelamin,
                               agama=agama, hobi1=hobi1,
                               hobi2=hobi2, hobi3=hobi3)
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
