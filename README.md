
# **Doctor Plus (Telemedicine Platform)**

A comprehensive **telemedicine platform** enabling **real-time video consultations** and **medical record management**. Built with **Django, WebRTC, jQuery, JavaScript, WebSocket, and AWS**, it ensures a secure, scalable, and user-friendly healthcare experience.

---

## **Table of Contents**  
1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Installation and Setup](#installation-and-setup)  
4. [Configuration](#configuration)  
5. [Usage](#usage)  
6. [Testing](#testing)  
7. [Deployment](#deployment) 

---

## **Features**  
- **Real-time Video Consultations:** Conduct interactive sessions via **WebRTC** with seamless video and audio streaming.  
- **Medical Record Management:** Store and access patient records, prescriptions, and reports securely.  
- **Role-based Access Control:** Separate dashboards for doctors, patients, and administrators.  
- **WebSocket-based Notifications:** Real-time alerts for appointments and messages.  
- **Integrated Frontend and Backend:** Simple and cohesive development using Django, jQuery, and JavaScript.  
- **Cloud Integration:** Store medical files in **AWS S3** and deploy backend on **EC2** for scalability.  

---

## **Tech Stack**  
- **Backend:** Python, Django  
- **Frontend:** JavaScript, jQuery  
- **Real-time Communication:** WebRTC, WebSocket  
- **Cloud Services:** AWS S3, EC2  
- **Database:** PostgreSQL/MySQL  
- **Authentication:** Django's built-in authentication with JWT  

---

## **Installation and Setup**  
### Prerequisites  
- Python 3.x  
- PostgreSQL/MySQL  
- AWS account for cloud services  

### Setup Instructions  
1. **Clone the repository:**  
   ```bash
   git clone <repository-url>  
   cd telemedicine-platform  
   ```

2. **Create and activate a virtual environment:**  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # For Linux/Mac  
   venv\Scripts\activate     # For Windows  
   ```

3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt  
   ```

4. **Configure the database and environment variables:**  
   - Update the `DATABASES` section in `settings.py`.  
   - Create a `.env` file in the root directory and add keys:  
     ```bash
     DATABASE_URL=<database-url>  
     SECRET_KEY=<django-secret-key>  
     AWS_ACCESS_KEY=<aws-access-key>  
     AWS_SECRET_KEY=<aws-secret-key>  
     ```

5. **Run migrations:**  
   ```bash
   python manage.py makemigrations  
   python manage.py migrate  
   ```

6. **Collect static files:**  
   ```bash
   python manage.py collectstatic  
   ```

7. **Start the Django server:**  
   ```bash
   python manage.py runserver  
   ```

---

## **Configuration**  
1. **WebRTC Configuration:**  
   - Ensure the WebSocket server is set up for signaling.  
   - Configure **STUN/TURN servers** to support peer-to-peer communication.

2. **AWS Configuration:**  
   - Set up an **S3 bucket** for storing patient files.  
   - Use **EC2** instances for hosting the backend in production.  

---

## **Usage**  
- **Patients:** Register, schedule appointments, and access prescriptions.  
- **Doctors:** Manage consultations, view patient records, and conduct video calls.  
- **Administrators:** Monitor activities and manage user accounts.  

---

## **Testing**  
Run the tests to ensure all components are functioning:  
```bash
python manage.py test  
```

---

## **Deployment**  
1. **Backend Deployment on AWS EC2:**  
   - Configure the instance with necessary dependencies.  
   - Use **Gunicorn** and **Nginx** for production deployment.  

2. **Static Files Hosting:**  
   - Store static assets on **S3** for optimized performance.  

## **Contact**  
For further queries or support, reach out to:  
**Zaakir Hussain**  
Email: [mail.zaakir.hussain@gmail.com](mailto:mail.zaakir.hussain@gmail.com)  
