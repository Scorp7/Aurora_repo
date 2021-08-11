# Resturant Manager In Django

##### Requirements:
1. Python v3+
2. Pip v20+
3. Django v3.2

##### Quick Setup For Windows

- Step 1 : Download Zip/Clone Repository From Github.
- Step 2 : Using CMD or Powershell create a new Python Virtual Environment (https://docs.python.org/3/library/venv.html).
- Step 3 : Activate the newly created virtual environment by using the activation script inside it. Eg - `your-env\Scripts\activate.bat`  or `your-env\Scripts\activate`
- Step 4 : Install all the required packages inside the virtual environment using command - `pip install -r requirements.txt`
- Step 5 : Once all the requirements are installed we can makemigrations in django using django management command `python manage.py makemigrations`.
- Step 6 : After makemigrations we run the command `python manage.py migrate` to write all the changes to the database.
- Step 7 : We need to create a new admin user we do that by using `python manage.py createsuperuser`
- Step 7 : Once superuser is created we can run the development server using the command `python manage.py runserver` 
- Step 8 : Open any browser on your computer and go to `127.0.0.1:8000 `
- Step 9 : Django Admin Interface Is located at `127.0.0.1:8000/root` you can login with the superuser we created in step 7.

##### Quick Setup For Linux/Mac

- Step 1 : Download Zip/Clone Repository From Github.
- Step 2 : Using Terminal Interface create a new Python Virtual Environment (https://docs.python.org/3/library/venv.html).
- Step 3 : Activate the newly created virtual environment by using the activation script inside it. Eg - `source your-env/bin/activate`
- Step 4 : Install all the required packages inside the virtual environment using command - `pip install -r requirements.txt`
- Step 5 : Once all the requirements are installed we can makemigrations in django using django management command `python manage.py makemigrations`.
- Step 6 : After makemigrations we run the command `python manage.py migrate` to write all the changes to the database.
- Step 7 : We need to create a new admin user we do that by using `python manage.py createsuperuser`
- Step 7 : Once superuser is created we can run the development server using the command `python manage.py runserver` 
- Step 8 : Open any browser on your computer and go to `127.0.0.1:8000 `
- Step 9 : Django Admin Interface Is located at `127.0.0.1:8000/root` you can login with the superuser we created in step 7.



Default Login Credentials  :
Admin :
Username : admin@admin.com
Password : admin

Customer:
Username : customer@customer.com
Password : customer


