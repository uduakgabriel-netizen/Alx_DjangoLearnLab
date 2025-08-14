GROUP + PERMISSION MANAGEMENT FOR THE 'Book' MODEL
This utility function defines 3 user groups:

Admins: Full access (create, view, edit, delete)
Editors: Can create and edit book records
Viewers: Read-only access to book records
Permissions must first be declared in the Book model's Meta class:

class Meta:
   permissions = [
       ('can_view', 'Can View Book'),
       ('can_create', 'Can Create Book'),
       ('can_edit', 'Can Edit Book'),
       ('can_delete', 'Can Delete Book'),
   ]
Usage:
group = create_group_permission("Admins") # Returns the group instance user.groups.add(group) # Assign group to a user

This setup works well with decorators like @permission_required() in views.