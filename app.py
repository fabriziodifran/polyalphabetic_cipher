from flask import Flask, render_template, redirect, request
from three_alph_enc import encrypt, decrypt

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/encryption', methods=['GET', 'POST'])
def encryption():

	if request.method == 'POST':
		message = request.form['message']
		message_encrypt, keys = encrypt(message)
		
		return render_template('index.html', m_enc=message_encrypt, key11=keys[0], key12=keys[1])
	

	else:
		return render_template('index.html')



@app.route('/decryption', methods=['GET', 'POST'])
def decryption():

	if request.method == 'POST':
		message = request.form['message_enc']
		keys = [int(request.form['key21']), int(request.form['key22'])]
		message_decrypt = decrypt(message, keys)
		
		return render_template('index.html', m_dec=message_decrypt)
	

	else:
		return render_template('index.html')


if __name__ == "__main__":
	app.run(debug = True)


