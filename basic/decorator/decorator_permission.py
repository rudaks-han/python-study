def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get("permissions", []) and permission in user["permissions"]:
                return func(user, *args, **kwargs)
            else:
                print(f"User {user['name']} does not have permission: {permission}")
                return None

        return wrapper

    return decorator


@requires_permission("admin")
def delete_database(user):
    print("Database deleted!")


if __name__ == "__main__":
    user = {"name": "Alice", "permissions": ["user"]}
    delete_database(user)

    admin_user = {"name": "Bob", "permissions": ["admin"]}
    delete_database(admin_user)
