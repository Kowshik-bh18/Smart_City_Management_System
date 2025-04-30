# 🏙️ Complaint Management System

This is a Django-based web application for citizens to report local issues by uploading images and automatically tagging their current location. The app is designed to assist smart city initiatives and allows government authorities to track, manage, and resolve complaints effectively.

---

## 🚀 Features

- 📷 Image Upload with Automatic Location Detection (Latitude & Longitude)
- 👥 User Authentication (Only logged-in users can submit complaints)
- 🔐 Access Control: Users can only edit or delete their own complaints
- 🌍 View complaint location on Google Maps
- 🛠️ Admin Panel to monitor all complaints
- 📬 **(Planned)** Auto-assignment of authority emails based on location
- ⏰ **(Planned)** Periodic email reminders for unresolved complaints
- ✅ **(Planned)** Manual and image-based complaint resolution tracking

---

## 🗂️ Tech Stack

- **Backend:** Django 5.2
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (default), can be upgraded to PostgreSQL
- **Other:** Geolocation API, Django Admin

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/complaint-app.git
cd complaint-app
