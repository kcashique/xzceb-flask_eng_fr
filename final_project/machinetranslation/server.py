from flask import Flask , render_template, request 
from machinetranslation import translator

app = Flask("Web Translator")

@app_route("/")
def renderIndexpage():
    # Write the code to render template
    return render_template('index.html')

@app_route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text

@app.route("/french_to_english")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)