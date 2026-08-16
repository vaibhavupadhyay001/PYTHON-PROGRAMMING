import json
from pathlib import Path

import streamlit as st


# =========================================================
# CONFIG
# =========================================================

DATABASE = "school_data.json"

DEFAULT_DATA = {
    "students": [],
    "Teachers": []
}


# =========================================================
# DATABASE
# =========================================================

def load_data():
    path = Path(DATABASE)

    if not path.exists():
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA.copy()

    try:
        with open(path, "r") as f:
            content = f.read().strip()

            if not content:
                return DEFAULT_DATA.copy()

            data = json.loads(content)

            # Make sure required keys exist
            data.setdefault("students", [])
            data.setdefault("Teachers", [])

            return data

    except (json.JSONDecodeError, OSError):
        return DEFAULT_DATA.copy()


def save_data(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)


data = load_data()


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="School Management System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background: #0b1120;
        color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* ---------- SIDEBAR ---------- */

    section[data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }

    section[data-testid="stSidebar"] h1 {
        color: #f8fafc;
    }

    /* ---------- HEADINGS ---------- */

    .main-title {
        font-size: 38px;
        font-weight: 800;
        margin-bottom: 5px;
        color: #f8fafc;
    }

    .subtitle {
        color: #94a3b8;
        font-size: 16px;
        margin-bottom: 30px;
    }

    /* ---------- CARDS ---------- */

    .stat-card {
        background: linear-gradient(
            135deg,
            #111827,
            #172033
        );

        border: 1px solid #263244;
        border-radius: 16px;

        padding: 22px;

        min-height: 140px;

        box-shadow: 0 8px 25px rgba(0,0,0,0.20);
    }

    .stat-title {
        color: #94a3b8;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .stat-value {
        color: #f8fafc;
        font-size: 32px;
        font-weight: 800;
    }

    .stat-description {
        color: #64748b;
        font-size: 13px;
        margin-top: 5px;
    }

    /* ---------- SECTION CARD ---------- */

    .section-card {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
    }

    /* ---------- PROFILE ---------- */

    .profile-card {
        background: linear-gradient(
            135deg,
            #111827,
            #1e293b
        );

        border: 1px solid #334155;
        border-radius: 18px;

        padding: 25px;

        margin-top: 15px;
    }

    .profile-name {
        font-size: 26px;
        font-weight: 800;
        color: #f8fafc;
    }

    .profile-role {
        color: #60a5fa;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .profile-info {
        color: #cbd5e1;
        margin: 8px 0;
    }

    /* ---------- BUTTONS ---------- */

    .stButton > button {
        border-radius: 10px;
        font-weight: 600;
        min-height: 42px;
    }

    /* ---------- INPUTS ---------- */

    input, textarea {
        border-radius: 9px !important;
    }

    /* ---------- TABLE ---------- */

    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
    }

    /* ---------- DIVIDER ---------- */

    hr {
        border-color: #1f2937;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def validate_email(email):
    return "@" in email and "." in email


def find_student(roll_no):
    for student in data["students"]:
        if student["roll_no"] == roll_no:
            return student

    return None


def find_teacher(emp_id):
    for teacher in data["Teachers"]:
        if teacher["emp_id"] == emp_id:
            return teacher

    return None


def calculate_average(grades):
    if not grades:
        return 0

    return sum(grades.values()) / len(grades)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <h1 style="font-size:25px;">
            🎓 School Admin
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:#64748b;'>Management Dashboard</p>",
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Register Student",
            "Register Teacher",
            "Manage Grades",
            "Student Details",
            "Teacher Details"
        ]
    )

    st.divider()

    st.markdown(
        f"""
        <div style="
            background:#0f172a;
            padding:15px;
            border-radius:12px;
            border:1px solid #1e293b;
        ">
            <div style="color:#94a3b8;font-size:12px;">
                SYSTEM STATUS
            </div>

            <div style="
                color:#4ade80;
                font-weight:700;
                margin-top:5px;
            ">
                ● Online
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# DASHBOARD
# =========================================================

if page == "Dashboard":

    st.markdown(
        '<div class="main-title">School Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Overview of your students, teachers and academic records.</div>',
        unsafe_allow_html=True
    )

    students_count = len(data["students"])
    teachers_count = len(data["Teachers"])

    total_subjects = sum(
        len(student.get("grades", {}))
        for student in data["students"]
    )

    averages = [
        calculate_average(student.get("grades", {}))
        for student in data["students"]
        if student.get("grades")
    ]

    overall_average = (
        sum(averages) / len(averages)
        if averages
        else 0
    )

    # ---------- STATS ----------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">TOTAL STUDENTS</div>
                <div class="stat-value">{students_count}</div>
                <div class="stat-description">
                    Registered students
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">TOTAL TEACHERS</div>
                <div class="stat-value">{teachers_count}</div>
                <div class="stat-description">
                    Registered teachers
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">SUBJECT RECORDS</div>
                <div class="stat-value">{total_subjects}</div>
                <div class="stat-description">
                    Grade entries
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="stat-card">
                <div class="stat-title">AVG PERFORMANCE</div>
                <div class="stat-value">{overall_average:.1f}</div>
                <div class="stat-description">
                    Overall average marks
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # ---------- RECENT STUDENTS ----------

    st.subheader("Students")

    if data["students"]:

        student_rows = []

        for student in data["students"]:

            grades = student.get("grades", {})

            student_rows.append({
                "Name": student["name"],
                "Roll No": student["roll_no"],
                "Age": student["age"],
                "Email": student["email"],
                "Subjects": len(grades),
                "Average": round(
                    calculate_average(grades),
                    2
                )
            })

        st.dataframe(
            student_rows,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No students registered yet.")


# =========================================================
# REGISTER STUDENT
# =========================================================

elif page == "Register Student":

    st.markdown(
        '<div class="main-title">Register Student</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Add a new student to the school database.</div>',
        unsafe_allow_html=True
    )

    with st.form("student_registration"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Full Name",
                placeholder="Enter student's name"
            )

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=100,
                value=18
            )

        with col2:

            email = st.text_input(
                "Email",
                placeholder="student@example.com"
            )

            roll_no = st.text_input(
                "Roll Number",
                placeholder="e.g. CS24001"
            )

        submitted = st.form_submit_button(
            "Register Student",
            use_container_width=True
        )

        if submitted:

            name = name.strip()
            email = email.strip()
            roll_no = roll_no.strip()

            if not name or not email or not roll_no:

                st.error("Please fill all fields.")

            elif not validate_email(email):

                st.error("Please enter a valid email address.")

            elif find_student(roll_no):

                st.error(
                    "A student with this roll number already exists."
                )

            else:

                data["students"].append(
                    {
                        "name": name,
                        "age": age,
                        "email": email,
                        "roll_no": roll_no,
                        "grades": {}
                    }
                )

                save_data(data)

                st.success(
                    f"Student {name} registered successfully!"
                )


# =========================================================
# REGISTER TEACHER
# =========================================================

elif page == "Register Teacher":

    st.markdown(
        '<div class="main-title">Register Teacher</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Add a new teacher to the school database.</div>',
        unsafe_allow_html=True
    )

    with st.form("teacher_registration"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Full Name",
                placeholder="Enter teacher's name"
            )

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=25
            )

            email = st.text_input(
                "Email",
                placeholder="teacher@example.com"
            )

        with col2:

            subject = st.text_input(
                "Subject",
                placeholder="e.g. Mathematics"
            )

            emp_id = st.text_input(
                "Employee ID",
                placeholder="e.g. EMP1001"
            )

        submitted = st.form_submit_button(
            "Register Teacher",
            use_container_width=True
        )

        if submitted:

            name = name.strip()
            email = email.strip()
            subject = subject.strip()
            emp_id = emp_id.strip()

            if not all([name, email, subject, emp_id]):

                st.error("Please fill all fields.")

            elif not validate_email(email):

                st.error("Please enter a valid email address.")

            elif find_teacher(emp_id):

                st.error(
                    "A teacher with this employee ID already exists."
                )

            else:

                data["Teachers"].append(
                    {
                        "name": name,
                        "age": age,
                        "email": email,
                        "subject": subject,
                        "emp_id": emp_id
                    }
                )

                save_data(data)

                st.success(
                    f"Teacher {name} registered successfully!"
                )


# =========================================================
# MANAGE GRADES
# =========================================================

elif page == "Manage Grades":

    st.markdown(
        '<div class="main-title">Manage Grades</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Add or update academic marks for students.</div>',
        unsafe_allow_html=True
    )

    if not data["students"]:

        st.warning("No students are registered yet.")

    else:

        roll_numbers = [
            student["roll_no"]
            for student in data["students"]
        ]

        selected_roll = st.selectbox(
            "Select Student",
            roll_numbers
        )

        student = find_student(selected_roll)

        if student:

            st.markdown(
                f"""
                <div class="profile-card">

                    <div class="profile-name">
                        {student["name"]}
                    </div>

                    <div class="profile-role">
                        Roll No: {student["roll_no"]}
                    </div>

                    <div class="profile-info">
                        📧 {student["email"]}
                    </div>

                    <div class="profile-info">
                        🎂 Age: {student["age"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            with st.form("grade_form"):

                col1, col2 = st.columns(2)

                with col1:

                    subject = st.text_input(
                        "Subject",
                        placeholder="e.g. Data Structures"
                    )

                with col2:

                    marks = st.number_input(
                        "Marks",
                        min_value=0.0,
                        max_value=100.0,
                        value=0.0,
                        step=0.5
                    )

                submitted = st.form_submit_button(
                    "Save Grade",
                    use_container_width=True
                )

                if submitted:

                    subject = subject.strip()

                    if not subject:

                        st.error("Please enter a subject.")

                    else:

                        student["grades"][subject] = marks

                        save_data(data)

                        st.success(
                            f"{subject} grade saved successfully!"
                        )

            if student["grades"]:

                st.subheader("Current Grades")

                grade_rows = [
                    {
                        "Subject": subject,
                        "Marks": marks
                    }
                    for subject, marks
                    in student["grades"].items()
                ]

                st.dataframe(
                    grade_rows,
                    use_container_width=True,
                    hide_index=True
                )

                avg = calculate_average(
                    student["grades"]
                )

                st.metric(
                    "Student Average",
                    f"{avg:.2f}"
                )


# =========================================================
# STUDENT DETAILS
# =========================================================

elif page == "Student Details":

    st.markdown(
        '<div class="main-title">Student Details</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Search and view complete student information.</div>',
        unsafe_allow_html=True
    )

    if not data["students"]:

        st.info("No students registered yet.")

    else:

        roll_numbers = [
            student["roll_no"]
            for student in data["students"]
        ]

        roll_no = st.selectbox(
            "Select Roll Number",
            roll_numbers
        )

        student = find_student(roll_no)

        if student:

            avg = calculate_average(
                student.get("grades", {})
            )

            st.markdown(
                f"""
                <div class="profile-card">

                    <div class="profile-name">
                        {student["name"]}
                    </div>

                    <div class="profile-role">
                        STUDENT
                    </div>

                    <div class="profile-info">
                        <b>Roll Number:</b>
                        {student["roll_no"]}
                    </div>

                    <div class="profile-info">
                        <b>Age:</b>
                        {student["age"]}
                    </div>

                    <div class="profile-info">
                        <b>Email:</b>
                        {student["email"]}
                    </div>

                    <div class="profile-info">
                        <b>Average Marks:</b>
                        {avg:.2f}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            st.subheader("Grades")

            if student["grades"]:

                grade_rows = []

                for subject, marks in student["grades"].items():

                    grade_rows.append(
                        {
                            "Subject": subject,
                            "Marks": marks
                        }
                    )

                st.dataframe(
                    grade_rows,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.info("No grades have been added yet.")


# =========================================================
# TEACHER DETAILS
# =========================================================

elif page == "Teacher Details":

    st.markdown(
        '<div class="main-title">Teacher Details</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Search and view teacher information.</div>',
        unsafe_allow_html=True
    )

    if not data["Teachers"]:

        st.info("No teachers registered yet.")

    else:

        employee_ids = [
            teacher["emp_id"]
            for teacher in data["Teachers"]
        ]

        emp_id = st.selectbox(
            "Select Employee ID",
            employee_ids
        )

        teacher = find_teacher(emp_id)

        if teacher:

            st.markdown(
                f"""
                <div class="profile-card">

                    <div class="profile-name">
                        {teacher["name"]}
                    </div>

                    <div class="profile-role">
                        TEACHER
                    </div>

                    <div class="profile-info">
                        <b>Employee ID:</b>
                        {teacher["emp_id"]}
                    </div>

                    <div class="profile-info">
                        <b>Age:</b>
                        {teacher["age"]}
                    </div>

                    <div class="profile-info">
                        <b>Email:</b>
                        {teacher["email"]}
                    </div>

                    <div class="profile-info">
                        <b>Subject:</b>
                        {teacher["subject"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )