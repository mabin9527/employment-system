# Employment System

![Am I Responsive](static/images/am-i-responsive.png)

**Developer: Bin Ma**

💻 [Visit live website](https://employment-system.herokuapp.com/)


## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

The Employment System is an online platform where users can manage employees. In case the viewer needs permission to get access to the other pages, the username and password for the login are Andy 1234. The viewer can then edit or delete it.
<hr>

### User Goals

- To set up the admin's account
- To be able to view edit and delete departments' title 
- To be able to view edit and delete employees' information
- To be able to search employees' detail 

### Site Owner Goals

- To provide a solution to allow users to create admin account to manage employee
- To provide a well-structured online platform with a simple operation interface
- Provide a modern application with a search function
- Fully responsive and accessible
<hr>


## User Experience

### Target Audience
- The HR wants to manage the company's employees easily
- The owner of the company would like to acquire updated information about employees
- The department manager wishes to know the employee list in their department

### User Requirements and Expectations

- Fully responsive
- Accessible
- Simple operation interface

##### Back to [top](#table-of-contents)<hr>


## User Experience

### Target Audience
- Users that wish to book a table for a meal or a party with family and friends
- Past and new customers for the business
- Tourists visiting the area that are looking for a meal or a drink or both
- Fans visiting the area for a sports event or a music concert
- People employed in the area to eat and drink after work

### User Requirements and Expectations

- Fully responsive
- Accessible
- A welcoming design
- Social media
- Contact information
- Accessibility

##### Back to [top](#table-of-contents)<hr>


## User Stories

### Users

1.	As a User I can navigate across the site so that I can move to each feature of the site easily
2.	As a User I can log in and logout the website 
3.	As a User I can edit and delete employees' information
4.	As a User I can view all employee detail in one certain department
5.	As a User I can set up an account for new employee

### Site Owner  
6. As a Site Owner, I can provide a fully responsive site for my customers so that they have a good user experience
7. As a Site Owner, I can validate data entered into my site so that all submitted data is correct to avoid errors
8. As a Site Owner, I can provide a site where users can manage easily

##### Back to [top](#table-of-contents)<hr>

## Design

### Colors

I chose a light grey as the nav-bar background color and an extremely clean white color as the background color. The text color would be normal black. Because as an online working platform, the HR or employees' attention should not be abstracted by the colorful design. 

The colors I wanted to stay close to  [Coolors.co](https://coolors.co/)
<details><summary>See colour pallet</summary>
<img src="static/images/colors.png">
</details>

### Fonts

 The fonts selected were from Google Fonts, Montserrat wits sans-serif as a backup font.


#### Website pages

The site was designed for the user to be familiar with the classic office applications such as a navigation bar along the top of the pages and a hamburger menu button for smaller screens. Besides, the operation interface is easy to learn which will save plenty of time and costs for the owner. Because it is not necessary to train new employees on how to use this platform.

- The site consists of the following pages:
  - The login page allows the user to get access to the platform
  - The admin page shows the admin's username 
  - The admin edit page allows the user to update the admin's username and password saved from the database
  - The department page displays the current consist of departments in the company
  - The employee page can be used to add, edit and delete employee detail

 #### Database

- Built with Python and the Django framework with a database of a Postgres for the deployed Heroku version(production)
- The database ER diagram and table show all the fields stored in the database

<details><summary>Show diagram</summary>
<img src="static/images/ER-diagram.png">
</details>
<details><summary>Show table</summary>
<img src="static/images/table.png">
</details>


### Wireframes
The wireframes were created using Balsamiq
<details><summary>Wireframes</summary>
<img src="static/images/wireframes/login.png">
<img src="static/images/wireframes/admin.png">
<img src="static/images/wireframes/depart.png">
<img src="static/images/wireframes/employee.png">
</details>


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django

##### Back to [top](#table-of-contents)


## Features

### Login page
- The login page includes an input form that allows the user to type in username and password to get access to the main page. The submit button sends the form data to the backend. 

<details><summary>See feature images</summary>

![Login page](static/images/features/login.png)
</details>

### Navigation
- Fully Responsive
- On small screens switches to the hamburger menu
- Show the current user's name
- Logout the site
- Displayed on all pages

<details><summary>See feature images</summary>

![Navigation](static/images/features/nav-bar.png)
![Logout](static/images/features/logout.png)
</details>

### Footer
- Contains copyright
- Displayed across all pages

<details><summary>See feature images</summary>

![Footer](static/images/features/footer.png)
</details>

### Admin
- Displayed all admin's username
- Allow users to add new admin, edit and delete exist admin
- Allow users to search for relevant information

<details><summary>See feature images</summary>

![Admin](static/images/features/admin.png)
</details>

### Add New Admin
- Allow users to add new admin

<details><summary>See feature images</summary>

![Admin](static/images/features/admin-add.png)
</details>

### Edit Admin
- Show the existing information of the admin
- Allow users to update existing information of the admin

<details><summary>See feature images</summary>

![Admin](static/images/features/admin-edit.png)
</details>

### Delete Admin
- Allow user to delete the selected admin from database
- The warning box reminds the user of the importance of data

<details><summary>See feature images</summary>

![Admin](static/images/features/warning-box.png)
</details>

### Department
- Displayed all current company departments
- Allow users to add new departments, edit and delete existing department
- Search functions

<details><summary>See feature images</summary>

![Department](static/images/features/depart.png)
</details>

### Add New Department Title
- Allow users to add new department title

<details><summary>See feature images</summary>

![Department](static/images/features/depart-add.png)
</details>

### Employee
- Displayed all current company employees
- Allow users to add new employees, edit and delete existing employees
- Search functions

<details><summary>See feature images</summary>

![Employee](static/images/features/employee.png)
</details>

### Add New Employees
- Allow users to add new employees

<details><summary>See feature images</summary>

![Employee](static/images/features/employee-add.png)
</details>

### Pagination
- Add self-defined pagination class
- Pagination is used on the admin, department and employee pages
- Ensures the page is kept tidy as 10 items are displayed per page
- Indicate current page
- Add skip-page box to allow user skip to some certain page
  
<details><summary>See feature images</summary>

![Pagination](static/images/features/pagination.png)
</details>

##### Back to [top](#table-of-contents)<hr>


## Validation

The W3C Markup Validation Service
<details><summary>Login</summary>
<img src="static/images/validation/login.png">
</details>

<details><summary>Admin</summary>
<img src="static/images/validation/admin.png">
</details>

<details><summary>Add New Admin</summary>
<img src="static/images/validation/admin-add.png">
</details>

<details><summary>Department</summary>
<img src="static/images/validation/depart.png">
</details>

<details><summary>Create Department Title</summary>
<img src="static/images/validation/depart-add.png">
</details>

<details><summary>Employee</summary>
<img src="static/images/validation/employee.png">
</details>

<details><summary>Add New Employee</summary>
<img src="static/images/validation/employee-add.png">
</details>


### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>
<img src="static/images/validation/css.png">
</details><hr>


### JavaScript Validation
JSHint JS Validation Service

<details><summary>Script.js</summary>
<img src="static/images/validation/js.png">
</details><hr>


### PEP8 Validation
PEP8 Validation Service was used to check the code for PEP8 requirements via Pycodestyle as PEP8online was no longer available

<details><summary>Tool used: Pycodestyle</summary>
<img src="static/images/pep8-validation/pycodestyle-install.png">
</details>

<details><summary>models.py</summary>
<img src="static/images/pep8-validation/models.png">
</details>

<details><summary>views.py</summary>
<img src="static/images/pep8-validation/views.png">
</details>

<details><summary>urls.py</summary>
<img src="static/images/pep8-validation/urls.png">
</details>

<details><summary>bootstrap.py</summary>
<img src="static/images/pep8-validation/bootstrap.png">
</details>

<details><summary>encrypt.py</summary>
<img src="static/images/pep8-validation/encrypt.png">
</details>

<details><summary>form.py</summary>
<img src="static/images/pep8-validation/form.png">
</details>

<details><summary>pagination.py</summary>
<img src="static/images/pep8-validation/pagination.png">
</details>


### Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

#### Desktop
<details><summary>Admin</summary>
<img src="static/images/lighthouse/admin.png">
</details>

<details><summary>Department</summary>
<img src="static/images/lighthouse/depart.png">
</details>

<details><summary>Employee</summary>
<img src="static/images/lighthouse/employee.png">
</details>

#### Mobile
<details><summary>Admin</summary>
<img src="static/images/lighthouse/admin-mobile.png">
</details>

<details><summary>Department</summary>
<img src="static/images/lighthouse/depart-mobile.png">
</details>

<details><summary>Employee</summary>
<img src="static/images/lighthouse/employee-mobile.png">
</details>

##### Back to [top](#table-of-contents)<hr>


### Automated testing

- Testing was done using the built-in Django module, unittest.

##### Back to [top](#table-of-contents)<hr>


## Bugs

### Fixed Bugs

- Run the python3 manage.py migrate command not working as excepted. When I create Django project, I forgot the . at the end of the project name. Then I recreate the project.
- Run the python3 manage.py collectstatic command not working. Delete the static folder in Cloudinary and recreate one.
- Deploy to Heroku failed. Delate the add-on.

### Unfixed Bugs

- No bugs remaining

##### Back to [top](#table-of-contents)<hr>

### Heroku Deployment


The website was deployed by following the steps below: 

1. Log in [Heroku](https://id.heroku.com/login). 

2. Click 'New' and select 'Create new app'

3. Choose a name for the app, region and click on 'Create app'

4. Only 'Deploy' and 'Settings' are relevant from the menu section. Starting with the 'Settings' first.

5. Now Buildpacks need to be added. They install future dependencies that are needed outside of the requirements file. The first is Python and the second is node.js. Python needs to be selected first and then node.js. Save this selection.

6. Now the 'Deploy' section needs to be selected from the menu and connect to Git Hub.

7. Enter the name of the repository we want to connect it with and click 'Connect'

8. The choice appears now to either deploy using automatic deploys or manual deployment, which deploys the current state of the branch.

9. Click deploy branch. 

##### Back to [top](#table-of-contents)<hr>


## Credits

- Two walkthrough projects Hello Django and I Think Therefore I Blog. Learned how set up the environment of the project.
- Bootstrap layout

##### Back to [top](#table-of-contents)<hr>


## Acknowledgments


Many thanks to the student care from the Code Institute for assisting me to solve the bugs and give me suggestions to optimize my code. At the same, I want to thanks my family to support me in using my spare time to learn to code.

##### Back to [top](#table-of-contents)<hr>


