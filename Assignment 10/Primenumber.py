from flask import Flask
app = Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/prime_number/<number>')
def prime_number(number):
    
    number = int(number)

    return {
        "Number": number,
        "isPrime": is_prime(number)
    }

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)