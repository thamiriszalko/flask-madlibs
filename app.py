from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route('/madlibs')
def madlibs_form():
    prompts = story.prompts

    return render_template("madlibs_form.html", prompts=prompts)


@app.route('/madlibs/result')
def madlibs_result():
    text = story.generate(request.args)

    return render_template("madlibs_result.html", text=text)
