# 🌆 Smart City Complaint Management System

An integrated Django web application that empowers citizens to raise complaints related to public infrastructure, utilities, and safety within a smart city initiative. The platform is modular, scalable, and can be used by municipal bodies to improve civic engagement and infrastructure responsiveness.

---

## 🧩 Modules / Django Apps

| App Name           | Purpose                                               |
|--------------------|--------------------------------------------------------|
| `complaint`         | Upload issues with images and geolocation             |
| `electricity`       | Report power cuts, faulty poles, and related issues   |
| `emergency`         | Urgent complaints (accidents, medical, fire)          |
| `mapdata`           | Handles location-based metadata or mapping visuals    |
| `road`              | Road damage, potholes, and construction complaints    |
| `waste_complaints`  | Specific UI for waste issues                          |
| `waste_management`  | Backend and processing for waste complaints           |
| `water_management`  | Water supply complaints and data handling             |
| `dashboard`         | Admin/authority dashboard to view & manage complaints |
| `smart_city`        | Main project settings and config                      |

---

## 🚀 Features

- 🖼️ Upload location-tagged images to report issues
- 📍 Auto-detect location using browser geolocation
- 📬 Planned: Automatic email routing to relevant govt. departments
- 🛠️ Modular structure for scalability
- 👤 User roles: Citizens, Authorities, Admins
- 📊 Dashboard for monitoring city-wide problems
- 🗑️ Domain-specific complaint tracking (Water, Road, Waste, Electricity, etc.)

---

## 🛠️ Technologies Used

- **Backend:** Django 5.2 (Python)
- **Frontend:** HTML5, Bootstrap
- **Database:** SQLite (can be replaced with PostgreSQL)
- **Others:** Geolocation API, Django Admin, File/Image uploads

---

## 📁 Directory Structure

