# Exam project

- [Exam project](#exam-project)
  - [Dates](#dates)
  - [Optional delivery](#optional-delivery)
  - [Assignments](#assignments)
  - [Overview](#overview)
  - [Collaboration requirements](#collaboration-requirements)
  - [Feedback and meeting](#feedback-and-meeting)
  - [Idea](#idea)
  - [Project delivery](#project-delivery)
  - [Technology Allowed](#technology-allowed)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Layout Requirements](#layout-requirements)
  - [Functional Requirements](#functional-requirements)
  - [Presentation](#presentation)


## Dates

| Date   |                               |                    |
| ------ | ----------------------------- | ------------------ |
| 15.04. | Start                         |                    |
| 06.05. | Idea                          | **deadline**       |
| 20.05. | Early Code delivery           | optional           |
| 22.05. | Early delivery presentation 1 | optional           |
| 28.05. | Early delivery presentation 2 | optional           |
| 07.06. | Code                          | **deadline** 23:59 |
| 10.06. | Presentation                  | **in person**      |
| 11.06. | Presentation                  | **in person**      |
| 12.06. | Presentation                  | **in person**      |

## Optional delivery

You have to present your project in person. 
Presentations will be sheduled on June 10th, 11th and 12th.
All group members have to be present in the presentation. 
Since some exchange students will no longer be in the country, we offer you a chance to deliver your project on the early delivery and present in May.

When doing the optional delivery, you cannot change your project afterwards.

## Assignments

All members of the group need to have passed the assignments. Students that did not pass assignments cannot participate in the project.

## Overview

For the exam project you are required to design and implement a complete web application, frontend and backend.

You are free to chose what kind of application you implement, but restrictions apply to both [technology that you may use](#technology-allowed) and there is some [required functionality](#functional-requirements).

You have to fix, the idea of your application until the [idea deadline](#idea) and have to show and answer questions about your application in person at the [presentation](#presentation)

## Collaboration requirements

Both group members need to contribute.

You should use git and your groups GitHub repository to actively collaborate and coordinate your work.

If one member does less than 30% of the commits on GitHub, he may be failed in the project.

## Feedback and meeting

Leander will be available for meetings to give feedback, discuss your project and help with any technical difficulties. I recommend that every group asks for feedback on their project idea at least once.

## Idea

You already proposed a project idea in Assignment 0.
You can update or change that project idea until 6th of May.
The project idea only needs to be a very general, e.g. a chat application, or a minesweeper game.
If your final page does not adhere to the project idea points will be deducted.


## Project delivery

On the final delivery you should hand in your complete code, and a README.md markdown file.
Your code should also include a SQL script that creates your database, and inserts example data.

The `README.md` file should contain the following sections:

- How to run: e.g.
    > Run the `setup.sql` script to create the database.
    > Update the database root users password in `app.py`.
    > Start the application by running `app.py` in the application folder.
- Instructions for testing, e.g. `username` and `password` for existing users.
- List of all functionality: List all implemented functionality, to make sure all your work is taken into account. For example
  - Dark mode is stored in local storage and present if the user revisits the page.
  - New categories can be added on the category pages.
    - An Icon and color can be chosen for the category.
  - If the user tries to register a password with less than 5 characters, an Error is displayed.

## Technology Allowed

You need to use the technology from the course, i.e. **MySQL**, **Flask**, and vanilla JavaScript (no JS framework).
You may only use the frameworks listed below. If you are unsure if something is allowed, please ask on Discord.

### Backend

Your web server should be Flask. Data should be stored in an MySQL database.
You may use the Flask-login plugin, but that is not required. If you do so, note it in your README.md.
You should write SQL queries.
Do not use an Object-Relational-Mapper or SQLAlchemy.
You cannot use Flask-forms, wtforms, Flask-WTF or similar.

### Frontend

The frontend should be vanilla JS.
You may use the Lodash JS library.
You may use all built-in JS APIs.

You are not allowed to use JS Framework like React, Vue or similar.

You may use additional JS libraries for achieving extra functionality, e.g. showing graphs, or similar.
Ask on discord, and mention what is used and for what in your README.

### Layout Requirements

You should use plain CSS. 
If you copy CSS files from the web, e.g. `reset.css` or `normalize.css`, you must specify this in the README.md. If specified, it will not count as plagiarism.

## Functional Requirements

Mostly your project need to have features mostly already covered in the assignments. 
Additionally, you will receive points for extra features.
*More details and examples for extra features will be provided next week.*

## Presentation

Each group has to present their project. 
In the presentation, you have to show the running code, and answer questions about the code.

Presentations will be shedules on June 10th, 11th and 12th.
All group members have to be present in the presentation. Failure to meet up for the presentation will result in not passing the course.

If you have a doctors certificate, showing that you could not attend the presentation, we will arrange a later date.

You have to be able to explain your code on a technical level.
For example, if you use the `forEach` method in JavaScript, you should be able to explain:
> `forEach` is a method on a Array. It takes a function (*callback function*) as argument and executes the *callback function* once for each element in the array. The element is given to the *callback function* as argument.