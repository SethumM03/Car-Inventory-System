## 🚗 Car Inventory System

A **Car Dealership Inventory Management System** built with **Python (Flask), MySQL, and Bootstrap**.
This project allows dealerships to easily manage their car listings with features like **adding, updating, deleting, viewing, searching, filtering, sorting, and uploading car photos**.


<img width="1919" height="1079" alt="Screenshot 2025-09-18 194555" src="https://github.com/user-attachments/assets/b576a466-37fb-4ebd-b01a-3962545e3eab" />



 ## ✨ Features

*  View all cars in an organized table
*  Add new cars with details (make, model, year, VIN, engine, mileage, color, price, status, photo)
*  Update car details or replace photos
*  Delete cars from inventory
*  Search cars by model
*  Filter by **status** (Available / Sold)
*  Sort by **Price** (Low → High / High → Low) or **Year** (Newest → Oldest)
* 🖼 Upload & display car photos with fallback to "No Image"

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Database:** MySQL
* **Frontend:** Bootstrap 5, HTML, CSS, JavaScript
* **Other:** Jinja2 templates, Werkzeug for file uploads

---

## 📂 Project Structure
```
car_inventory_system/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── add_car.html
│   ├── view_cars.html
│   └── update_car.html
├── static/
│   ├── css/
│   └── images/
└── venv/
```




## ⚙️ Installation & Setup

1. **Clone the repo**

```bash
git clone https://github.com/SethumM03/Car-Inventory-System.git
cd Car-Inventory-System
```

2. **Set up a virtual environment** (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create MySQL database**

```sql
CREATE DATABASE car_dealership;

USE car_dealership;

CREATE TABLE cars (
    car_id INT AUTO_INCREMENT PRIMARY KEY,
    make VARCHAR(100),
    model VARCHAR(100),
    year INT,
    vin VARCHAR(100),
    engine VARCHAR(100),
    mileage INT,
    color VARCHAR(50),
    price DECIMAL(10,2),
    status VARCHAR(50),
    photo VARCHAR(255)
);
```

5. **Run the app**

```bash
python app.py
```

6. Open in your browser:
   👉 `http://127.0.0.1:5000/`

---

## 📸 Screenshots

<img width="1919" height="868" alt="Screenshot 2025-09-18 194715" src="https://github.com/user-attachments/assets/5186787e-0351-4268-a13e-0684a95cef8a" />

<img width="1919" height="864" alt="Screenshot 2025-09-18 195224" src="https://github.com/user-attachments/assets/9cb4656d-cab6-4d30-ac84-24bcabb8fdfc" />

<img width="1919" height="1055" alt="Screenshot 2025-09-18 195952" src="https://github.com/user-attachments/assets/77079d41-5ff5-41dd-881f-c82ed818e483" />

<img width="1919" height="1079" alt="Screenshot 2025-09-18 195419" src="https://github.com/user-attachments/assets/5ad8c31f-f305-4503-b96f-ec0b4f71c8cd" />





