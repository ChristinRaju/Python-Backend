from flask import Flask
app = Flask(__name__)

@app.route('/factorial/<int:num>')
def factorial_calc(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return f"Factorial of {num} is {fact}"

@app.route('/sum/<int:num1>/<int:num2>')
def sum_numbers(num1, num2):
    return f"Sum of {num1} and {num2} is {num1 + num2}"

@app.route('/palindrome/<string:text>')
def palindrome_check(text):
    
    if text == text[::-1]:
        return f'"{text}" is a palindrome'
    else:
        return f'"{text}" is not a palindrome'
    
if __name__ == "__main__":
    app.run(debug=True, port=5009)
