[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Django Campus Server

## Library Documentation

### User Stories

- Version 1:
  - As a user, I want to view a single book
  - As a user, I want to view all books
  - As a user, I want to create a book with a title and author
  - As a user, I want to edit a book's title and author
  - As a user, I want to delete a book

- Version 2:
  - Everything in Version 1
  - As a user, I want to view an author
  - As a user, I want to view all authors
  - As a user, I want to create an author with a first name and lastt name
  - As a user, I want to edit an author's first name and lastt name
  - As a user, I want to delete an author
  - As a user, I want to assign a single author to a book
  - As a user, I want to assign multiple books to an author

- Version 3:
  - Everything in Version 2
  - As a user, I want to view a borrower
  - As a user, I want to view all borrowers
  - As a user, I want to create a borrower with a first name and lastt name
  - As a user, I want to edit a borrower's first name and lastt name
  - As a user, I want to delete a borrower
  - As a user, I want borrowers to loan many books
  - As a user, I want books to be loaned by many borrowers

### Entity Relationship Diagrams

#### Version 1

**Books**

<table>
  <th colspan="2" style="text-align:center">Books</th>
  <tr>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>title</td>
    <td>string</td>
  </tr>
  <tr>
    <td>author</td>
    <td>string</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
</table>

#### Version 2

`Authors` -|--< `Books`

**Books** belong to **Author**

**Author** has many **Books**

<table style="display:inline">
  <th colspan="2" style="text-align:center">Books</th>
  <th colspan="2" style="text-align:center">
  Authors
  </th>
  <tr>
    <td>id</td>
    <td>primary key</td>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>title</td>
    <td>string</td>
    <td>first_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>author_id</td>
    <td>foreign key</td>
    <td>lastt_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
</table>

#### Version 3

`Authors` -|--< `Books`

`Books` -|--< `Loans` >--|- `Borrowers`

**Books** belong to **Author**

**Author** has many **Books**

**Books** have many **Borrowers** through **Loans**

**Borrowers** have many **Books** through **Loans**

**Loans** belongs to both a **Book** and a **Borrower**

<table style="display:inline">
<th colspan="2" style="text-align:center">
Books
</th>
  <th colspan="2" style="text-align:center">Authors</th>
  <tr>
    <td>id</td>
    <td>primary key</td>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>title</td>
    <td>string</td>
    <td>first_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>author_id</td>
    <td>foreign key</td>
    <td>lastt_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
</table>

<br>

<table style="display:inline">
  <th colspan="2" style="text-align:center">
  Loans
  </th>
  <th colspan="2" style="text-align:center">
  Borrowers
  </th>
  <tr>
    <td>id</td>
    <td>primary key</td>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>borrower_id</td>
    <td>foreign key</td>
    <td>first_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>book_id</td>
    <td>foreign key</td>
    <td>lastt_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
</table>

## [License](../LICENSE)

1. All content is licensed under a CC­BY­NC­SA 4.0 license.
1. All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
