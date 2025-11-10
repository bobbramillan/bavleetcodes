courses = {
    "CS 164": [],
    "CS 171": [],
    "CS 172": [{"course": "CS 171", "min_grade": "C"}],
    "CS 265": [{"course": "CS 172", "min_grade": "C"}],
    "CS 260": [{"course": "CS 265", "min_grade": "B"}],
    "CS 270": [{"course": "CS 172", "min_grade": "B"}],
    "CS 300": [
        {"course": "CS 265", "min_grade": "B"},
        {"course": "CS 270", "min_grade": "C"}
    ]
}


course_info = {
    "CS 164": {
        "title": "Introduction to Computer Science",
        "description": "Covers basic programming concepts, algorithms, and problem-solving techniques using Python.",
        "credits": 3
    },
    "CS 171": {
        "title": "Computer Systems",
        "description": "Introduction to computer architecture, data representation, and low-level programming concepts.",
        "credits": 3
    },
    "CS 172": {
        "title": "Data Structures",
        "description": "Covers linked lists, trees, graphs, and algorithm analysis. Focus on design and implementation efficiency.",
        "credits": 4
    },
    "CS 265": {
        "title": "Algorithms",
        "description": "Design and analysis of algorithms including sorting, searching, dynamic programming, and graph algorithms.",
        "credits": 3
    },
    "CS 260": {
        "title": "Advanced Programming Techniques",
        "description": "Focuses on software design patterns, debugging, performance optimization, and modular development.",
        "credits": 3
    },
    "CS 270": {
        "title": "Database Systems",
        "description": "Introduction to relational databases, SQL, and data modeling concepts.",
        "credits": 3
    },
    "CS 300": {
        "title": "Machine Learning Fundamentals",
        "description": "Foundational concepts in machine learning including supervised learning, feature engineering, and model evaluation.",
        "credits": 3
    }
}
