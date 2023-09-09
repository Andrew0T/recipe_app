Recipe App

![searches](https://github.com/Andrew0T/recipe_app/assets/113891991/e0f9cf76-1c32-4ca0-a176-bad0e9a83efe)


Overview

Recipe App is a full stack application built by Python using Django MVT web framework and it comes with the admin panel to perform CRUD operations in or on the database. 
Using Django's user authentication and view protection security measures, only registered users have access to the recipes list and details. 
The Recipe app allows users to searching recipes by name and data is returned as a single table column and the user has the option of 3 different chart types, bar, pie or line.

Key features

    Displays all recipes once user has logged in
    Details of each recipe displayed upon selection
    Search function allows full, partial word or single letter to be used as criteria
    Return recipes are shown and data visualizaions based on the user's search criteria
    18 preload Recipes are included

Technologies

    Python
    Django
    pandas
    matplotlib
    Pillow
    CSS

Video

https://github.com/Andrew0T/recipe_app/assets/113891991/4051e89f-a8be-46ca-9e24-82f2bd64c4cc


To see the live version

https://my-recipe-app-20230829-6f8ec0be54fd.herokuapp.com/

Login use
Username: u16831
Password: Have@Look23

Challenges: 

    1. was unable to move the database from sqlite to a format that heroku would read, searched and this answer
     https://stackoverflow.com/questions/61336258/how-to-transfer-your-local-sqlite3-data-to-heroku#61336319
    
    2. the recipe images failed to load and console error 404, not sure why. 
        Tutor's Answer: there were several steps 
        moved the recipe images within the static folder and renamed it to recipes
        because the file is saved as recipes/image.jpg.
        In html pages update the file image name
    