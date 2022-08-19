
Swept coding take home challenge. This little project allows you to showcase your skills developing with our tech stack.

# Overview
Company Yola is a startup company that connects cleaning companies to individuals and companies(client). A solution was built to manage cleaners profile, client details, payment, etc. But the company needed a way to schedule cleaners' shifts and send reminders when a client requested a change.

## How the system works
* A cleaning company can offer multiple cleaners to chose from
* A cleaner can specify availability
* A client can request a cleaner from a company
* A client can schedule and book a cleaning shift 

## Workflow
* Client enter email address
* Select Company from dropdown
* Select Cleaner from dropdown
* Schedule a cleaning shift 

## Schema.sql 
```
User
> ID 
> Name 
> Email Address 
> Availability Status
> Company ID

Schedule
> ID
> User ID
> Client ID
> Date range (text)

Company 
> ID 
> Name

Client
> ID 
> Email Address
```

> Note: Feel free to add other columns to the above schema if you think they'd be useful. For example, you can add a created_at and updated_at for each entity.
# Deliverables
## Technologies
* Python/Flask
* JavaScript/React
* MySQL

## Functional Specification
* No sign-in/sign-up/login required
* Client are identified only by their email addresses
* All information should be predefined (pre-seeded in the DB)
* Email messages can be logged in a file instead of sending an actual email

## Frontend (React)
Update the UI to:

* Allow a client to submit and create a new cleaning shift
* Display a confirmation message the booking was created

## Backend (Python/Flask/Celery)
Build a Web API that can:
* Create a new cleaning shift
* Send a booking confirmation email to both the client and cleaner
* Remind the cleaner 2hrs before the shift 
    >(sample: Hello john doe, your cleaning shift for client XYZ is in 2hours. Don’t be late and do a good job. Thanks)

# Next Steps
* Go through the requirements and let us know if you have any questions
* Setup the project in this repo, see the ReadMe files in the api and web folders
* Add additional pre-seeded data where required
* Create required scheduling endpoint
* Create notification tasks
* Update UI to handle new use case 

# Evaluation Criteria
* Write the sent messages/mails to a log file (extra bonus if external mail service is implemented)
* Set up the scheduling logic to handle the process
* SQL queries for creating new entities
* Necessary Python APIs exposed
* Updated UI to permit new use cases
* Unit Tests for core logic
* Strong OOP principles
* Well documented README.md
* Video demo/presentation

# Run Services
`docker-compose up -d --build`
