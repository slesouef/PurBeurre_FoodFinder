# PurBeurre_FoodFinder
Create a programme for the fictional startup PurBeurre that will interact with the Open Food Facts database in order to extract products, compare them, and propose a healthier substitute that is of interest to the user.

# Fonctionalities:
- The application will run in a terminal window.

The user will be presented with numbered list of options in order to interact with the application

- The search will be run from a MySQL Database

At application first launch, the database creation script is run and the necessary information is downloaded via the Open Food Facts API.
The database is automatically populated with the a filtered version of the retrieved information to minimize the database size.

- The search is run by selecting a category of product, then selecting a product to replace

- The following information must be displayed to the user at the end of a search
    - Substitute product name
    - Substitute product description
    - Health rating of the substitute
    - Name of the place where the product can be found
    - Link to the Open Food Facts product's page

- The user can save a search once it has been completed

- In the case where the user enters an incorrect search value, the selection request is repeated

# Specifications:
- at first launch, create and populate the database with information retrieved from Open Food Facts
    - check if database exists
    - automatically run database creation script
    - retrieve info from Open Food Facts
    - filter information from Open Food Facts and insert in database

# Resources:

[Open Food Facts API](http://en.wiki.openfoodfacts.org/Project:API)

# Deliveries:
- Physical Data Model
- Database creation script
- Github repository location
- [Agile board](https://tree.taiga.io/project/slesouef-oc_purbeurre/taskboard/sprint-1-just-code-it)
- Project description document
