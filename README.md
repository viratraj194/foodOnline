<div align="center">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_Maps-4285F4?style=for-the-badge&logo=google-maps&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />

  <br/>
  <h1>🍕 FoodOnline Marketplace</h1>
  <p><strong>A Premium Multi-Vendor Food Ordering System with Geolocation Features</strong></p>
  
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#installation">Installation</a> •
  <a href="#logic">Business Logic</a>
</div>

---

## 📖 Overview
**FoodOnline** is a high-end multi-vendor marketplace where restaurant owners (vendors) can register, manage their menus, and receive orders, while customers can find nearby restaurants based on their precise location using Google Maps Geolocation.

## 🚀 Key Features

### 📍 Location-Based Search (Radius Logic)
- **Geolocation:** Uses Google Maps API to fetch the user's current location.
- **Proximity Search:** Customers can search for food within a specific radius (e.g., 15km). The system calculates the distance between the customer and listed restaurants using the **Haversine formula**.

### 🏗 Multi-Vendor System
- **Vendor Onboarding:** Restaurants can register and wait for Admin approval.
- **Menu Management:** Vendors have a private dashboard to manage Categories and Food Items (with images and pricing).
- **Business Hours:** Dynamic opening/closing time management.

### 🛒 Ordering & Cart
- **AJAX Cart:** Add/Remove items without page refreshes (built with jQuery).
- **Tax Calculation:** Dynamic tax calculation based on location/category.
- **Secure Checkout:** Integration for seamless ordering.

### 🔐 Security & Auth
- **Gmail SMTP Integration:** Secure user registration with email activation links.
- **Role-Based Access:** Distinct permissions for Customers and Vendors.

---

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Python & Django Framework |
| **Database** | PostgreSQL (Production-ready relational DB) |
| **Frontend** | HTML5, CSS3, JavaScript, jQuery (AJAX) |
| **APIs** | Google Maps (Place Autocomplete, Distance Matrix) |
| **Authentication** | Django Custom User Model + Gmail SMTP |

---

## ⚙️ How It Works (The Core Logic)

1. **User Registration:** Users sign up and receive a verification email via Gmail.
2. **Profile Completion:** Vendors must upload their business license and location data.
3. **The Marketplace:** When a customer searches for "Pizza," the backend queries the **PostgreSQL** database and filters restaurants by distance using the coordinates stored during vendor registration.
4. **Ordering:** The cart logic is handled asynchronously using **jQuery AJAX**, updating the database and the UI simultaneously.

---

## 🚀 Installation & Setup

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/viratraj194/FoodOnline.git](https://github.com/viratraj194/FoodOnline.git)
   cd FoodOnline
