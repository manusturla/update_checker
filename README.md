# Update notifier
This simple application checks if changes were made to text in 
a webpage. 
It notifies the user via Telegram if changes were made.

The webpage URL is set as a variable in the `config.py` file.

# Installation
1. Clone the repository.
2. Run the following commands:
```bash
python -m virtualenv venv
source venv/bin/activate
python -m pip install -r requirements.txt
docker compose up -d  # start postgres dev database
sudo -u postgres psql --dbname=postgres -f ./create_db.sql
python -m flask db upgrade # run migrations and create proper tables
```
3. Create `.env` file with the following variables:
```bash
POSTGRES_HOST=localhost
POSTGRES_USERNAME=
POSTGRES_PASSWORD=
POSTGRES_DATABASE=
POSTGRES_PORT=5432

TELEGRAM_BOT_API_KEY= # your bot api key
TELEGRAM_NOTIFICATION_CHAT_ID= # your chat id
```

# Running
```bash
export $(cat .env | xargs) # export environment variables
docker compose up -d # start postgres dev database
source venv/bin/activate
python -m flask run
```
