def get_input():
    students = []
    for _ in range(5):
        student_id = input("학번: ")
        name = input("이름: ")
        english = int(input("영어: "))
        c_language = int(input("C-언어: "))
        python = int(input("파이썬: "))
        students.append([student_id, name, english, c_language, python])
    return students

def calculate_total_and_average(students): # 학생들의 총점과 평균을 계산하는 함수
    for student in students:
        total = sum(student[2:5])
        average = round(total / 3,2)
        student.extend([total, average])
    return students

def calculate_grade(students): # 학생들의 학점을 계산하는 함수
    for student in students:
        average = student[5]
        if average >= 95:
            grade = 'A+'
        elif average >= 90:
            grade = 'A'
        elif average >= 85:
            grade = 'B+'
        elif average >= 80:
            grade = 'B'            
        elif average >= 75:
            grade = 'C+'
        elif average >= 70:
            grade = 'C'
        elif average >= 75:
            grade = 'D+'
        elif average >= 70:
            grade = 'D'
        else:
            grade = 'F'
        student.append(grade)
    return students

def calculate_rank(students): # 학생들의 등수를 계산하는 함수
    students.sort(key=lambda x: x[5], reverse=True) # 총점을 기준으로 내림차순 정렬
    for i, student in enumerate(students, start=1): # 등수를 계산하여 추가
        student.append(i) 
    return students

def print_results(students): # 학생들의 정보를 출력하는 함수
    print("성적관리 프로그램")
    print("=============================================================================")
    print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=============================================================================")
    for student in students:
        print("\t".join(str(x) for x in student))

def count_students(students): # 평균이 80점 이상인 학생 수를 계산하는 함수
    count = sum(1 for student in students if student[6] >= 80)
    print(f"평균이 80점 이상인 학생수: {count}")

students = get_input()
students = calculate_total_and_average(students)
students = calculate_grade(students)
students = calculate_rank(students)
print_results(students)
count_students(students)