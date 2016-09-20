# UDN-lite
A mini undiagnosed diseases network app built in Django for Harvard Med School code test.

Built with <3.

## Starting the app

Should be pretty straightforward.  I did not use my own DB solution, SQLite does everything I need.

Requirements:

* python3

```
# Register and make models
$ python manage.py makemigrations
$ python manage.py migrate

# Start the server
$ python manage.py runserver
```

## Models

### Participants
The participants in the study or database.  Contains name and date of birth attributes.  Age is calculated via `getAge()` method using the date of birth.

Associated environmental exposures and genetic mutations are connected via many-to-many relationship.  This allows the app the ability to sort and identify participants based on these attributes and might be helpful later on down the line.

Methods `getEnvironmentalExposures()` and `getGeneticMutations()` do exactly what you expect.

### Environmental Exposures and Genetic Mutations
For this example, these are identical.  Only a name and description attribute, but I assume some smart scientist somewhere might want them to be more capable.

## Views

### Form view
The form view will dynamically switch based on the context it receives.  Thus, any new object entry will have the same entry point.  This might bite us later on down the line if the app were to grow, but it's not a crazy idea to split off future forms into their own view and even group associated forms in this way.

### Participant View
Lists all the relevant attributes for the given participant.  Also provide s entry into the new gm and new ee forms.

### Participant List View
Lists all the participants entered into the system.