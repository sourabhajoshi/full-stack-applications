# Full-Stack Project Roadmap (Vue 3 + Quasar + Django REST Framework)  

This repository contains 10 full-stack applications built with Vue 3 (Quasar) on the frontend and Django REST Framework on the backend.

Each project focuses on **different problem domains** and introduces **new sub-techs** to cover real-world scenarios.

---

## Project List

## 1. Authentication System
**Features**
- JWT login, register, logout  
- Profile management  
- Role-based access (admin, user, manager)  

**Skills**
- DRF SimpleJWT authentication  
- Pinia store for tokens  
- Vue Router guards  

**Sub-techs**
- Refresh tokens  
- Role-based permissions middleware  

## 2. E-Commerce Platform
**Features**
- Product catalog & search  
- Cart, checkout, and order history  
- User reviews & ratings  
- Admin dashboard  

**Skills**
- DRF ViewSets & filtering  
- Vue 3 forms & validation  
- State management for cart  

**Sub-techs**
- Stripe/PayPal integration  
- Redis caching for products  
- Recommendation engine (basic ML)  

## 3. Chat + Video Calling App
**Features**
- Real-time chat (1:1 and groups)  
- File sharing in chat  
- Notifications (browser & in-app)  
- Video calling with WebRTC  

**Skills**
- Django Channels (WebSockets)  
- Vue state management for live updates  
- WebRTC peer connections  

**Sub-techs**
- Push notifications  
- Chat persistence in PostgreSQL  

## 4. Hospital Management System
**Features**
- Manage patients, doctors, and appointments  
- Role-based dashboards (doctor, nurse, admin)  
- Medical record tracking  

**Skills**
- Secure data modeling in DRF  
- Role-based serializers & permissions  
- Vue forms & validation  

**Sub-techs**
- Audit logs  
- Role-based dashboards  

## 5. College / Learning Management System
**Features**
- Course creation & enrollment  
- Video and file uploads  
- Progress tracking  
- Paid/free courses  

**Skills**
- DRF file uploads  
- Role-based authentication (student, instructor)  
- Vue Router navigation  

**Sub-techs**
- Video storage in S3/Cloud  
- Payment integration  
- Progress tracking models  

## 6. Fraud Detection System
**Features**
- Transaction ingestion  
- Anomaly detection alerts  
- Fraud detection dashboard  

**Skills**
- DRF for transaction APIs  
- ML anomaly detection (Scikit-learn/TensorFlow)  
- Vue alert system  

**Sub-techs**
- Celery for async detection tasks  
- Redis for caching transactions  

## 7. Job Board + Resume Builder
**Features**
- Job postings & applications  
- Search & filter jobs  
- Resume upload & parsing  
- Resume builder with PDF export  

**Skills**
- File handling in DRF  
- PDF generation (ReportLab/WeasyPrint)  
- Vue form builder  

**Sub-techs**
- Full-text search (Elasticsearch/Postgres)  
- Async resume parsing  

## 8. IoT Waste Management
**Features**
- IoT sensor data ingestion  
- Bin fill-level tracking  
- Map visualization of bins  

**Skills**
- DRF APIs for IoT devices  
- Vue map integration (Leaflet/Mapbox)  
- Real-time sensor updates  

**Sub-techs**
- MQTT or REST ingestion  
- Celery for batch data processing  

## 9. Social Media Analytics Dashboard
**Features**
- OAuth integration with Twitter, GitHub, LinkedIn  
- Data aggregation & visualization  
- Scheduled data refresh  

**Skills**
- OAuth 2.0 in DRF  
- Chart libraries in Vue (Recharts/D3.js)  
- Aggregation queries in PostgreSQL  

**Sub-techs**
- Celery for periodic API fetch  
- Redis for caching results

## 10. Video Streaming + Recommendation Platform
**Features**
- Video upload & streaming (HLS/Dash)  
- Comments & likes  
- Recommendation engine  

**Skills**
- DRF file uploads  
- Vue video player integration  
- ML recommendation logic  

**Sub-techs**
- FFmpeg + Celery for transcoding  
- CDN integration for streaming  

---

## Tech Stack

**Frontend**  
- Vue 3 (Composition API)  
- Quasar Framework (UI Components)  
- Pinia (State Management)  
- Axios (API Calls)  
- Recharts / D3.js (Charts)  

**Backend**  
- Django 5 + Django REST Framework  
- Django Channels (WebSockets)  
- Celery (Async tasks)  
- Redis (Cache + Broker)  
- PostgreSQL (Database)  

**Other Tools**  
- Docker & Docker Compose  
- GitHub Actions (CI/CD)  
- Nginx + Gunicorn (Deployment)  
- S3/Cloud Storage (Media & Videos)  

---

## Projects Overview

| #  | Project | Features | Skills | Sub-techs |
|----|---------|----------|--------|-----------|
| 1  | Authentication System | JWT login, register, roles, profile | DRF SimpleJWT, Vue route guards, Pinia auth store | Refresh tokens, role-based permissions |
| 2  | E-Commerce Platform | Catalog, cart, checkout, reviews, admin | DRF ViewSets, Vue forms, cart state management | Stripe/PayPal, Redis cache, ML recommendations |
| 3  | Chat + Video Calling | Real-time chat, file sharing, notifications, WebRTC | Django Channels, Vue live updates, WebRTC | Push notifications, PostgreSQL persistence |
| 4  | Hospital Management System | Patients, doctors, appointments, records | Secure DRF models, role-based serializers | Audit logs, dashboards |
| 5  | College / LMS | Courses, enrollment, uploads, tracking | DRF file uploads, role-based auth | S3/Cloud storage, payments |
| 6  | Fraud Detection System | Transactions, anomaly alerts | DRF APIs, ML anomaly detection | Celery workers, Redis cache |
| 7  | Job Board + Resume Builder | Job posts, resume upload & parsing, PDF builder | File handling, PDF generation | Elasticsearch search, async parsing |
| 8  | IoT Waste Management | Sensor data ingestion, bin fill levels, maps | DRF APIs, Vue maps (Leaflet/Mapbox) | MQTT ingestion, Celery batch jobs |
| 9  | Social Media Analytics Dashboard | OAuth API integration, charts, scheduled refresh | OAuth, DRF aggregation, Vue charts | Celery for periodic jobs, caching |
| 10 | Video Streaming + Recommendation | Video upload/streaming, comments, rec engine | DRF file uploads, Vue video player, ML | FFmpeg + Celery transcoding, CDN |

## Learning Outcomes
By completing these 10 apps, you will:  
- Master **Vue 3 (Quasar)** → state management, forms, real-time UIs  
- Master **Django REST Framework** → auth, async, file handling, caching  
- Learn **DevOps practices** → Docker, CI/CD, deployment, monitoring  
- Gain experience in **sub-techs** → Payments, WebRTC, ML APIs, FF

