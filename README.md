# 🏏 IPL Stats API Service

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.26-013243?style=for-the-badge&logo=numpy&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)

> A RESTful API service built with Python and Flask that delivers comprehensive IPL cricket statistics — including batting, bowling, and team records — derived from **90,000+ ball-by-ball delivery records**.

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Endpoints](#-api-endpoints)
- [Frontend](#-frontend)
- [Sample Response](#-sample-response)
- [Author](#-author)

---

## ✨ Features

- 🏏 **Batting Analytics** — Runs, average, strike rate, 50s, 100s, highest score & more
- 🎯 **Bowling Analytics** — Wickets, economy, average, best figures & more
- 📊 **Team Records** — Win/loss record, titles won, head-to-head comparisons
- ⚔️ **Head to Head** — Compare any two IPL teams directly
- 🌐 **Interactive Frontend** — Search and view stats directly in browser
- 📡 **REST API** — Clean JSON responses for all endpoints

---

## 🛠 Tech Stack

| Technology | Usage |
|------------|-------|
| 🐍 Python | Core programming language |
| ⚗️ Flask | REST API framework |
| 🐼 Pandas | Data processing & analytics |
| 🔢 NumPy | Numerical computations |
| 🌐 HTML/CSS/JS | Frontend interface |
| 🔗 Flask-CORS | Cross-origin resource sharing |

---

## 📁 Project Structure

```
ipl-api-service/
│
├── app.py              # Flask application & API routes
├── ipl.py              # Team statistics logic
├── jugad.py            # Batting & bowling analytics
├── index.html          # Interactive frontend UI
├── matches.csv         # IPL match-level dataset
├── balls.csv           # Ball-by-ball delivery dataset
├── download_data.py    # Script to download datasets
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/satyanandpandey71-byte/ipl-api-service.git
cd ipl-api-service
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download the dataset**
```bash
python download_data.py
```

**4. Run the server**
```bash
python app.py
```

**5. Open the frontend**

Open `index.html` in your browser using Live Server or just double-click it.

> Server runs at: `http://127.0.0.1:5000`

---

## 📡 API Endpoints

### 🏠 Home
```
GET /
```
Returns a welcome message.

---

### 🏟️ All Teams
```
GET /api/teams
```
Returns list of all IPL teams.

---

### 📊 Team Record
```
GET /api/team-record?team=Mumbai Indians
```
Returns overall win/loss record and record against every other team.

| Parameter | Type | Description |
|-----------|------|-------------|
| `team` | string | Full team name |

---

### ⚔️ Head to Head
```
GET /api/teamVteam?team1=Mumbai Indians&team2=Chennai Super Kings
```
Returns head-to-head match record between two teams.

| Parameter | Type | Description |
|-----------|------|-------------|
| `team1` | string | First team name |
| `team2` | string | Second team name |

---

### 🏏 Batting Record
```
GET /api/batting-record?batsman=RG Sharma
```
Returns complete batting statistics for a player.

| Parameter | Type | Description |
|-----------|------|-------------|
| `batsman` | string | Player name |

**Returns:** Innings, Runs, Average, Strike Rate, 50s, 100s, Highest Score, Fours, Sixes, MOM awards & stats vs each team.

---

### 🎯 Bowling Record
```
GET /api/bowling-record?bowler=JJ Bumrah
```
Returns complete bowling statistics for a player.

| Parameter | Type | Description |
|-----------|------|-------------|
| `bowler` | string | Player name |

**Returns:** Innings, Wickets, Economy, Average, Strike Rate, Best Figure, 3-wicket hauls, MOM awards & stats vs each team.

---

## 🖥️ Frontend

The project includes a sleek, dark-themed frontend with tabs for:

- 🏏 All Teams
- 📊 Team Record
- ⚔️ Head to Head
- 🏏 Batting Stats
- 🎯 Bowling Stats
- 📡 API Docs

Simply open `index.html` with Live Server while Flask is running.

---

## 📦 Sample Response

**GET** `/api/batting-record?batsman=RG Sharma`

```json
{
  "RG Sharma": {
    "all": {
      "innings": 221,
      "runs": 5879,
      "avg": 30.30,
      "strikeRate": 129.89,
      "fifties": 40,
      "hundreds": 1,
      "highestScore": "109*",
      "fours": 519,
      "sixes": 240,
      "mom": 18
    },
    "against": {
      "Chennai Super Kings": {
        "innings": 31,
        "runs": 770,
        "avg": 27.5,
        "strikeRate": 125.40
      }
    }
  }
}
```

---

## 👨‍💻 Author

**Satyanand Pandey**

[![GitHub](https://img.shields.io/badge/GitHub-satyanandpandey71--byte-181717?style=for-the-badge&logo=github)](https://github.com/satyanandpandey71-byte)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ and 🏏 by Satyanand Pandey</p>
