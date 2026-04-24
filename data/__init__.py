from flask import Flask, render_template

app = Flask(__name__)

@app.route('/profile')
def profile():
    user_data = {'name': 'Тест', 'email': 'test@test.com'}
    return render_template('profile.html', title='Профиль пользователя', user=user_data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)