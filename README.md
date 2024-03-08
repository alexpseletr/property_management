# Property Management Django
Reservation and property management API, made in django rest framework

## Configuração do Ambiente Virtual

1. Install Python (if not already installed): https://www.python.org/downloads/
2. Create a virtual environment:
    ```
    python -m venv myenv
    ```
3. Install packages:
    ```
    pip install django
    pip install djangorestframework
    ```
4. Activate the virtual environment:
    - On Windows:
        ```
        myenv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source myenv/bin/activate
        ```

## Django commands

- **Create migrations:**
```
python manage.py makemigrations
```
- **Apply migrations:**
```
python manage.py migrate
```
- **Load data to populate the database:**
```
python manage.py loaddata seeder.json
```

- **Run development server:**
```
python manage.py runserver
```

- **Run tests:**
```
python manage.py test
```

## Endpoints

- `/api/properties/`: Endpoint to manipulate properties.
- `/api/adverts/`: Endpoint for handling advertisements.
- `/api/reservations/`: Endpoint to handle reservations.


## CURL commands to test the application

### Properties API

- **Create a new property:**
```bash
curl -X POST http://127.0.0.1:8000/api/properties/ \
     -d "property_code=ABC123" \
     -d "guest_limit=4" \
     -d "bathroom_count=2" \
     -d "accept_pets=true" \
     -d "cleaning_fee=50.00" \
     -d "activation_date=2024-03-07" 
```
- **Search a list of properties:**
```bash
curl http://127.0.0.1:8000/api/properties/
```
- **Search for an individual property: "api/properties/<id>/"**
```bash
curl http://127.0.0.1:8000/api/properties/1/
```
- **Change an existing property: "api/properties/<id>/"**
```bash
curl -X PUT http://127.0.0.1:8000/api/properties/2/ \
     -H "Content-Type: application/json" \
     -d '{"property_code": "BCD1231", "guest_limit": 6, "bathroom_count": 3, "pets_allowed": true, "cleaning_fee": 85.00, "activation_date": "2024-03-10"}'
```
- **Delete an existing property:  "api/properties/<id>/"**
```bash
curl -X DELETE http://127.0.0.1:8000/api/properties/3/
```

### Adverts API 
- **Criar um novo anúncio:**
```bash
curl -X POST http://127.0.0.1:8000/api/adverts/ \
     -H "Content-Type: application/json" \
     -d '{"property_id": 1, "platform_name": "AirBnb", "platform_fee": 10.00}'
```
- **Search a list of adverts:**
```bash
curl http://127.0.0.1:8000/api/adverts/
```
- **Search for an individual advert: "api/adverts/<id>/"**
```bash
curl http://127.0.0.1:8000/api/adverts/2/
```
- **Change an existing advert: "api/adverts/<id>/"**
```bash
curl -X PUT http://127.0.0.1:8000/api/adverts/2/ \
     -H "Content-Type: application/json" \
     -d '{"id": 2, "property_id": 1, "platform_name": "AirBnb", "platform_fee": 35.00}'
```

### Reservation API
- **Create a new reservation:**
```bash
curl -X POST http://127.0.0.1:8000/api/reservations/ \
     -H "Content-Type: application/json" \
     -d '{"adverts_id": 1, "check_in_date": "2024-03-15", "check_out_date": "2024-03-20", "total_price": 200.00, "comment": "A wonderful stay!", "guest_count": 2}'
```
- **Search a list of reservations:**
```bash
curl http://127.0.0.1:8000/api/reservations/
```
- **Search for an individual reservation: "api/reservations/<reservation_id>/"**
```bash
curl http://127.0.0.1:8000/api/reservations/uOnalTBZ2y/
```
- **Delete an existing reservation: "api/reservations/<reservation_id>/"**
```bash
curl -X DELETE http://127.0.0.1:8000/api/reservations/uOnalTBZ2y/
```

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push your changes to your fork: `git push origin feature-name`.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [GNU LGPLv3].
