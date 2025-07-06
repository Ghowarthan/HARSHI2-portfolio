from flask import Flask, render_template, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/profile')
def get_profile():
    profile = {
        "name": "Harshitha Vatturi",
        "title": "Computer Science Engineering Student",
        "location": "Chennai, India",
        "email": "harshithavatturi@gmail.com",
        "phone": "+91 8680005999",
        "linkedin": "linkedin.com/in/vatturiharshitha",
        "period": "2021–2025",
        "gpa": "8.8/10",
        "roles": [
            "UI/UX Designer",
            "Kotlin Developer", 
            "IEEE Published Author"
        ],
        "passions": [
            "UI/UX Design", "Mobile Development", "IoT", "Machine Learning"
        ],
        "skills": {
            "programming": ["Python", "Kotlin", "Angular", "JSON"],
            "design": ["Figma", "UI/UX Design", "Wireframing", "Prototyping"],
            "tools": ["MS Office", "Social Media Management", "Market Research"],
            "soft_skills": ["Communication", "Leadership", "Event Coordination", "Stakeholder Management", "Cross-Functional Collaboration"]
        },
        "projects": [
            {
                "title": "Business Enquiry Email Parsing Bot",
                "description": "Automated email parsing system that boosted workflow efficiency by 75%",
                "tech": ["Python", "JSON", "Automation"],
                "year": "2024",
                "link": "#"
            },
            {
                "title": "KSN Construction Company Website",
                "description": "Designed customer-facing web platform to enhance trust and visibility",
                "tech": ["Angular", "UI/UX Design", "Web Development"],
                "year": "2023",
                "link": "#"
            },
            {
                "title": "IoT Safety Device for Women & Children",
                "description": "Engineered a smart safety device using IoT technology to improve user safety",
                "tech": ["IoT", "Hardware", "Safety Technology"],
                "year": "2023",
                "link": "#"
            }
        ],
        "publications": [
            {
                "title": "Smartwatch-Powered Vehicle Navigation On Unmapped Terrain",
                "journal": "IEEE - 2024 Third International Conference on Smart Technologies and Systems for Next Generation Computing (ICSTSN)",
                "year": "2024",
                "doi": "10.1109/ICSTSN61422.2024.10670946"
            },
            {
                "title": "Mental Health Harmony: Insights from the Machine Learning Frontier",
                "journal": "IEEE",
                "year": "2024",
                "doi": "IEEE Publication"
            },
            {
                "title": "Detection of Potholes Using CNN",
                "journal": "EasyChair Publications",
                "year": "2023",
                "doi": "EasyChair Publication"
            }
        ],
        "experience": [
            {
                "company": "Central Metro Railway Ltd. (CMRL)",
                "role": "UI/UX Designer & Kotlin Developer",
                "description": "UI redesign, Kotlin development, cross-team communication",
                "period": "0-6 months"
            },
            {
                "company": "Vikatan",
                "role": "UX Designer & Digital Strategist",
                "description": "UX optimization, digital strategy, ad automation",
                "period": "0-6 months"
            }
        ],
        "contact": {
            "email": "harshithavatturi@gmail.com",
            "phone": "+91 8680005999",
            "linkedin": "linkedin.com/in/vatturiharshitha",
            "location": "Chennai, India"
        }
    }
    return jsonify(profile)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)