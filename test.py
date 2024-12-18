import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split()
X='watermelon','apple','melon','wildberris'

print(X)
print(ALLOWED_HOSTS)