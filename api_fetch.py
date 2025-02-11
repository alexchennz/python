import requests
import json

def fetch_todo():
    """
    Fetch todo data from JSONPlaceholder API
    
    Returns:
        dict: Todo item data
    """
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    try:
        # Make GET request to the API
        response = requests.get(url)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Parse JSON response
        todo_data = response.json()
        return todo_data
        
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_todo(todo):
    """
    Display todo item in a formatted way
    
    Args:
        todo (dict): Todo item data
    """
    if todo:
        print("\n=== Todo Item ===")
        print(f"User ID: {todo['userId']}")
        print(f"Todo ID: {todo['id']}")
        print(f"Title: {todo['title']}")
        print(f"Completed: {todo['completed']}")
        
        # Print raw JSON for reference
        print("\nRaw JSON:")
        print(json.dumps(todo, indent=2))
    else:
        print("No data to display")

def fetch_all_posts():
    """
    Fetch all posts from JSONPlaceholder API
    
    Returns:
        list: List of post dictionaries
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        # Make GET request to the API
        response = requests.get(url)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Parse JSON response
        posts_data = response.json()
        return posts_data
        
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
        return None

def display_posts(posts):
    """
    Display all posts in a formatted way
    
    Args:
        posts (list): List of post dictionaries
    """
    if not posts:
        print("No posts to display")
        return
        
    print("\n=== All Posts ===")
    for post in posts:
        print(f"\nPost #{post['id']}")
        print(f"User ID: {post['userId']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 50)

def create_post(title, body, userId=1):
    """
    Create a new post via JSONPlaceholder API
    
    Args:
        title (str): Title of the post
        body (str): Body content of the post
        userId (int): User ID (default: 1)
    
    Returns:
        dict: Created post data from the API response
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Prepare the post data
    post_data = {
        "title": title,
        "body": body,
        "userId": userId
    }
    
    try:
        # Make POST request to the API
        response = requests.post(url, json=post_data)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Parse JSON response
        created_post = response.json()
        return created_post
        
    except requests.RequestException as e:
        print(f"Error creating post: {e}")
        return None

def display_created_post(post):
    """
    Display created post details
    
    Args:
        post (dict): Created post data
    """
    if post:
        print("\n=== Created Post ===")
        print(f"Post ID: {post['id']}")
        print(f"User ID: {post['userId']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("\nNote: In JSONPlaceholder API, creates are not persisted.")
    else:
        print("Failed to create post")

def update_post(post_id, title=None, body=None, userId=None):
    """
    Update an existing post via JSONPlaceholder API
    
    Args:
        post_id (int): ID of the post to update
        title (str, optional): New title of the post
        body (str, optional): New body content of the post
        userId (int, optional): New user ID
    
    Returns:
        dict: Updated post data from the API response
    """
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    try:
        # First fetch the existing post
        response = requests.get(url)
        response.raise_for_status()
        existing_post = response.json()
        
        # Prepare the update data (keep existing values if not provided)
        update_data = {
            "title": title if title is not None else existing_post['title'],
            "body": body if body is not None else existing_post['body'],
            "userId": userId if userId is not None else existing_post['userId'],
            "id": post_id
        }
        
        # Make PUT request to update the post
        response = requests.put(url, json=update_data)
        response.raise_for_status()
        
        # Parse JSON response
        updated_post = response.json()
        return updated_post
        
    except requests.RequestException as e:
        print(f"Error updating post: {e}")
        return None

def display_updated_post(old_post, new_post):
    """
    Display the changes made to the post
    
    Args:
        old_post (dict): Original post data
        new_post (dict): Updated post data
    """
    if not new_post:
        print("Failed to update post")
        return
        
    print("\n=== Post Update Summary ===")
    print(f"Post ID: {new_post['id']}")
    
    # Compare and show changes
    print("\nChanges:")
    if old_post['title'] != new_post['title']:
        print(f"Title:\n  - Old: {old_post['title']}\n  + New: {new_post['title']}")
    if old_post['body'] != new_post['body']:
        print(f"Body:\n  - Old: {old_post['body']}\n  + New: {new_post['body']}")
    if old_post['userId'] != new_post['userId']:
        print(f"User ID:\n  - Old: {old_post['userId']}\n  + New: {new_post['userId']}")
        
    print("\nNote: In JSONPlaceholder API, updates are not persisted.")

def delete_post(post_id):
    """
    Delete a post via JSONPlaceholder API
    
    Args:
        post_id (int): ID of the post to delete
    
    Returns:
        bool: True if deletion was successful, False otherwise
    """
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    
    try:
        # First verify the post exists
        get_response = requests.get(url)
        get_response.raise_for_status()
        post_to_delete = get_response.json()
        
        # Make DELETE request to the API
        delete_response = requests.delete(url)
        delete_response.raise_for_status()
        
        return True, post_to_delete
        
    except requests.RequestException as e:
        print(f"Error deleting post: {e}")
        return False, None

def display_deleted_post(success, post):
    """
    Display the result of post deletion
    
    Args:
        success (bool): Whether deletion was successful
        post (dict): The deleted post data
    """
    if success and post:
        print("\n=== Post Deleted Successfully ===")
        print("Deleted post details:")
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"User ID: {post['userId']}")
        print("\nNote: In JSONPlaceholder API, deletes are not persisted.")
    else:
        print("Failed to delete post")

def main():
    choice = input("What would you like to do?\n1. Single Todo\n2. All Posts\n3. Create New Post\n4. Update Post\n5. Delete Post\nEnter choice (1/2/3/4/5): ")
    
    if choice == "1":
        print("Fetching todo data from JSONPlaceholder API...")
        todo = fetch_todo()
        display_todo(todo)
    elif choice == "2":
        print("Fetching all posts from JSONPlaceholder API...")
        posts = fetch_all_posts()
        display_posts(posts)
    elif choice == "3":
        print("\n=== Create New Post ===")
        title = input("Enter post title: ")
        body = input("Enter post body: ")
        userId = int(input("Enter user ID (default 1): ") or "1")
        
        print("\nCreating post...")
        created_post = create_post(title, body, userId)
        display_created_post(created_post)
    elif choice == "4":
        print("\n=== Update Post ===")
        post_id = int(input("Enter post ID to update: "))
        
        # Fetch the existing post first
        url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
        response = requests.get(url)
        old_post = response.json()
        
        print("\nCurrent post details:")
        print(f"Title: {old_post['title']}")
        print(f"Body: {old_post['body']}")
        print(f"User ID: {old_post['userId']}")
        
        print("\nEnter new values (press Enter to keep current value):")
        new_title = input("New title: ") or None
        new_body = input("New body: ") or None
        new_userId = input("New user ID: ")
        new_userId = int(new_userId) if new_userId else None
        
        print("\nUpdating post...")
        updated_post = update_post(post_id, new_title, new_body, new_userId)
        display_updated_post(old_post, updated_post)
    elif choice == "5":
        print("\n=== Delete Post ===")
        post_id = int(input("Enter post ID to delete: "))
        
        print(f"\nDeleting post {post_id}...")
        success, deleted_post = delete_post(post_id)
        display_deleted_post(success, deleted_post)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 