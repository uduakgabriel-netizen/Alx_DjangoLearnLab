from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book


# ---------------------------------------------------------------------------
# GROUP + PERMISSION MANAGEMENT FOR THE 'Book' MODEL
#
# This utility function defines 3 user groups:
#   - Admins: Full access (create, view, edit, delete)
#   - Editors: Can create and edit book records
#   - Viewers: Read-only access to book records
#
# Permissions must first be declared in the Book model's Meta class:
#
#   class Meta:
#       permissions = [
#           ('can_view', 'Can View Book'),
#           ('can_create', 'Can Create Book'),
#           ('can_edit', 'Can Edit Book'),
#           ('can_delete', 'Can Delete Book'),
#       ]
#
# Usage:
#   group = create_group_permission("Admins")  # Returns the group instance
#   user.groups.add(group)                    # Assign group to a user
#
# This setup works well with decorators like @permission_required() in views.
# ---------------------------------------------------------------------------


# --- Group permissions ---
def create_group_permission(group):
    # Get a specific permission (e.g., 'can_create' for a 'Book' model)

    # content_type = ContentType.objects.get(app_label='bookshelf', model='Book')

    content_type = ContentType.objects.get_for_model(Book)
    
    # creating group
    editors_group, _ = Group.objects.get_or_create(name='Editors')
    viewers_group, _ = Group.objects.get_or_create(name='Viewers')
    admins_group, _ = Group.objects.get_or_create(name='Admins')

    can_create_permission = Permission.objects.get(codename='can_create', content_type=content_type)
    can_edit_permission = Permission.objects.get(codename='can_edit', content_type=content_type)
    can_view_permission = Permission.objects.get(codename='can_view', content_type=content_type)
    can_delete_permission = Permission.objects.get(codename='can_delete', content_type=content_type)

    # add permission to the group
    editors_group.permissions.add(can_create_permission)
    editors_group.permissions.add(can_edit_permission)
    viewers_group.permissions.add(can_view_permission)
    admins_group.permissions.add(can_create_permission)
    admins_group.permissions.add(can_edit_permission)
    admins_group.permissions.add(can_view_permission)
    admins_group.permissions.add(can_delete_permission)

    # return group
    if group == 'Editors':
        return editors_group
    elif group == 'Viewers':
        return viewers_group
    elif group == 'Admins':
        return admins_group
    else:
        raise ValueError('Group not on list')