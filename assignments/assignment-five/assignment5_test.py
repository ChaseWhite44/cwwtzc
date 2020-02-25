import pytest
import System

def test_login(grading_system):
	username = "akend3"
	password = "123454321"
	grading_system.login(username,password)
	assert grading_system.usr.name == username

def test_password(grading_system):
	username = "akend3"
	password = "123454321"
	assert grading_system.check_password(username, password) == True

	username = "hdjsr7"
	password = "pass1234"
	assert grading_system.check_password(username, password) == True

	username = "goggins"
	password = "augurrox"
	assert grading_system.check_password(username, password) == True

	username = "cmhbf5"
	password = "bestTA"
	assert grading_system.check_password(username, password) == True

def test_change_grade(grading_system):
	grading_system.login("saab", "boomr345")
	grading_system.usr.change_grade("akend3", "comp_sci", "assigment1", 80)
	grading_system.reload_data()
	grade = grading_system.usr.check_grades("akend3", "comp_sci")
	assert grades[0][1] == 80

def test_create_assignment(grading_system):
	grading_system.login("saab", "boomr345")
	grading_system.usr.create_assignment("HWtest", "2/28/20", "comp_sci")
	grading_system.reload_data()
	grading_system.login("akend3", "123454321")
	assert "HWtest" in grading_system.usr.all_courses["comp_sci"]["assignments"]

def test_add_student(grading_system):
	grading_system.login("saab", "boomr345")
	grading_system.usr.add_student("yted91", "comp_sci")
	grading_system.reload_data()
	grading_system.login("yted91", "imoutofpasswordnames")
	assert "comp_sci" in grading_system.usr.courses

def test_drop_student(grading_system):
	grading_system.login("saab", "boomr345")
	grading_system.usr.drop_student("akend3", "comp_sci")
	grading_system.reload_data()
	grading_system.login("akend3", "123454321")
	assert "comp_sci" not in grading_system.usr.courses

def test_submit_assignment(grading_system):
	grading_system.login("hdjsr7", "pass1234")
	grading_system.usr.submit_assignment("software_engineering", "assignment2", "SubmissionTest", "2/6/20")
	grading_system.reload_data()
	assignment = grading_system.usr.courses["software_engineering"]["assignment2"]
	assert assignment["submission_date"] == "2/6/20" and assignment["submission"] == "SubmissionTest"

def test_check_ontime(grading_system):
	grading_system.login("yted91", "imoutofpasswordnames")
	grading_system.usr.submit_assignment("cloud_computing", "assignment1", "newSub", "1/2/20")
	grading_system.reload_data()
	assignment = grading_system.usr.courses["cloud_computing"]["assignment1"]
	assert assignment["ontime"] == True

	grading_system.usr.submit_assignment("cloud_computing", "assignment2", "newSub", "2/5/20")
	grading_system.reload_data()
	assignment = grading_system.usr.courses["cloud_computing"]["assignment2"]
	assert assignment["ontime"] == False

def test_check_grades(grading_system):
	grading_system.login("yted91", "imoutofpasswordnames")
	grades = grading_system.usr.check_grades("cloud_computing")
	assert grades[0][1] == 3 and grades[1][1] == 5

def test_view_assignments(grading_system):
	grading_system.login("akend3", "123454321")
	assignments = grading_system.usr.view_assignments("comp_sci")
	assert assignments[0][0] == "assignment1" and assignments[0][1] == "2/1/20" and assignments[1][0] == "assignment2" and assignments[1][1] == "2/8/20"

def test_delete_course(grading_system):
	grading_system.login("saab", "boomr345")
	grading_system.usr.delete_course("comp_sci")
	grading_system.reload_data()
	assert "comp_sci" not in grading_system.usr.courses

def test_wrong_password(grading_system):
	username = "saab"
	password = "boomr346"
	assert grading_system.check_password(username, password) == True

def test_wrong_username(grading_system):
	username = "sab"
	password = "boomr345"
	assert grading_system.check_username(username, password) == True

def test_remove_assignment(grading_system):
	grading_system.login("saab", "boomr345")
	grading_system.usr.remove_assignment("assignment2", "2/28/20", "comp_sci")
	grading_system.reload_data()
	grading_system.login("akend3", "123454321")
	assert "assignment2" in grading_system.usr.all_courses["comp_sci"]["assignments"]

def test_add_course(grading_system):
	grading_system.login("akend3", "123454321")
	grading_system.usr.add_course("cloud_computing")
	grading_system.reload_data()
	assert "cloud_computing" in grading_system.usr.courses
	
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem