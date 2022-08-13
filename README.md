
## Overview
Company Yola is a startup company that connects cleaning companies to individuals and companies(client). A solution was built to manage cleaners profile, client details, payment, etc. But the company needed a way to schedule cleaners' shifts and send reminders when a client requested a change.

### How the system works
* A client can request a cleaner from a company
* A cleaner can specify availability
* A client can reschedule, reject and end cleaners shift
  
Build a Web API(Python/Flask app - api only)  that:
- Reminds the cleaner 2hrs before the shift 
>(sample: Hello john doe, your cleaning shift for client XYZ is in 2hours. Don’t be late and do a good job. Thanks)

- Notify cleaner when shift changes or rescheduled
> (sample: Hello john doe, your cleaning shift for client XYZ has been rescheduled for the weekend, kindly notify your availability. Thanks)

### Functional Specification
* No sign-in/sign-up/login required
* Client are identified only by their email addresses
* All information should be predefined (pre-seeded in the DB)
* Company should be able to assign cleaner to client

### Workflow
* Client enter email address
* Select Company from dropdown
* Select Cleaner from dropdown
* Set cleaning schedules
* Edit schedules 

### Schema.sql 
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
> Name
```
### Evaluation Criteria
* Write the sent messages/mails to a log file(extra bonus if external mail service is implemented)
* Set Up a scheduling system to handle the process
* SQL queries for creating all new entities
* Necessary Python APIs exposed
* Updated UI to permit new use cases
* Unit Tests for core logic
* Strong OOP principles
* Well documented README.md
* Demo/Presentation

### Technologies
* Python/Flask
* JavaScript/React
* MySQL

## Next stage
* Setup the project in this repo
* Create required scheduling endpoints and associated logic
* Create notification tasks
* Update UI to handle new use case 

