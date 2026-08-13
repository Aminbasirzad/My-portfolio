from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["portfolio"]

projects = db["projects"]

project = {
    "title": "Django Online Store",
    "description": "A Online store built with Django for managing projects, users, and orders",
    "technologies": ["Python", "Django", "HTML", "CSS", "Bootstrap"],
    "category": "app",
    "image": "img/portfolio/img1.png",
    "github": "https://github.com/Aminbasirzad/Shop"
}
