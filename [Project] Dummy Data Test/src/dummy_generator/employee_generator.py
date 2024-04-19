from faker.generator import random
def generate_employee_dummy_data(fake, n):
    check_duplicate_username = set()
    dummy_data = []

    for i in range(n):
        # int, primary key, auto_incr
        # employee_id

        # varchar(100)
        # https://faker.readthedocs.io/en/stable/locales/en.html#faker.providers.person.en.Provider.first_name
        firstname = fake.first_name()
        lastname = fake.last_name()


        # date
        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.date_time.en_US.Provider.date_between
        birthdate = fake.date_between()

        # char(1)
        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.passport.en_US.Provider.passport_gender
        sex = fake.passport_gender()

        # varchar(100)
        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.address.en_US.Provider.street_address
        street = fake.street_address()
        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.address.en_US.Provider.city
        city = fake.city()

        # smallint
        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.address.en_US.Provider.zipcode
        zipcode = int(fake.zipcode())
        while not 0 <= zipcode <= 32767:
            zipcode = int(fake.zipcode())

        # varchar(100)
        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.address.en_US.Provider.country
        country = fake.country()

        # varchar(120)
        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.internet.en_US.Provider.ascii_company_email
        emailaddress = fake.company_email()

        # varchar(30)
        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker-providers-phone-number
        telephoneno = fake.country_calling_code() + fake.basic_phone_number()

        # decimal(8, 2)
        # https://faker.readthedocs.io/en/master/providers/faker.providers.python.html#faker.providers.python.Provider.pydecimal
        salary = fake.pydecimal(right_digits=2, left_digits=8, positive=True, min_value=2000, max_value=50000)

        # enum ('Marketing','Buchhaltung','Management','Logistik','Flugfeld']
        # https://stackoverflow.com/questions/62724145/choosing-from-a-list-of-names-using-factory-boy-integrated-with-faker
        department_list = ['Marketing','Buchhaltung','Management','Logistik','Flugfeld']
        department = random.choice(department_list)

        # varchar(20), unique
        # https://stackoverflow.com/questions/73433408/how-to-create-a-random-login-with-faker-on-java
        username = fake.user_name()
        while username in check_duplicate_username:
            username = fake.user_name()
        check_duplicate_username.add(username)

        # char(32)
        # https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html#faker.providers.misc.Provider.password

        password = fake.password(special_chars=True, length=32)

        dummy_data.append((firstname, lastname, birthdate, sex, street, city, zipcode, country, emailaddress, telephoneno, salary, department, username, password))

    return dummy_data
