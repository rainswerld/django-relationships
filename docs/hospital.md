[![General Assembly Logo](https://camo.githubusercontent.com/1a91b05b8f4d44b5bbfb83abac2b0996d8e26c92/687474703a2f2f692e696d6775722e636f6d2f6b6538555354712e706e67)](https://generalassemb.ly/education/web-development-immersive)

# Django Campus Server

## Hospital Documentation

### User Stories

- Version 1
  - As a user, I want to view a single patient
  - As a user, I want to view all patients
  - As a user, I want to create a patient with a first name, last name,
    diagnosis and born on
  - As a user, I want to edit a patient's first name, last name, diagnosis and
    born on
  - As a user, I want to delete a patient

- Version 2
  - Everything in Version 1
  - As a user, I want to view a doctor
  - As a user, I want to view all doctors
  - As a user, I want to create a doctor with a first name, last name, zip
    code and specialty
  - As a user, I want to edit a doctor's first name, last name, zip code and
    specialty
  - As a user, I want to delete a doctor
  - As a user, I want to assign a single doctor to a patient as their primary care physician
  - As a user, I want to assign multiple patients to a doctor as their primary care recipient

- Version 3
  - Everything in Version 2
  - As a user, I want to create an appointment between a patient and a doctor
  - As a user, I want to delete an appointment between a patient and a doctor

### Entity Relationship Diagrams

#### Version 1

**Patients**

<table>
  <th colspan="2" style="text-align:center">Patients</th>
  <tr>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>first_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>last_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>diagnosis</td>
    <td>string</td>
  </tr>
  <tr>
    <td>born_on</td>
    <td>date</td>
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

`Doctors` -|--< `Patients`

**Patients** belong to **Doctor**

**Doctor** has many **Patients**

<table style="display:inline">
  <th colspan="2" style="text-align:center">Patients</th>
  <th colspan="2" style="text-align:center">
  Doctors
  </th>
  <tr>
    <td>id</td>
    <td>primary key</td>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>first_name</td>
    <td>string</td>
    <td>first_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>last_name</td>
    <td>string</td>
    <td>last_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>diagnosis</td>
    <td>string</td>
    <td>zip_code</td>
    <td>string</td>
  </tr>
  <tr>
    <td>born_on</td>
    <td>date</td>
    <td>specialty</td>
    <td>string</td>
  </tr>
  <tr>
    <td>doctor_id</td>
    <td>foreign key</td>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
    <td></td>
    <td></td>
  </tr>
</table>

#### Version 3
```
Patients -|--< Appointments >--|- Doctors
 \/                                    |
  --------------------------------------
```
**Patients** have many **Doctors** through **Appointments**

**Doctors** have many **Patients** through **Appointments**

**Appointments** belongs to both a **Patient** and a **Doctor**

**Patients** belongs to **Doctor** as _Primary Care Physician_

**Doctor** as _Primary Care Physician_ has many **Patients**

<table style="display:inline">
  <th colspan="2" style="text-align:center">Patients</th>
  <th colspan="2" style="text-align:center">
  Appointments
  </th>
  <th colspan="2" style="text-align:center">
  Doctors
  </th>
  <tr>
    <td>id</td>
    <td>primary key</td>
    <td>id</td>
    <td>primary key</td>
    <td>id</td>
    <td>primary key</td>
  </tr>
  <tr>
    <td>first_name</td>
    <td>string</td>
    <td>patient_id</td>
    <td>foreign key</td>
    <td>first_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>last_name</td>
    <td>string</td>
    <td>doctor_id</td>
    <td>foreign key</td>
    <td>last_name</td>
    <td>string</td>
  </tr>
  <tr>
    <td>diagnosis</td>
    <td>string</td>
    <td>created_at</td>
    <td>datetime</td>
    <td>zip_code</td>
    <td>string</td>
  </tr>
  <tr>
    <td>born_on</td>
    <td>date</td>
    <td>updated_at</td>
    <td>datetime</td>
    <td>specialty</td>
    <td>string</td>
  </tr>
  <tr>
    <td>doctor_id</td>
    <td>foreign key</td>
    <td></td>
    <td></td>
    <td>created_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>created_at</td>
    <td>datetime</td>
    <td></td>
    <td></td>
    <td>updated_at</td>
    <td>datetime</td>
  </tr>
  <tr>
    <td>updated_at</td>
    <td>datetime</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>

## [License](../LICENSE)

1. All content is licensed under a CC­BY­NC­SA 4.0 license.
1. All software code is licensed under GNU GPLv3. For commercial use or
    alternative licensing, please contact legal@ga.co.
