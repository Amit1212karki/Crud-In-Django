from django import template
from django.utils.translation import get_language
import json
from django.conf import settings

register = template.Library()

@register.simple_tag

def json_translation(key):
    translations = {
        'en': 'locale/translations/en.json',
        'ne': 'locale/translations/ne.json',
    }
    current_language = get_language()  # Get the current language code

    try:
        with open(translations.get(current_language, translations['en']), encoding='utf-8') as f:
            translation_dict = json.load(f)
            return translation_dict.get(key, key)
    except FileNotFoundError:
        pass  # Handle file not found error or return the key as fallback

    return key  # Return key as fallback if translation not found