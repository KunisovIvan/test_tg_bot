# Test Tg Bot
Tests django-project.

# bot_name: @test_phone_tg_bot


## Virtual Environment

0. Create Virtual Environment

    ```
    $ sudo apt install python3-pip python3-venv
    $ python3 -m venv .venv
    ```

0. Activate Virtual Environment

    ```
    source .venv/bin/activate
    ```

0. Install requirements

    ```
    (.venv)$ pip install -r requirements.txt
    ```

0. Copy `.env.example` file to `.env` and correct variables if not yet

## Run

Before running the app upgrade a DB:

```
(.venv) $ python manage.py migrate
```

Run the app with:

```
(.venv) $ python manage.py run_bot
```