from ibm_watson import SpeechToTextV1

print("In this first section we'll convert speech to text using the ibm_watson package")
print("")

url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"

apikey_s2t = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-"

s2t = SpeechToTextV1(iam_apikey=apikey_s2t, url=url_s2t)

filename = 'hello_world.wav'

with open(filename, mode='rb') as wav:#rb means read as a binary format
    response = s2t.recognize(audio=wav, content_type='audio/wav')
    print("Response:")
    print(response.result)
    recognized_text = response.result['result'][0]['alternatives'][0]['transcript']
    print("Recognized text is:")
    print(recognized_text)


print("In this second section we'll translate the text using the ibm_watson package")

from ibm_watson import LanguageTranslatorV3

url_lt = "https://gateway.watsonplatform.net/language-translator/api"

apikey_lt = "XXXXXXXXXXXXXXXXXXXXXXXX"

version_lt = '2018-05-01'

language_translator = LanguageTranslatorV3(iam_apikey=apikey_lt, url=url_lt, version=version_lt)
all_langs = language_translator.list_identifiable_languages().get_result()

print("The list of all languages that can be translated with LT v3: ")
print(all_langs)

recognized_text = 'hello this is python'
info = "The message will be translated to Spanish is: {}\n".format(recognized_text)
print(info)

translation_response = language_translator.translate(text=recognized_text, model_id='en-es')

translation = translation_response.get_result()
spanish_translation = translation['translations'][0]['translation'] #get only the translation

text_translated = "The result of the translation of the text to Spanish is: {}\n".format(spanish_translation)

print(text_translated)