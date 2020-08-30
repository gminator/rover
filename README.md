# Rover

The project is writting a single script to make it easy to run 

# Runing The Project 

## Animation 
To see the rovers move accross screen/grid

```bash
$ python run.py
```
You should see the rovers move accross the grid and change orientation as they do. 

## Unit Test

Unit test will run the varios functional components

```bash
$ python test.py
```


## Design 

###Note On Design

I subscribed to the principles of Domain-Driven Design, Single Responsibility, and OOP; all business logic is contained in specific models. 

I’ve written the functions to satisfy a single requirement where possible. This makes it easier to write unit tests. 

I always start with the lowest dependencies 1st for a more robust testing suit. This allows me to cover more scenarios across the layers of dependencies. In this example I call the entire stack even at the higher level of abstraction, normally I would make use of mocks, stubs, or patches but didn’t feel it was needed for this purpose (this method is useful when testing 3rd Party APIs). 
