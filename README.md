#

# Emotion-Based Diary Web Application 🌸

This project is an **Emotion-Based Diary Web Application** that allows users to log in, create diary entries, and receive emotion-specific motivational messages. Built with **Flask** and **SQLite**, the app provides a simple, user-friendly interface, styled in a baby pink theme with a "Read Me When" emotion-based feature for positivity and motivation.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup & Installation](#setup--installation)
5. [Running the Application](#running-the-application)
6. [Docker Image Instructions](#docker-image-instructions)
7. [Application Structure](#application-structure)
8. [Usage Guide](#usage-guide)
9. [Screenshots](#screenshots)
10. [Future Improvements](#future-improvements)
11. [Author & Acknowledgments](#author--acknowledgments)

---

## Project Overview

This application enables users to:
- **Register** and **Log in** securely
- **Write and store diary entries**
- **Receive motivational notes** based on their emotions, which can be selected on the "Read Me When" page
- **Log out** securely

The app is containerized using Docker, allowing easy deployment and ensuring consistency across different environments.

---

## Features

- **User Authentication**: Register, log in, and log out functionality.
- **Diary Entries**: Users can write and view personal diary entries.
- **Emotion Jar**: A motivational message generator based on user-selected emotions, including options for "Happy," "Sad," "Anxious," "Depressed," and "Angry."
- **Responsive Design**: Aesthetic baby pink theme with a responsive layout.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Styling**: CSS
- **Containerization**: Docker

---

## Setup & Installation

### Prerequisites

- **Docker** installed on your system
- **Python 3.9+** installed, if running without Docker

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/diary-app.git
    cd diary-app
    ```

2. **Install Dependencies** (if running without Docker):
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Docker image**
    https://hub.docker.com/r/eshemafzal/django-flask




## Running the Application

### Option 1: Using Docker

1. **Build the Docker Image**:
    ```bash
    docker build -t diary_app .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -p 5000:5000 diary_app
    ```

3. **Access the App**:
   Open your browser and go to `http://localhost:5000`.

### Option 2: Running Locally (Without Docker)

1. **Initialize the Database**:
   Run `init_db.py` to create tables and add default data:
    ```bash
    python init_db.py
    ```

2. **Run the Flask Application**:
    ```bash
    flask run
    ```

3. **Access the App**:
   Open your browser and go to `http://localhost:5000`.

---

## Docker Image Instructions

### Pushing the Image to Docker Hub

To push the Docker image to Docker Hub:

1. **Tag the Image**:
    ```bash
    docker tag diary_app yourdockerusername/diary_app:latest
    ```

2. **Log In to Docker Hub**:
    ```bash
    docker login
    ```

3. **Push the Image**:
    ```bash
    docker push yourdockerusername/diary_app:latest
    ```

---

## Application Structure

```
diary-app/
├── app.py                # Main application file
├── init_db.py            # Script to initialize the database
├── Dockerfile            # Docker setup
├── models.py             # Database models for User, DiaryEntry, and PositiveNote
├── templates/            # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── my_diary.html
│   └── jar.html          # Emotion Jar template
├── static/               # Static files (CSS, images)
│   └── styles.css
└── README.md             # Project documentation
```

---

## Usage Guide

1. **Register**: Create an account to access the application.
2. **Login**: Enter your credentials to enter your personal diary.
3. **Add Diary Entry**: Use the "Add Note" page to log a new diary entry.
4. **View Past Entries**: View previous diary entries on the "My Diary" page.
5. **Select an Emotion**: Go to "Open Jar" and choose an emotion to receive a motivational message.
6. **Logout**: Use the "Logout" button to end the session securely.

---

## Screenshots

1. **Login Page**: Simple login interface with baby pink theme.
   
![image](https://github.com/user-attachments/assets/081b1821-b7e0-4335-b3c2-4039f6bebd60)



   
3. **Register Page**: Easy-to-follow registration form

   ![image](https://github.com/user-attachments/assets/60157a0b-a7ce-4875-baf0-a63e2deb694c)

5. **Diary Page**: Page to add and view diary entries.

   ![image](https://github.com/user-attachments/assets/454bc964-5247-452d-bbbe-3294fac2f0ba)

7. **Emotion Jar**: Motivational quotes based on emotions, with options like Happy, Sad, Anxious, Depressed, and Angry.


![image](https://github.com/user-attachments/assets/1101ef9b-ae62-4584-9f4f-95004ffe6b98)


---

## Future Improvements

- **Database Integration for Emotion Notes**: Currently, notes are hardcoded. Future implementations could store notes in the database.
- **Advanced UI Design**: Add animations or transition effects for improved user experience.
- **Additional Features**: Expand the Emotion Jar to include more emotions and categories of motivational messages.

---

## Tem members for Assignment

**Developed by**: 1. Muhammad QASIM 221026
                  2. Esham Afzal 221008
                  3. Aisha Munir 221014





---

