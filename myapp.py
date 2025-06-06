from flask import Flask, render_template, request, redirect, url_for, session
from flask_babel import Babel

app = Flask(__name__)
app.secret_key = "secret-key"
app.config["BABEL_DEFAULT_LOCALE"] = "en"
app.config["BABEL_TRANSLATION_DIRECTORIES"] = "translations"

# ✅ عرف الدالة أولاً
def select_locale():
    return session.get("lang") or request.accept_languages.best_match(['en', 'ar', 'de'])

# ✅ ثم ثبّت Babel بعدها
babel = Babel()
babel.init_app(app, locale_selector=select_locale)

# ✅ الآن أصبح بإمكانك استخدام select_locale في Jinja
app.jinja_env.globals['get_locale'] = select_locale







@app.route("/set_language", methods=["POST"])
def set_language():
    session["lang"] = request.form["lang"]
    return redirect(request.referrer or url_for("home"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")



