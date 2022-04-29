import sys
from pprint import pprint
from google.cloud import translate_v3

def translate_text(text="Hello, world!", project_id="ia-playground-326814"):

    client = translate_v3.TranslationServiceClient()
    parent = f"projects/{project_id}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            #"source_language_code": "en-US",
            "target_language_code": "pt-BR",
        }
    )

    print(vars(response))

    ret = response.translations[0].translated_text

    print(ret)

    return ret

    # i = 0
    # for translation in response.translations:
    #     print("Translated text: {}".format(translation.translated_text))

    # print("fim do loop")
    # print(vars(response))

try:
    if(len(sys.argv) > 1):
        print("antes do translate")
        translate_text(sys.argv[1])
        print("depois do translate")
        translate_text("Because I didn't want to!")
    else:
        translate_text()
    print("Done!")
except Exception as e:
    print(e)
finally:
    print("fim do programa")