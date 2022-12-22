# GitHub Codespaces ♥️ Flask

Development Environment: VS Code on GitPod

To run this application:

``` flask --app school --debug run ```

## TODO's

Set-up database models for users having the following roles

* Student - This entity describes a student in a school. Each student has fields for Names, Sex, Access Code, Admission Number, etc.

* Teacher - This role describes subject teachers, identified by their ID, subject, etc.

* Admin - This role defines personalities such as the Principal, IT Staff, etc.

* YearHead - This entity is responsible for modifying student details as well as passing remarks on student results.

## Permissions

* view:student-details
* view:students
* modify:student

* modify:student-details
* view:results

* modify:results
* delete:results

## Role Based Access Control (RBAC)

The following are the roles and permissions assigned to users in the system

* Student
```get::student-result```
```get::student-details```

* Admin
```get::student-result```
```get::student-details```
```write::student-result```
```write::student-details```

* YearHeads
```get::student-details```
```write::student-details```

* Teachers
```get::student-result```
```write::student-result```

## API Documentation

This API would be consumed by Frontend APPs
