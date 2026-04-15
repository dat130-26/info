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
    - [Score Table](#score-table)
    - [Idea followed          | 5 |](#idea-followed-----------5-)
    - [How to Run works         | 3 |](#how-to-run-works----------3-)
    - [Log in and register users | 5 |](#log-in-and-register-users--5-)
    - [Example data | 2 |](#example-data--2-)
    - [JS Form validation | 5 |](#js-form-validation--5-)
    - [Sort and search in JS | 3 |](#sort-and-search-in-js--3-)
    - [Sort stored | 3 |](#sort-stored--3-)
    - [\>5 Tables | 6 |](#5-tables--6-)
    - [Complex queries | 3 |](#complex-queries--3-)
    - [Insert, Update, delete data | 6 |](#insert-update-delete-data--6-)
    - [AJAX request used | 5 |](#ajax-request-used--5-)
    - [Dynamic layout | 2 |](#dynamic-layout--2-)
    - [Semantic tags | 2 |](#semantic-tags--2-)
    - [Code separation | 4 |](#code-separation--4-)
    - [Best practice routes | 5 |](#best-practice-routes--5-)
    - [Server side validation | 4 |](#server-side-validation--4-)
    - [Errors handled and displayed | 5 |](#errors-handled-and-displayed--5-)
    - [Authentication | 4 |](#authentication--4-)
    - [Access control | 3 |](#access-control--3-)
    - [Extra feature | 25 |](#extra-feature--25-)
      - [CSS Features example:](#css-features-example)
      - [JavaScript Features example:](#javascript-features-example)
      - [Python features](#python-features)
      - [Vector database](#vector-database)
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
Presentations will be scheduled on June 10th, 11th, and 12th.
All group members must be present for the presentation.
Since some exchange students will no longer be in the country, we offer you a chance to deliver your project early and present it in May.

When doing the optional delivery, you cannot change your project afterward.

## Assignments

All members of the group need to have passed the assignments. Students who did not pass the assignments cannot participate in the project.

## Overview

For the exam project, you are required to design and implement a complete web application, frontend and backend.

You are free to choose what kind of application you implement, but restrictions apply to both the [technology that you may use](#technology-allowed) and there is some [required functionality](#functional-requirements).

You have to finalize the idea for your application by the [idea deadline](#idea) and show and answer questions about your implementation in person at the [presentation](#presentation).

## Collaboration requirements

Both group members need to contribute.

You should use git and your group's GitHub repository to actively collaborate and coordinate your work.

If one member does less than 30% of the commits on GitHub, he/she may fail in the project.

## Feedback and meeting

Leander is available for meetings to give feedback, discuss your project, and help with any technical difficulties. I recommend that every group asks for feedback on their project idea at least once.

Book a meeting using [this link](https://outlook.office.com/bookwithme/user/90a9d200a112481b8677a71c1ab2a195@uis.no/meetingtype/q1YLgJWHFkmBl0VtgX-_ig2?anonymous&ismsaljsauthenabled&ep=mlink).

*Some people see wrong meeting times, due to wrong time-zone settings. All meetings are between 12:30 and 16:00.*

## Idea

You already proposed a project idea in Assignment 0.
You can update or change that project idea until 6th of May.
The project idea only needs to be a very general, e.g. a chat application, or a minesweeper game.
If your final page does not adhere to the project idea, points will be deducted.

## Project delivery

On the final delivery, you should hand in your complete code and a README.md markdown file.
Your code should also include a SQL script that creates your database and inserts example data.

The `README.md` file should contain the following sections:

- How to run: e.g.
    > Run the `setup.sql` script to create the database.
    > Update the database root user's password in `app.py`.
    > Start the application by running `app.py` in the application folder.
- Instructions for testing, e.g., `username` and `password` for existing users.
- List of all functionality: List all implemented functionality, to make sure all your work is taken into account. For example
  - Dark mode is stored in local storage and is present if the user revisits the page.
  - New categories can be added on the category pages.
    - An Icon and color can be chosen for the category.
  - If the user tries to register a password with fewer than 5 characters, an Error is displayed.

## Technology Allowed

You need to use the technology from the course, i.e., **MySQL**, **Flask**, and vanilla JavaScript (no JS framework).
You may only use the frameworks listed below. If you are unsure if something is allowed, please ask on Discord.

### Backend

Your web server should be Flask. Data should be stored in a MySQL database.
You may use the Flask-login plugin, but that is not required. If you do so, note it in your README.md.
You should write SQL queries.
Do not use an Object-Relational-Mapper or SQLAlchemy.
You cannot use Flask-forms, wtforms, Flask-WTF, or similar.

### Frontend

The frontend should be vanilla JS.
You may use the Lodash JS library.
You may use all built-in JS APIs.

You are not allowed to use a JS Framework like React, Vue, or similar.

You may use additional JS libraries to implement extra functionality, e.g., to display graphs or similar.
Ask on Discord, and mention what is used and for what in your README.

### Layout Requirements

You should use plain CSS. 
If you copy CSS files from the web, e.g., `reset.css` or `normalize.css`, you must specify this in the README.md. If specified, it will not count as plagiarism.

## Functional Requirements

Some features of your application are required. 
For example, your application must include login, registration of new users, and sort and search functionality.

The required functionality is reflected in the criteria below. The main criteria make up 75% of the grade, via points shown below. 
Additionally, you can collect up to 25 points for additional features. See below for examples.

### Score Table

| Criteria | pts |
| --------------------- | --- |
| Idea followed          | 5 |
| How to Run works         | 3 |
| Log in and register users | 5 |
| Example data | 2 |
| JS Form validation | 5 |
| Sort and search in JS | 3 |
| Sort stored | 3 |
| >5 Tables | 6 |
| Complex queries | 3 |
| Insert, Update, delete data | 6 |
| AJAX request used | 5 |
| Dynamic layout | 2 |
| Semantic tags | 2 |
| Code separation | 4 |
| Best practice routes | 5 |
| Server side validation | 4 |
| Errors handled and displayed | 5 |
| Authentication | 4 |
| Access control | 3 |
| Extra feature | 25 |

### Idea followed          | 5 |

The application follows the idea from assignment 0.

### How to Run works         | 3 |

The `README.md` contains sufficient and working explanation how to run the project.

### Log in and register users | 5 |

It is possible to log in with an existing user and register new users.

### Example data | 2 |

The page contains example data, e.g. existing users with data.

### JS Form validation | 5 |

User input forms are validated in JavaScript, to help the user fill forms correctly.
Full points require that checks are actually performed in JS (not just using HTML attributes) and that errors are nicely displayed.

### Sort and search in JS | 3 |

It should be possible to sort and search some part of the data. Sort and search should be implemented in JS using JS as source of truth.

### Sort stored | 3 |

Sorting should be stored, so data is still sorted in the same order, when a user returns.

### >5 Tables | 6 |
The database contains at least 5 tables with primary and foreign keys.

### Complex queries | 3 |
The application uses complex queries, including 
`JOIN` and `GROUP BY`.

### Insert, Update, delete data | 6 |

The application's operations insert, update, and delete data, affecting data in all tables.

### AJAX request used | 5 |

The application contains at least one AJAX request, where this makes sense.

### Dynamic layout | 2 |

The page layout is dynamic, adjusting to both wide and medium size screens.

### Semantic tags | 2 |

The HTML uses semantic tags.
Try to use them extensively, where possible.

### Code separation | 4 |

Both JS and Python code is meaningfully separated into multiple files.

### Best practice routes | 5 |

Route names follow best practice.
Where routes do not fit into best practice principles, explain this in comments.

### Server side validation | 4 |

Validate input on server side. 
Check for malformed or missing input.

### Errors handled and displayed | 5 |

Errors are caught, and shown to the client including appropriate error codes.

### Authentication | 4 |

Proper authentication on routes that require login.

### Access control | 3 |

Ensure access control or authorization for data that is not accessible to all users.



### Extra feature | 25 |

You can gain up to 25 additional points for extra features.
However, you can get at most 12 points for features implemented in JavaScript and at most 12 points for backend (python) features, 5 points for CSS features, and up to 10 points for integrating a Vector database.

Examples are taken from previous projects in the Web Programming course. Examples that require learning additional technology are marked with *

#### CSS Features example:

Adjustment to phone size screen layout.
To get 5 points here, adjustment must be significant.

#### JavaScript Features example:
Some examples of extra features implemented in JS are

- Game running in JS, e.g. Yatzy, Minesweeper, Sudoku or other.
- Additional use of AJAX beyond a single request.

- *Display of graphs
- *Dynamic update subscription via long polling or websockets (e.g receive chat messages)
- *Image upload and preview

#### Python features

- Game logic, or application logic implemented in backend
- Calls to third party API
  
- *Email authorization
- *Dynamic update subscription via long polling or websockets (e.g receive chat messages)
- *Advanced login via Flask Login, JWT tokens or similar
- *Image storage and validation

#### Vector database 

The application uses a vector database to store and search texts.
The vector database should contain at least 100 texts.
It should be possible to search the texts using user input.
Any vector database of your choice might be used.

## Presentation

Each group has to present their project. 
In the presentation, you have to show the running code, and answer questions about the code.

Presentations will be scheduled on June 10th, 11th and 12th.
All group members have to be present in the presentation. Failure to meet up for the presentation will result in not passing the course.

If you have a doctor's certificate, showing that you could not attend the presentation, we will arrange a later date.

You have to be able to explain your code on a technical level. 
For example, if you use the `forEach` method in JavaScript, you should be able to explain:
> `forEach` is a method on an Array. It takes a function (*callback function*) as argument and executes the *callback function* once for each element in the array. The element is given to the *callback function* as argument.
