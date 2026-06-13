# 🛒 eCart - Django E-Commerce Application

eCart is a simple e-commerce web application built using **Django** and **Bootstrap**. The project demonstrates the fundamentals of building an online shopping platform with features such as product browsing, cart management, user authentication, profile management, and order tracking.


## 📸 Application Screenshots

> Add your screenshots inside `/Uploads/screenshots/` folder and update the image paths.

**Home Page**

![Home]()

**Product Details**

![Product Details]()

**Shopping Cart**

![Cart]()

**Login**

![Login]()

**Signup**

![Signup]()

**Verify OTP**

![Verify OTP]()

**Profile**

![Profile]()

**Orders**

![Orders]()


## 🚀 Features Implemented

**User authentication:**
* User Signup
* Login using Email
* Session-based Authentication
* Logout

**Product management:**
* Display all products
* Category-wise filtering
* Product detail page
* Product images
* Product descriptions

**Shopping Cart:**
* Add products to cart
* Remove products from cart
* Quantity management
* Total price calculation
* Checkout

**Orders:**
* Place orders
* View previous orders
* Order status
* Order history

**Profile Management:**
* View profile information
* Edit profile information
* Manage addresses (UI implemented)


## 🏗️ Project Structure

```
ecart
├── Readme.md
├── db.sqlite3
├── eCart
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── store
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── middlewares
│   ├── migrations
│   ├── models
│   ├── templates
│   ├── templatetags
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   └── views
├── uploads
│   ├── logo
│   └── products
└── venv
```

## ⚙️ Django Project Setup

**Step-1:** Create Virtual Environment

`python -m venv venv`

**Step-2:** Activate

Windows: `venv\Scripts\activate` \
Linux/macOS: `source venv/bin/activate`

**Step-3:** Install Packages

`pip install -r requirements.txt`


**Step-4:** Apply Migrations

`python manage.py makemigrations` \
`python manage.py migrate`


**Step-5:** Run Server

`python manage.py runserver`

**Step-6:** Open

`http://127.0.0.1:8000/store`


## 📦 Packages Used

### Django

**Purpose:**

* MVC/MVT framework
* URL Routing
* ORM
* Template Engine
* Authentication
* Session Management


### Pillow

**Purpose:**

* ImageField support
* Product image uploads


### Bootstrap 5

**Purpose:**

* Responsive UI
* Navbar
* Forms
* Cards
* Tables
* Buttons
* Modals

Included using CDN.


### Bootstrap Icons

**Purpose:**

* Icons for cart
* Profile
* Social media
* Navigation

Included using CDN.


## 🗄️ Models

### Customer

Stores customer information.

**Fields:**

* name
* phone
* email
* address


### Category

Stores product categories.

**Fields:**

* name

**Examples:**

* Computer accessories
* House accessories
* Mobile accessories


### Product

Stores product details.

**Fields:**

* name
* price
* category
* image
* description


### Order

Stores placed orders.

**Fields:**

* customer
* product
* quantity
* price
* address
* phone
* date
* status


## 🌐 URL Routing

### Examples:

|URL|Name|
|---|----|
|`/store`|Home Page|
|`/store/signup`|Signup Page|
|`/store/login`|Login Page|
|`/store/verify_otp`|Verify OTP|
|`/store/logout` |Logout|
|`/store/cart`|Shopping Cart|
|`/store/orders`|Orders Page|
|`/store/profile`|User Profile|
|`/store/product/<id>`| Product Details|
|`/store/check-out`| Checkout|

## 🧠 Views Implemented

### Index View

**Responsibilities:**

* Fetch products
* Filter by category
* Render home page


### Product Detail View

**Responsibilities:**

* Display single product
* Add item to cart


### Signup View

**Responsibilities:**

* Register customer with email


### Login View

**Responsibilities:**

* Authenticate user
* Create session


### Logout View

**Responsibilities:**

* Destroy session
* Redirect to home


### Cart View

**Responsibilities:**

* Show selected products
* Remove products
* Calculate totals


### Checkout View

**Responsibilities:**

* Create orders
* Store shipping information
* Clear cart


### Orders View

**Responsibilities:**

* Fetch customer orders
* Display order history


### Profile View

**Responsibilities:**

* Show customer details
* Update profile information


## 🧮 Custom Template Filters

Implemented inside: `store/templatetags/`

**Examples:**

* cart_quantity
* price_total
* total_cart_price
* currency
* multiply

These simplify calculations directly inside templates.


## Email utlity management system

The application includes a utility function for sending OTP (One-Time Password) emails to users during authentication or verification processes. \
This functionality is implemented inside the ```utils.py``` file using Django’s built-in email system.

## Code implementation

```
from django.core.mail import send_mail
from django.conf import settings


def send_otp_email(email, otp):
    send_mail(
        subject="OTP Verification",
        message=f"Your OTP is: {otp}. This OTP is valid for 5 minutes.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
```


### How it Works

* The function `send_otp_email(email, otp)` is called when OTP verification is required.
* Django’s `send_mail()` function is used to send emails.
* The email contains:
  * `Subject: OTP Verification`
  * `Message: The generated OTP and validity time (5 minutes)`
* from_email is configured using `settings.EMAIL_HOST_USER`
* `recipient_list` sends the OTP to the user's registered email address


### Configuration

To use this feature, email settings must be configured in ```settings.py```:

```
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "Your email id"
EMAIL_HOST_PASSWORD = "Your email host password"
```

**Note:**  \
*Currently, the ```send_otp_email(email, otp)``` function is commented out in both login.py and signup.py views. Uncomment these lines to enable OTP email sending functionality.*

## 💾 Session Management

The application uses Django Sessions to store:

* Logged-in customer ID
* Shopping cart items

**Example:**

`request.session["customer"]` \
`request.session["cart"]`


## 🎨 Frontend

**Built using:**

* HTML
* Bootstrap v5.3
* Bootstrap Icons
* JavaScript
* Django Template Language (DTL)


## 🔮 Planned Improvements

* Product search with autocomplete
* Razorpay/Stripe payment integration


## 👨‍💻 Author

Developed as a learning project to understand:

* Django MVT Architecture
* ORM
* Session Management
* Authentication
* Template Rendering
* CRUD Operations
* E-Commerce Application Development
