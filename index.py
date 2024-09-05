

# from flask import Flask, render_template, request, redirect
# import hashlib

# app = Flask(__name__)

# # PayU credentials
# PAYU_KEY = 'JPM7Fg'
# PAYU_SALT = 'your_salt_here'  # Replace with your actual salt

# # Route to handle payment request
# @app.route('/payment', methods=['POST', 'GET'])
# def payment():
#     # Sample data for payment request
#     payment_data = {
#         "key": PAYU_KEY,
#         "txnid": "t6svtqtjRdl4ws",  # Generate a unique transaction ID
#         "amount": "10",
#         "productinfo": "iPhone",
#         "firstname": "Yasar",
#         "email": "test@gmail.com",
#         "phone": "9988776655",
#         "surl": "https://yourwebsite.com/success",
#         "furl": "https://yourwebsite.com/failure"
#     }

#     # Create hash for payment security
#     hash_string = f"{PAYU_KEY}|{payment_data['txnid']}|{payment_data['amount']}|{payment_data['productinfo']}|{payment_data['firstname']}|{payment_data['email']}|{PAYU_SALT}"
#     hash_value = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
#     payment_data['hash'] = hash_value

#     # Render the template to redirect to PayU
#     return render_template('redirect_to_payu.html', payment_data=payment_data)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
import hashlib

app = Flask(__name__)

def calculate_hash(key, txnid, amount, productinfo, firstname, email, salt):
    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|||||||||||{salt}"
    hash_object = hashlib.sha512(hash_string.encode())
    return hash_object.hexdigest()

@app.route('/payment')
def payment():
    payment_data = {
        'key': 'JPM7Fg',
        'txnid': 't6svtqtjRdl4wsdvssddss',
        'productinfo': 'iPhone',
        'amount': '10',
        'email': 'test@gmail.com',
        'firstname': 'Yasar',
        'lastname': '',
        'surl': 'https://apiplayground-response.herokuapp.com/',
        'furl': 'https://apiplayground-response.herokuapp.com/',
        'phone': '9988776655',
        'salt': 'TuxqAugd'
    }
    hash_value = calculate_hash(
        payment_data['key'],
        payment_data['txnid'],
        payment_data['amount'],
        payment_data['productinfo'],
        payment_data['firstname'],
        payment_data['email'],
        payment_data['salt']
    )
    payment_data['hash'] = hash_value

    print(payment_data)

    return render_template('redirect_to_payu.html', payment_data=payment_data)

if __name__ == '__main__':
    app.run(debug=True)
