from flask import Flask
from  random import randint

HIGHER_IMG = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
LOWER_IMG = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
CORRECT_IMG = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'

app = Flask(__name__)
random_number = randint(0,9)

@app.route(f"/<int:guess>")
def response(guess):
    html_wrong_return = f"<div style='text-align: center;'> \
                    <h1 style='color: red;'>The number {guess} is level than the number. Please try again</h1> \
                    <br> \
                    <img style='width: 300px; height: 300px;' src='image'></img>  \
                </div>"
    html_correct_return = f"<div style='text-align: center;'> \
                    <h1 style='color: green;'>The number {guess} is the correct one!</h1> \
                    <h2 style='color: blue;'>Congrats!</h2>\
                    <br> \
                    <img style='width: 300px; height: 300px;' src={CORRECT_IMG}></img>  \
                </div>"
   
    if guess == random_number:
        return html_correct_return
    elif guess > random_number:
        html_wrong_return = html_wrong_return.replace("level", "HIGHER")
        html_wrong_return = html_wrong_return.replace("image", HIGHER_IMG)
        return html_wrong_return
    else:
        html_wrong_return = html_wrong_return.replace("level", "LOWER")
        html_wrong_return = html_wrong_return.replace("image", LOWER_IMG)
        return html_wrong_return 
      
@app.route("/")
def hello_world():
    return f"<div style='text-align: center;'> \
        <h1>Guess a number between 0 and 9</h1> \
        <br> \
        <img style='width: 300px; height: 300px;' src='https://media1.giphy.com/media/JW5vQQNt4pbfq/200.webp?cid=ecf05e47s1mqr2u65uq2j1yke10vkdg508qu8boeqnyvyhw7&ep=v1_gifs_search&rid=200.webp&ct=g'></img> \
    </div>"
    



