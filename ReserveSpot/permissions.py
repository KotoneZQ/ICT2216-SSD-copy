def check_permission(user, resource, action):
    permissions = {
        'Admin': {
            'VendorAccountDetails': ['read', 'update', 'delete'],
            'UserAccountDetails': ['read', 'update', 'delete'],
            'ActivityListings': ['read', 'update', 'delete'],
            'Bookings': ['read', 'update', 'delete'],
            'Reviews': ['read', 'update', 'delete']
        },
        'Vendor': {
            'VendorAccountDetails': ['create', 'read', 'update', 'delete'],
            'ActivityListings': ['create', 'read', 'update', 'delete'],
            'Bookings': ['read', 'update', 'delete'],
            'Reviews': ['read']
        },
        'User': {
            'UserAccountDetails': ['create', 'read', 'update', 'delete'],
            'ActivityListings': ['read'],
            'Bookings': ['create', 'read', 'update', 'delete'],
            'Payments': ['create', 'read', 'update', 'delete'],
            'Reviews': ['create', 'read', 'update', 'delete']
        }
    }
    return action in permissions.get(user.role, {}).get(resource, [])


def has_admin_access(user):
    return user.is_authenticated and user.role in ['Admin']