from flask import Flask, request, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False
app.json.sort_keys = False

# Dữ liệu mẫu (Sample Data)
SAMPLE_DATA = {
    "students": [
        {
            "student_id": "SV001",
            "name": "Nguyen Hoang Xuan Bach",
            "age": 19,
            "gender": "male"
        },
        {
            "student_id": "SV002",
            "name": "Nguyen Hong Gam",
            "age": 24,
            "gender": "female"
        },
        {
            "student_id": "SV001",
            "name": "Nguyen Hoang Xuan Bach",
            "age": 19,
            "gender": "male"
        },
        {
            "student_id": "SV001",
            "name": "Nguyen Hoang Xuan Bach",
            "age": 19,
            "gender": "male"
        },
        {
            "student_id": "SV003",
            "name": "Pham Hoang Sang",
            "age": 20,
            "gender": "male"
        }
    ]
}

@app.route('/', methods=['GET', 'POST'])
def register_students():
    if request.method == 'POST' and request.is_json:
        data = request.get_json()
    else:
        data = SAMPLE_DATA

    if 'students' not in data or not isinstance(data['students'], list):
        return jsonify({
            "status": "error", 
            "message": "Dữ liệu thiếu trường \"students\" hoặc sai định dạng danh sách."
        }), 400

    raw_list = data['students']
    student_groups = {}

    for st in raw_list:
        required_fields = ["student_id", "name", "age", "gender"]
        if not all(key in st for key in required_fields):
            return jsonify({"status": "error", "message": f"Thiếu thông tin: {st}"}), 400
        
        if not isinstance(st['age'], int):
            return jsonify({"status": "error", "message": f"Sai tuổi: {st}"}), 400

        s_id = st['student_id']
        if s_id not in student_groups:
            student_groups[s_id] = []
        student_groups[s_id].append(st)

    duplicate_list = []
    eligible_list = []

    for s_id, group in student_groups.items():
        if len(group) > 1:
            duplicate_list.extend(group[1:])
        
        first_student = group[0]
        if first_student['age'] < 23:
            eligible_list.append(first_student)

    response = {
        "status": "success",
        "message": "Danh sách đã được xử lý thành công.",
        "total_students": len(raw_list),
        "total_duplicates": len(duplicate_list),
        "duplicate_students": duplicate_list,
        "students_eligible_for_free_ticket": eligible_list
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)