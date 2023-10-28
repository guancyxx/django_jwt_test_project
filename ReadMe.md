The goal is to create a django project, using [django rest framwork](https://www.django-rest-framework.org/), and [jwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/), and implement the following 3 endpoints:

- `/signup/`, testing request:
    
    ```bash
    curl --location 'http://127.0.0.1:8000/signup/' \
    --data-raw '{
        "email": "test@test.com",
        "password": "123"
    }'
    ```
    
    - Expected server response: {id, email} of the user
- `/signin/` , testing request:
    
    ```bash
    curl --location 'http://127.0.0.1:8000/signin/' \
    --data-raw '{
        "email": "test@test.com",
        "password": "123"
    }'
    ```
    
    - Expected server response: dict of {access_token, refresh_token}
- `/me/`, testing request:
    
    ```bash
    curl --location 'http://127.0.0.1:8000/me/' \
    --header 'Authorization: Bearer <access_token_from_signin>'
    ```
    
    - Expected server response: dict of {id, email} that associated with the token.