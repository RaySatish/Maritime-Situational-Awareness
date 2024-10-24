INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'maritime_awareness',
    'frontend',
]

# OCR Settings
OCR_ENGINE = 'tesseract'
OCR_LANGUAGE = 'eng'

# RAG Model Settings
RAG_MODEL = 'huggingface/maritime-rag'
