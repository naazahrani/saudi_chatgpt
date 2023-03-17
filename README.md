# saudi_chatgpt

# requirements

torch

pip install -r requirements.txt
# database

create .env file

POSTGRES_TEST_DB=postgres_test
POSTGRES_HOST=0.0.0.0
POSTGRES_USER=saudigpt
POSTGRES_PASSWORD=123123
POSTGRES_DB=postgres_dev
ENV=dev
BCRYPT_PASSWORD=abdulaziz-confidential-password
SALT_ROUNDS=10
TOKEN_SECRET=abdulaziz123

docker compose up

cd src/

alembic revision --autogenerate -m "initial commit"

alembic upgrade head