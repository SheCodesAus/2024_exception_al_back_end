## PLANIDEA

**Live Frontend**: https://planidea.netlify.app/

**Live Backend**: https://2024-exception-al-back-end.fly.dev/


### API SPECIFICATION
| HTTP Method | URL                                | Purpose                                                               | Request Body | Successful Response Code | Authentication and Authorization                     |
|-------------|------------------------------------|-----------------------------------------------------------------------|--------------|--------------------------|------------------------------------------------------|
| POST        | /api-token-auth/                  | User object. Logs user in and returns auth token                       | N/A          | 200                      | None required                                        |
| GET         | /workshops/                        | Returns a list of workshop objects                                    |              | 200                      | None required                                        |
| POST        | /workshop/create                   | Create a new workshop entry                                           | See below    | 201                      | User must be logged in. Auth token required         |
| GET         | /workshop/<workshop_id>/           | Returns Workshop page with id = <workshop_id>                         |              | 200                      | None required                                        |
| PUT         | /workshop/<workshop_id>/           | Edits/updates (partial) workshop detail page with id = <workshop_id>  |              | 200                      | User must be logged in. Auth token required.       |
| DELETE      | /workshop/<workshop_id>/           | Deletes Workshop page with id = <workshop_id>                         |              | 200                      | User must be logged in. Auth token required. Must be owner of <workshop_id> |
| GET         | /workshops/?is_active=True/       | Returns a list of active Workshops with the status is_active = True   |              | 200                      | None required                                        |
| GET         | /workshops/?order_by=closing_date | Returns a list of active Workshops in order of closing date           |              | 200                      | None required                                        |
| GET         | /users/                            | Returns a list of User objects                                        |              | 200                      | None required                                        |
| POST        | /users/                            | Create a new User                                                     | See below    | 201                      | None required                                        |
| GET         | /users/<user_id>/                 | Returns User profile with id = <user_id>                              |              | 200                      | User must be logged in. Auth token required.       |
| DELETE      | /users/<user_id>/                 | Delete User with id = <user_id>                                       |              | 200                      | Must be logged in as User id = <user_id>. Auth token required |
| PUT         | /user/change_password/            | Change User password with id=<user_id>                                | See below    | 200                      | Must be logged in as User id=<user_id>. Auth token required. |
| GET         | /eois/                            | Returns a list of EOIs                                               | See below    | 200                      | User must be logged in. Auth token required.       |
| POST        | /eoi/                            | Creates a new vote to participate in a Workshop object              | See below    | 201                        |  None required       |

### DATABASE SCHEMA

[Click here to view database schema](https://www.figma.com/proto/gIA4O41ID35xRIU9A2Fanp/Planet-Expressions?page-id=0%3A1&type=design&node-id=1-166&viewport=624%2C751%2C0.5&t=9W1qOP7NjVqqxKTU-1&scaling=min-zoom&mode=design)

