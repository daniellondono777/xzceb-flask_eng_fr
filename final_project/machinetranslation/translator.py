import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

print(LanguageTranslatorV3.SDK_NAME)


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version='2022-11-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator)
language_translator.set_service_url(url)



def english_to_french(english_text):
    """
    Translator from English to French
    """
    french_text = language_translator.translate(
        text = english_text.lower(),
        model_id = 'en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """
    Translator from French to English
    """
    english_text = language_translator.translate(
        text = french_text.lower(),
        model_id = 'fr-en'
    ).get_result()
    return english_text.get("translations")[0].get("translation")


