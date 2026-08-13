from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["portfolio"]

projects = db["projects"]

project = {
    "title": "BMI Calculator",
    "description": "A BMI calculator project built with Python.",
    "technologies": ["Python"],
    "category": "app",
    "image": "img/portfolio/img2.png",
    "github": "https://github.com/Aminbasirzad/bmi_calculator"
}

