from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

class MongoDBClient:
    """Class to handle MongoDB operations"""
    
    def __init__(self):
        """Initialize MongoDB connection using environment variables"""
        # Use environment variable for the connection string
        self.connection_string = os.getenv('MONGODB_URI')
        if not self.connection_string:
            raise ValueError("MongoDB connection string not found in environment variables")
        
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client.get_database("test")  # Replace with your database name
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise
    
    def list_collections(self):
        """List all collections in the database"""
        try:
            collections = self.db.list_collection_names()
            return collections
        except Exception as e:
            print(f"Error listing collections: {e}")
            return []
    
    def fetch_all_documents(self, collection_name):
        """
        Fetch all documents from a specific collection
        
        Args:
            collection_name (str): Name of the collection
        """
        try:
            collection = self.db[collection_name]
            documents = list(collection.find({}))
            return documents
        except Exception as e:
            print(f"Error fetching documents from {collection_name}: {e}")
            return []
    
    def fetch_documents_with_filter(self, collection_name, filter_dict):
        """
        Fetch documents that match specific criteria
        
        Args:
            collection_name (str): Name of the collection
            filter_dict (dict): Filter criteria
        """
        try:
            collection = self.db[collection_name]
            documents = list(collection.find(filter_dict))
            return documents
        except Exception as e:
            print(f"Error fetching filtered documents from {collection_name}: {e}")
            return []
    
    def display_documents(self, documents):
        """
        Display documents in a formatted way
        
        Args:
            documents (list): List of documents to display
        """
        if not documents:
            print("No documents found")
            return
            
        for doc in documents:
            print("\n" + "="*50)
            for key, value in doc.items():
                if key == '_id':
                    print(f"ID: {value}")
                else:
                    # Format datetime objects
                    if isinstance(value, datetime):
                        value = value.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{key}: {value}")
    
    def close_connection(self):
        """Close the MongoDB connection"""
        try:
            self.client.close()
        except Exception as e:
            print(f"Error closing connection: {e}")


def main():
    try:
        # Initialize MongoDB client
        mongo_client = MongoDBClient()
        
        while True:
            print("\n=== MongoDB Operations ===")
            print("1. List all collections")
            print("2. View all documents in a collection")
            print("3. Search documents with filter")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                collections = mongo_client.list_collections()
                print("\nAvailable collections:")
                for collection in collections:
                    print(f"- {collection}")
                    
            elif choice == "2":
                collections = mongo_client.list_collections()
                print("\nAvailable collections:")
                for i, collection in enumerate(collections, 1):
                    print(f"{i}. {collection}")
                    
                collection_index = int(input("\nEnter collection number: ")) - 1
                if 0 <= collection_index < len(collections):
                    documents = mongo_client.fetch_all_documents(collections[collection_index])
                    mongo_client.display_documents(documents)
                else:
                    print("Invalid collection number")
                    
            elif choice == "3":
                collections = mongo_client.list_collections()
                print("\nAvailable collections:")
                for i, collection in enumerate(collections, 1):
                    print(f"{i}. {collection}")
                    
                collection_index = int(input("\nEnter collection number: ")) - 1
                if 0 <= collection_index < len(collections):
                    print("\nEnter filter criteria (example: {'field': 'value'}):")
                    filter_str = input()
                    try:
                        filter_dict = eval(filter_str)
                        documents = mongo_client.fetch_documents_with_filter(
                            collections[collection_index],
                            filter_dict
                        )
                        mongo_client.display_documents(documents)
                    except Exception as e:
                        print(f"Error parsing filter: {e}")
                else:
                    print("Invalid collection number")
                    
            elif choice == "4":
                print("\nClosing connection...")
                mongo_client.close_connection()
                break
                
            else:
                print("Invalid choice! Please try again.")
                
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main() 