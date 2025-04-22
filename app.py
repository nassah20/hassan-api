from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students=[
        {"name": "asha nambari", "program": "Software Engineering"},
        {"name": "Hassan gombanila", "program": "Computer Science"},
        {"name": "shaibu said", "program": "Information Systems"},
        {"name": "mulhat malick", "program": "Software Engineering"},
        {"name": "shaban msanga", "program": "Health information science"},
        {"name": "zamda nambari", "program": "Cybersecurity"},
        {"name": "hawa hussein", "program": "Information system"},
        {"name": "juma ramadhan", "program": "Computer Engineering"},
        {"name": "Winnie peter", "program": "Software Engineering"},
        {"name": "samwel madembwe", "program": "Information Technology"}
    ])

@app.route('/subjects', methods=['GET'])
def get_subjects():
    return jsonify(subjects={
        "Year 1": [
            "Principles of Programming Languages(CP 111)",
            "Development Perspectives(DS 102)",
            "Mathematical Foundations of Information Security-(IA 112)",
            "Introduction to Information Technology(IT 111)",
            "Communication Skills(LG 102)",
            "Discrete Mathematics for ICT(MT1111)",
            "Calculus(MT 1112)",
            "Linear Algebra for ICT(MT 1117)",
            "Introduction to Computer Networking(CN 121)",
            "Introduction to Database systems(CP 121)",
            "Introduction to High Level Programming(CP 123)",
            "Introduction to Software Engineering(CS 123)",
            "Introduction to IT Security(IA 124)",
            "Numerical Analysis for ICT(MT 1211)",
            "Introduction to Probability and Statistics(ST 1210)"
        ],
        "Year 2": [
            "Computer Networking Protocols(CN 211)",
            "Introduction To Linux/Unix Systems(CP 211)",
            "Systems Analysis and Design(CP 212)",
            "Data Structures and Algorithms Analysis(CP 213)",
            "Computational Theory(CP 214)",
            "Object Oriented Programming in Java(CP 215)",
            "Industrial Practical Training I(CS 131)",
            "Computer Organization and Architecture I(CT 211)",
            "Internet Programming And Application I(CP 221)",
            "Open Source Technologies(CP 222)",
            "Object-Oriented Systems Design(CP 223)",
            "Database Management Systems(CP 224)",
            "Software Testing and Quality Assurance(CP 225)",
            "Operating Systems(CP 226)",
            "ICT Research Methods(IS 221)"
        ],
        "Year 3": [
            "Internet Programming and Applications II(CP 311)",
            "Python Programming(CP 312)",
            "Mobile Applications Development(CP 313)",
            "Selected Topics in Software Engineering(CP 316)",
            "Computer Graphics(CP 318)",
            "Industrial Practical Training II(CS 231)",
            "ICT Entrepreneurship(EME 314)",
            "Mathematical Logic and Formal Semantics(MT 3111)",
            "Distributed Database Systems(CP 321)",
            "Data Mining and Warehousing(CP 322)",
            "Web Framework Development Using Javascript(CP 323)",
            "Compiler Technology(CP 324)",
            "Advanced Java Programming(CS 321)",
            "Information and Communication Systems Security(IA 321)"
        ],
        "Year 4": [
            "ICT Project Management(BT 413)",
            "Distributed Computing(CP 314)",
            "C# Programming(CP 412)",
            "Industrial Practical Training III(CS 332)",
            "Software Reverse Engineering(CS 411)",
            "Software Engineering Project I(CS 431)",
            "Computer Maintenance(CT 312)",
            "Human Computer Interaction(IM 411)",
            "Professional Ethics and Conduct Core(SI 311)",
            "Software Deployment and Management(CS 421)",
            "Big Data Analysis(CS 329)",
            "Software Engineering Project II(CS 432)",
            "Artificial Intelligence(CP 422)",
            "System Administration and Management(CP 423)",
            "Cloud Computing(CP 424)",
            "Foundations of Data Science(CG 222)"
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
