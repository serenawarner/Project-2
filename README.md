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

# how to play battleship

- both players place ships on a 10 x 10 grid. ships have different lengths and can be either horizontal or vertical
- each player can see a map of where their own ships are, as well as a map that displays where they have already attempted to shoot and whether or not they hit a ship in that location, in order to track where their opponent's ships might be
- when a player shoots and hits one of their opponent's ships, it should mark it on the map that tracks their attempted shots. when one of a player's ships is hit, that section of the ship should be marked on the map.
- each player gets 5 attempts to hit their opponent's ships per turn. on a 10 x 10 board, this caps the game's length at a worst-case maximum of 20 turns per player, making gameplay short and engaging
- the winner is the first player to successfully sink all of their opponent's ships

# documentation

## installation and use

download the folder of files. run "python main.py" ("python" might be "python3" depending on OS and version) in the command line.

## code documentation

### board

Each board is managed via a Board class. This class contains a map, which is an array of arrays. This structure allows for coordinates to be entered in the form of "map[x][y]", where x and y correspond to the targeted coordinate to the user and a specific item in a specific subarray to the computer.

The board, when initialized, takes a variable called "h", which determines whether the location of the ships is visible on the board. If h is true, then the ships will be hidden and only the explosions will be shown on hit ships. This function enables the drawmap() function to create both hidden boards to track the opponent's map and visible ones for a player to track their own ships.

Each coordinate on the board is represented as a string filled by an emoji. The possible coordinate states are as follows:

  empty space on the visible map = "🌊"  
  ship location on the visible map = "🚢"  
  ship section that has been hit on the visible map *or* successful shot on the hidden map = "💥" 
  unknown coordinate on the hidden map = "◼️"
  
  unsuccessful shot on the hidden map = "❌" 

### ship

Every ship has a length, an (x,y) coordinate that marks its starting place, and a boolean that determines whether the ship is horizontal or vertical. 

The Ship class contains a function that determines whether the ship is hit by taking an (x,y) coordinate and checking whether there is a ship at that location by calculating the length and direction of the ship relative to its starting coordinate, called hit(x,y)

The ship has a secondary class that contains some of its locational information called ShipSize. This class contains a few utility functions that assist in calculation for the Ship class.
