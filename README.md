# 🏡 Real Estate Django Project

A full-stack real estate listing web application built using **Django**, designed to showcase properties, allow search and filtering, and manage listings through an admin panel.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🚀 Features

- 🔍 Property search and filtering
- 🏢 Listings by location, price, and category
- 📸 Property detail pages with images and description
- 👤 Admin panel to add, update, or delete listings
- 🎨 Responsive front-end design using HTML/CSS
- 🔒 Authentication and admin control (optional)

---

## 🛠️ Tech Stack

| Technology | Description               |
|------------|---------------------------|
| Django     | Web framework (backend)   |
| Python     | Programming language      |
| SQLite     | Default Django DB         |
| HTML/CSS   | Frontend design           |
| Bootstrap  | (Optional) Styling        |
| Git/GitHub | Version control           |

---

## ⚙️ Project Setup

### 🐍 Create and activate a virtual environment

```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# (or use source venv/bin/activate on Mac/Linux)
```

### 📦 Install dependencies

```bash
pip install -r requirements.txt
```

### 🔧 Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 🔐 Create admin user (optional)

```bash
python manage.py createsuperuser
```

### 🚀 Run the server

```bash
python manage.py runserver
```

Then open your browser and visit:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Folder Structure

```
real-estate-django/
├── estate/              # Django app
├── venv/                # Virtual environment (not tracked)
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── db.sqlite3           # Default database
├── manage.py            # Django CLI
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧪 Sample Admin Panel Access

- Go to: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- Log in with your superuser credentials
- Add/update/delete property listings

---

## 📌 Notes

- Don't upload the `venv/` folder or `.env` file to GitHub.
- Add custom styles in `/static/` and templates in `/templates/`.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Anu Senthil Kumar**  
💻 [GitHub Profile](https://github.com/anusenthilkumar)

---

## 🌟 Support

If you like this project, leave a ⭐️ on the repo and share it!  
Issues and pull requests are welcome.
