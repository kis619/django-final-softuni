# Django Web App Requirements
- The application must have at least 10 web pages:
  - Can be created using function-based views or/and class-based views;
  - At least 5 of them must be class-based views.
- The application must have at least 5 independent models.
- The application must have at least 5 forms.
- The application must have at least 5 templates.
- **Database Service:** default SQLite
- Use Django Template Engine
- The application must have login/register/logout functionality.
- The application must have a public part (A part of the website, which is accessible by everyone - unauthenticated users and admins).
- The application must have a private part (accessible only by authenticated users and admins).
- The application must have a customized admin site (accessible only by admins):
  - Add at least 5 custom options (in total) to the admin interface (e.g., filters, list display, ordering, etc.).
- Unauthenticated users (public part) have only 'get' permissions, e.g., landing page, details, about page, and login/register 'post' permissions.
- Authenticated users (private part) have full CRUD for all their created content.
- Admins - at least 2 groups of admins:
  - One must have permission to do full CRUD functionalities (superusers);
  - The other/s have permission to do limited CRUD functionalities (staff).
  - User roles could be manageable from the admin site.
  - Make sure the role management is secure and error-safe.
- Implement Exception Handling and Data Validation to avoid crashes when invalid data is entered (both client-side and server-side).

## Application Overview

This Django web app is designed as a social media platform specifically for long-form content. Users can create and share posts with a minimum length of 2,000 words, enabling in-depth expression and storytelling.


## Bonus
I had a lot of fun and experienced a lot of frustration trying to get the reactions to work
