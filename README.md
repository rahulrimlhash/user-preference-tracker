# Backend Service for User Preference Tracking

## Overview
This project is designed to track user interactions with posts and update user preferences based on those interactions. It includes the following features:  
- A `POST` API for recording user interactions.  
- A `GET` API for fetching user preferences.  
- Redis caching for optimizing data retrieval.  
- Logging for complete execution tracking.

---

## Setup Instructions  

### Prerequisites  
- Python 3.8 or higher  
- Redis server  
- Django framework
- Posgresql

### Step-by-Step Guide  

1. **Create a Virtual Environment**  
   - Navigate to the project directory in your terminal.  
   - Run the following command to create a virtual environment:  
     ```bash
     python -m venv venv
     ```  
   - Activate the virtual environment:  
     - On Windows:  
       ```bash
       venv\Scripts\activate
       ```  
     - On macOS/Linux:  
       ```bash
       source venv/bin/activate
       ```

2. **Install Dependencies**  
   - Install all required dependencies listed in `requirements.txt` using:  
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Redis**  
   - Install Redis on your system:  
     - On Ubuntu:  
       ```bash
       sudo apt update
       sudo apt install redis
       ```
     On Windows:  
       ```bash
       pip install redis
       ```  
     - On macOS:  
       ```bash
       brew install redis
       ```  
   - Start the Redis server and ensure it is running.  
   - Verify that the Redis server path matches the configuration in `settings.py`.  

4. **Run the Project**  
   - Start the Django development server:  
     ```bash
     python manage.py runserver
     ```

5. **Django Admin Panel Setup**  
   - Access the Django admin panel at: `http://127.0.0.1:8000/admin`.  
   - Create at least 5 users, posts, and tags.  

6. **Interact with APIs**  
   - Use the `POST` API to record user interactions: `/api/interaction`.  
   - Use the `GET` API to fetch user preferences: `/api/preferences`.  
   - Refer to the attached documentation for detailed API usage, including parameters and sample data.  

---

## Additional Notes  
- Ensure that the Redis server is running during API testing to utilize the caching mechanism.  
- Logging is enabled for tracking all actions, providing an audit trail for debugging and analysis.  

---

## Contact  
For any queries or issues, feel free to contact:  
**Rahul K.**  
**rahulrimlhash6@gmail.com**

