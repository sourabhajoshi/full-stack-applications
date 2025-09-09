# Project Structure

```angular2html
VueDRFMonorepo/
│── README.md                  # Repo-level README with project overview
│── requirements.txt            # Backend dependencies
│── package.json                # Frontend dependencies (Vue + Quasar + Pinia)
│── docker-compose.yml          # Optional: Run backend, frontend, DB together
│── .gitignore
│
├── backend/                    # Django REST Framework backend
│   ├── manage.py
│   ├── backend/                # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py             # Root URLs
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── apps/                   # Each app lives here
│   │   ├── authn/              # Authentication System
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py
│   │
│   │   ├── ecommerce/          # E-Commerce
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── views.py
│   │   │   ├── urls.py
│   │   │   └── tests.py
│   │
│   │   ├── chat/               # Chat + Video Calling
│   │   ├── hospital/           # Hospital Management System
│   │   ├── college/            # College / LMS
│   │   ├── fraud/              # Fraud Detection
│   │   ├── jobs/               # Job Board + Resume Builder
│   │   ├── iot/                # IoT Waste Management
│   │   ├── analytics/          # Social Media Analytics Dashboard
│   │   └── streaming/          # Video Streaming + Recommendation
│   │
│   ├── common/                 # Shared utils (middlewares, mixins)
│   │   ├── permissions.py
│   │   ├── helpers.py
│   │   └── decorators.py
│   │
│   ├── tests/                  # Global backend tests
│   │   └── test_setup.py
│   │
│   └── requirements/           # Split requirements (dev.txt, prod.txt)
│       ├── dev.txt
│       └── prod.txt
│
├── frontend/                    # Vue 3 + Quasar frontend
│   ├── quasar.conf.js
│   ├── package.json
│   ├── src/
│   │   ├── main.js             # App entry
│   │   ├── router/             # Vue Router
│   │   │   ├── index.js
│   │   │   └── routes.js
│   │   │
│   │   ├── stores/             # Pinia state management
│   │   │   ├── authn.js
│   │   │   ├── ecommerce.js
│   │   │   ├── chat.js
│   │   │   └── ...
│   │   │
│   │   ├── pages/              # Each app has its own folder
│   │   │   ├── Authn/
│   │   │   │   ├── Login.vue
│   │   │   │   ├── Register.vue
│   │   │   │   └── Profile.vue
│   │   │   ├── Ecommerce/
│   │   │   │   ├── ProductList.vue
│   │   │   │   ├── Cart.vue
│   │   │   │   └── Checkout.vue
│   │   │   ├── Chat/
│   │   │   ├── Hospital/
│   │   │   ├── College/
│   │   │   ├── Fraud/
│   │   │   ├── Jobs/
│   │   │   ├── IoT/
│   │   │   ├── Analytics/
│   │   │   └── Streaming/
│   │   │
│   │   ├── components/         # Shared components
│   │   │   ├── Navbar.vue
│   │   │   ├── Sidebar.vue
│   │   │   ├── Modal.vue
│   │   │   └── Loader.vue
│   │   │
│   │   ├── assets/             # Images, icons, styles
│   │   └── utils/              # API wrappers, formatters, helpers
│   │
│   └── tests/                  # Unit & e2e tests
│
├── docs/                        # Project documentation
│   ├── 01-authn.md
│   ├── 02-ecommerce.md
│   ├── 03-chat.md
│   └── ...
│
└── scripts/                     # Utility scripts
    ├── seed_users.py
    ├── seed_products.py
    └── reset_db.py

```
