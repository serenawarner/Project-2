# Project-2

For this project, we will use daily check-ins with your team.  These are associated with Agile software development methodology.  The purpose of this is for you to update your team at the beginning of each class.  A good update includes a description of:   

1) what was completed since last time 
2) what you plan to complete today 
3) what is blocking your progress 

Updates are typically given while standing, to keep the time spent talking short. 

Your group should have 4 people.  In your group, please choose an idea for your project.  Create a list of features using Github Issues, and give them a description and priority.  Assign these to your group so that each person has at least one feature.  You can also refer to Issue numbers in Pull Requests and commit messages.  Try to estimate the amount of time that each feature will take.  This is commonly done using a Fibonacci scale:  1,2,3,5, or 8 days.  (Although you are not technically supposed to measure time with Agile).  Your project should have a ReadMe file with documentation for a use and installation.  Your application should create debugging logs while running.  

The design of your application is up to your team. You can use pair programming and test driven development, along with any other system design principles.  Create one pull request per feature, with a description, and ask a team member to review the changes before merging.   

Your features should have some unit tests associated with each change.  It may be worth the time to configure your project with GitHub Actions, or other CI/CD tools that will automatically run unit tests, if they offer a free tier.  If someone on your team wants to manually test the app for bugs, they can do this also.  This is typically called manual Regression Testing, which looks for bugs and tries to break things. 

Prepare a demo of your app to present.  Create release notes summarizing each feature at the end of development time.

1) code program in python
2) no/minimal ui/ux

 Battleship
------------
Natalie and Theo:
- [] drawMap()

Russell:
- [] placeShip(size,location,rotation)


Noelynn:
- [] drawScoreboard()
- [] drawHiddenMap()

Serena:
- [] hit(x,y)


----------------------------------------------------------

start with 2 players, automated if more time 

drawScoreboard() - 2 days
 - rounds

board class
 - hit(x,y) - 2 days
   - return hit or not
   - 5 times per round
 - drawMap() - 3 days
 - drawHiddenMap() - 2 days
 - placeShip(size,location,rotation) - 8 days
   - error for if ship already there
