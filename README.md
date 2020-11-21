[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Django Relationships

## Prerequisites

- [django-intro](https://git.generalassemb.ly/ga-wdi-boston/django-intro)
- [django-crud](https://git.generalassemb.ly/ga-wdi-boston/django-crud)

## Objectives

By the end of this, developers should be able to:

- Create one-to-many relationships with Django
- Create many-to-many relationships with Django
- Diagram relationships with ERDs

## Preparation

1. Fork and clone this repository.
 [FAQ](https://git.generalassemb.ly/ga-wdi-boston/meta/wiki/ForkAndClone)
1. Create a new branch, `training`, for your work.
1. Checkout to the `training` branch.
1. Run `pipenv shell` to start up your virtual environment.
2. Run `pipenv install` to install dependencies.
3. Create a psql database for the project
    1. Type `psql` to get into interactive shell
    2. Run `CREATE DATABASE "django-campus";`
    3. Exit shell
4. Generate and run migrations with `python3 manage.py makemigrations` and `python3 manage.py migrate`
5. Run the server with `python3 manage.py runserver`

## Building an API with Relationships

So far we have built some pretty basic applications with Django and Python, but
now we are going to step it up and add in relationships to our models. To guide
us, we have plenty of documentation about the API we are building, including
user stories and ERDs (Entity Relationship Diagrams).

This repository has our V1 for a library and hospital app. Our docs
show us that for V2 and V3, we are adding relationships to the different models.

## Library V2

For V2 of our library app we need to add a new resource called `Author` and
connect it to our `Book` resource. We will be building a one-to-many
relationship where a `Book` has one `Author` and an `Author` can be referenced
on many `Book` resources.

We can also think of this as an `Author` having multiple `Book`s, which is how
we diagram our ERD:

`Author` -|---< `Book`

### Code-Along: One-to-Many Relationships

In order to get started we should work methodically and build out `Author` and
make sure that resource works on it's own before connecting it to `Book`.

This repo has starter code for our `Author` resource, so right now we can CRUD
on that resource successfully on it's own. This is good - going methodically
and making sure `Author` works properly before adding a relationship will
ultimately help us write better code.

Now, to connect `Book` and `Author` we have to look to the model first. This
step will involve us adding a field to `Book` that references the `Author`
resource.

```py
author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)
```

Let's break this down:

- `models.ForeignKey`: creates a foreign key reference to the `'Author'` model.
This will allow the `author` field on `Book` to point to a specific `Author` in
our database.
    - Note: Foreign keys are used in databases to connect resources.

- `related_name`: this is what we will be able to access on the other side of
our relationship to see what books an author wrote.

- `on_delete=models.CASCADE`: this will cause the books our author wrote to be
deleted if the author is as well.
    - We have [lots of options](https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models) of what we can put here.

That's all we need to do to actually connect these resources!

We can ping our endpoint to create or update a book and send along an ID value
for the `author` field. This will be that "foreign key" that points to the
author who wrote the book.

However, we can't see the books that our authors wrote on the other side yet!
The `AuthorSerializer` can be updated to reference the `BookSerializer` and
then return the `'books'` field. This should match the name on the `Book` model
for the `related_name`.

```py
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'books')
```

Now, when an `Author` is returned from the database it will include a reference
to that author's `books`.

## Hospital V2

### Lab: `Doctor` -|---< `Patient`

Time to work on our next app's V2: hospital.

The [hospital docs](docs/hospital.md) lay out the details for two resources,
`Doctor` and `Patient`. This repository has some starter code for an app
`hospital`. Just like with the library's starter code, right now both
`Doctor` and `Patient` support successful CRUD on their own.

Let's connect these two resources:

1. Add `ForeignKey` field to `Patient`
2. Update `DoctorSerializer` to return `patients`

## Library V3

### Code-Along: Many-to-Many Relationships

Time to see how we can add a many-to-many relationship to `Book`. Following the
[library documentation](docs/library.md), `Book` should have a field that
references who has or is borrowing that books from the library.

`Book` >---< `Borrower`

`Borrower`s can borrow many `Book`s, and `Book`s can be borrowed by many
`Borrower`s!

As before, there is already a `Borrower` resource that supports full CRUD.

In the `Book` model we will add a new field to reference the `Borrower` model.

The `borrowers` field will be a `ManyToManyField` that will allow `Book` to
store multiple `borrowers`.

This field might be empty at some point, and that's okay, so the `blank=True`
option sets `borrowers` to be optional.

On the `Borrower` resource, the books borrowed will be referenced with the
`related_name` which is `loans`.

In the `BorrowerSerializer` we can reference the `BookSerializer` to be able to
see the books a borrower has borrowed.

#### SQL Join

Sometimes, we want a table to keep track of the connections between resources.
For example, a resource called `Loan` could keep track of the ID of the
`Borrower` and the `Book` in our many-to-many relationship. In relational
databases, this kind of resource/table that "joins" the relationship between
two other resources is known as a join table. This table could also hold
information about the loan, like due date and checkout date.

We often talk about building a relationship that goes "through" this join
table, which is why you'll often see the keyword `through` when building out
join tables in different frameworks.

In Django we can accomplish a join table for our `Book` >---< `Borrower`
relationship using the current `Loan` model. We will need to modify our models
so that `Loan` can be used to represent this relationship. 

1. Add two `ForeignKey`s to `Loan` (join table)
    - This will keep track of the relationship to the `Book` and `Borrower`
    - Note: We can also give it any other fields we want, like a due date!
2. Update the `borrower` field on `Book` to go "through" the `Loan` table
    - Use `through` to reference the `Loan` model
    - Use `through_fields` to reference the fields on `Loan` that should refer to the `Borrower` and `Book` IDs
3. Add a `LoanReadSerializer` to display the book and borrower objects

`Book` -|--< `Loan` >--|- `Borrower`

We should be able to create a `Loan` and have that translate over to both
`Book` and `Borrower`, based on the data in the `Loan` we created. We actually
don't end up interacting with the `Book` or `Borrower`, but instead just CRUD on
`Loan`s.

## Hospital V3

Time to plug in a many-to-many relationship between `Doctor` and their
`Patient`s. The [hospital documentation](docs/hospital.md) shows us that we
should have a resource called `Appointment` to join `Doctor` and `Patient`.

### Lab: Join Patients and Doctors through `Appointment`

We need our `Appointment` before we can use it to "join" `Doctor` and `Patient`.

Use the current files for doctors and patients to help guide you.

1. Create an `Appointment` model
3. Add a new serializer class for `Appointment`s
2. Add CRUD views for `Appointment`s
4. Test CRUD on `Appointment`
5. Connect `Patient` and `Doctor` using the `Appointment` table

## Bonus Lab: Cafeteria App

[Django Relationships Practice Lab](https://git.generalassemb.ly/ga-wdi-boston/django-relationships-practice)

## Additional Resources

- [Django Models](https://docs.djangoproject.com/en/3.0/topics/db/models/)
- [Django One-to-Many Relationships](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/one_to_many.html)

## [License](LICENSE)

1. All content is licensed under a CC­BY­NC­SA 4.0 license.
1. All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
