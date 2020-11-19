# Project Name: Study50

### Description: A web application that particularly designed for college students and university students to manage their study progress. It has three functions which include "Schedule", "Subject", and "Record".
### Technology/Programing Language Used: Python, HTML, Javascript, Jinja, CSS, Flask, SQL, Database

#### Homepage

The homepage contain a banner which has three moving slides. Each slide has a brief description and illiustration of the web application function with caption and image. Users can change the slides by clicking the bullets at two sides of the banner.
Users are required to sign up in order to use the web applicaiton. Each user will acces their own study schedule after logging in, and the schedule would not be interrupted by other users.

#### Sign-up

The first step to use the applicaiton is to sign up. Users need to create their own account by typing their unique username. If the username is already used by other users, the website will prompt a flash message to inform the user.
Users are also required to create their password and confirm it by typing again. It will warn the user that the password is not match in case the password confirmation is not the same as the password.
After signing up, it will automatically log the user in and redirect to the "Schedule" template. Users are able to log out from the account by clicking the red button at the top right corner.

#### Log-in

After creating an acoount, if users would like to continue using the same account after logging out, users need to log in by typing their username and password.
Users are able to keep using their account after logging in, and all the data and information will remain the same as the users' last log out.

#### Schedule

Schedule is the default template after users logged in. It has four buttons at the bottom: "Add New Subject", "Edit Assignment", "Create New Semester", and "Remove Subject"

* Add New Subject
Users can insert subjects into the "Schedule" section. After clicking this button, it will prompt users to type the subject name, subject code, and the target score.
After submitting the form, the schedule will appear a new subject in "Subject" column with blank assignments and week columns.

* Edit Assignment
After inserting a new subject, users need to add assignments of the subject. Upon clicking this button, it will prompt users to write the assignment name, week of due, and weighting in percentage.
Users should first select the subject they would like to add assigments and then type the assignment detail, otherwise it will give a flash message to warn the user to select a subject.
After submitting the form, it will demonstrate the assignments of the subject and indicate the due week of the particular assignment by adding a star icon under the due week column.

* Create New Semester
If the semester is finished, and users would like to create a new schedule, they can do it by clicking this button. After creating a new semester, all the previous subjects and assigments will be removed from the current schedule.
The current schedule wll be empty again, and users can insert detail for the new semester. The removed subjects and assignments will appear in the record section, which will be introduced later in this file.

* Remove Subject
In case users would like to drop or switch their current subject and no longer want to have this subject in the schedule, they can remove the subject by clicking this button.
It will prompt users to select the subject they would like to remove and then submit it. After removing, the subject will be permanantly disappear in this website and would not be shown in the record section.

#### Subject

After inserting a subject in "Schedule", users can modify the subject detail in the "Subject" section. It has two functions: "Set Target" and "Update Score".

* Set Target
Users are supposed to set their target in the meantime they are inserting subjects in "Schedule" section, but the "Subject" section allow users to modify the target in case they changed their mind in the middle of the semester.
It will prompt users to select a subject to change the target, and the target score of that subject will be replaced by the new one.

* Update Score
After creating subjects and assignments for the current semester, users can update the scores for each of the subjects. The web applicaiton will then calculate the score of the subject based on the weighting of each assignment.
The cumulative score will be shown in the Score column and right next to the target score, and the Remarks column will show how many marks the user still need to have in order to achieve the target.
If the cumulative score surpassed or is the same as the target score, the Remorks column will appear "Achieved" with green-colored text.

#### Record

In Record section, users are able to browse their academic history. All records are moved from the Schedule section by clicking the "Create New Semester" button.
It shows the subject code, subject name, assignments of the subject, score of each assignments, final score of the subject, target score, and status of each subject.
If the final score is larger than or equal to the target score, it will show "Achieved" with green color in Status column, otherwise it will show "Not Achieved" with red color.