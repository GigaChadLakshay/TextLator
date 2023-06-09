import requests
import streamlit as st

url = "https://translate-plus.p.rapidapi.com/translate"


def translate(text: str, translate_language: str, text_language: str):
    payload = {
        "text": r"{}".format(text),
        "source": text_language,
        "target": translate_language
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f040f7203emsh29d8b768df429b6p1a13dfjsn6347c0e9f764",
        "X-RapidAPI-Host": "translate-plus.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


print(dict(translate("my name is lakshay", "hi", "en")))

language_with_code = {"Select Language": "", "Abkhazian": 'af', "Albanian": 'sq', "Amharic": 'am', "Arabic": 'ar',
                      "Armenian": 'hy',
                      "Azerbaijani": 'az',
                      "Basque": 'eu', "Belarusian": 'be', "Bengali": 'bn', "Bosnian": 'bs', "Bulgarian": 'bg',
                      "Catalan": 'ca',
                      "Valencian": 'ca', "Chinese-CN": 'zh-CN', "Chinese-TW": 'zh-TW', "Corsican": 'co',
                      "Croatian": 'hr', "Czech": 'cs', "Danish": 'da', "Dutch": 'nl', "Flemish": 'nl', "English": 'en',
                      "Esperanto": 'eo', "Estonian": 'et', "Finnish": 'fi', "Franch": 'fr', "Western Frisian": 'fy',
                      "Galician": 'gl',
                      "Georgian": 'ka', "German": 'de', "Greek": 'el', "Gujarati": 'gu', "Haitian": 'ht', "Hausa": 'ha',
                      "Hebrew": 'iw', "Hindi": 'hi', "hmong; Mong": 'hmn', "Hungarian": 'hu', "Icelandic": 'is',
                      "Igbo": 'ig',
                      "Indonesian": 'id', "Irish": 'ga', "Italian": 'it', "Japanese": 'ja', "Javanese": 'jv',
                      "Kannada": 'kn',
                      "Kazakh": 'kk', "Central Khmer": 'km', "Kinyarwanda": 'rw', "Korean": 'ko', "Kurdish": 'ku',
                      "Central Kurdish": 'ckb',
                      "Kirghiz, Kyrgyz": 'ky', "kao": 'lo', "Latin": 'la', "Latvian": 'lv', "Lithuanian": 'lt',
                      "Luxembourgish, Letzeburgesch": 'lb',
                      "Macedonian": 'mk', "Malagasy": 'mg', "Malay": 'ms', "Malayalam": 'ml', "Maltese": 'mt',
                      "Maori": 'mi', "Marathi": 'mr',
                      "Mongolian": 'mn', "Burmese": 'my',
                      "Nepali": 'ne', "Norwegian": 'no', "Nyanja": 'ny', "Oriya": 'or', "Pashto, Pushto": 'ps',
                      "Persian": 'fa', "Polish": 'pl',
                      "Portuguese": 'pt', "Punjabi": 'pa', "Romanian, Moldavian": 'ro', "Russian": 'ru', "Samoan": 'sm',
                      "Gaelic": 'gd', "Serbian": 'sr',
                      "Southern Sotho": 'st', "Shona": 'sn', "Sindhi": 'sd',
                      "Slovak": 'sk', "Slovenian": 'sl', "Somali": 'so', "Spanish": 'es', "Sundanese": 'su',
                      "Swahili": 'sw', "Swedish": 'sv',
                      "Tagalog": 'tl', "Tajik": 'tg', "Tamil": 'ta', "Tatar": 'tt', "Telugu": 'te', "Thai": 'th',
                      "Turkish": 'tr',
                      "Turkmen": 'tk', "Ukrainian": 'uk',
                      "Urdu": 'ur', "Uighur": 'ug', "Uzbek": 'uz', "Vietnamese": 'vi', "Welsh": 'cy', "Xhosa": 'xh',
                      "Yiddish": 'yi',
                      "Yoruba": 'yo', "Zulu": 'zu'}

language_names = []
language_code = []
for language, code in language_with_code.items():
    language_names.append(language)
    language_code.append(code)
st.set_page_config(page_title="textlator")
st.title("TextLator")
st.subheader("Text Translator")
st.write("Made By Lakshay")
text_language = st.selectbox(label="", options=language_names)
st.markdown('#### To')
translate_language = st.selectbox(label="", options=language_names, key=0)
text = st.text_area("Enter Text To Translate", placeholder="Type Here...")
translate_button = st.button(label="Translate")
if translate_button:
    if text_language != "Select Language" and translate_language != "Select Language" and text!="":
        st.markdown("#### Translation:")
        translated_to = st.write(dict(translate(text, language_with_code[translate_language], language_with_code[text_language]))['translations']['translation'])
