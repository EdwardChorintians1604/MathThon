#!/usr/bin/env python3
"""
Test script untuk Profile CRUD APIs
"""

import requests
import json

# Base URL (sesuaikan dengan environment Anda)
BASE_URL = "http://localhost:5000"

# Headers untuk CSRF dan JSON
headers = {
    "Content-Type": "application/json"
}

def test_change_password():
    """Test change password endpoint"""
    print("\n=== Testing Change Password ===")
    url = f"{BASE_URL}/user/change_password"
    
    payload = {
        "old_password": "your_current_password",
        "new_password": "your_new_password"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

def test_upload_profile_photo():
    """Test upload profile photo endpoint"""
    print("\n=== Testing Upload Profile Photo ===")
    url = f"{BASE_URL}/user/upload_profile_photo"
    
    # Contoh upload file
    with open("path_to_image.jpg", "rb") as f:
        files = {"file": f}
        try:
            response = requests.post(url, files=files)
            print(f"Status: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {e}")

def test_update_profile():
    """Test update profile endpoint"""
    print("\n=== Testing Update Profile ===")
    url = f"{BASE_URL}/user/update_profile"
    
    data = {
        "name": "John Doe",
        "email": "john@example.com",
        "born_place": "Jakarta",
        "date": "1990-01-01"
    }
    
    try:
        response = requests.post(url, data=data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

def test_delete_account():
    """Test delete account endpoint"""
    print("\n=== Testing Delete Account ===")
    url = f"{BASE_URL}/user/delete_account"
    
    try:
        response = requests.post(url, headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Profile CRUD API Test")
    print("=" * 50)
    print("\nNote: Pastikan Anda sudah login sebelum testing!")
    print("Test ini memerlukan session cookie dan CSRF token yang valid")
    
    # Test endpoints
    # test_update_profile()
    # test_change_password()
    # test_upload_profile_photo()
    # test_delete_account()
    
    print("\nUncomment test functions untuk menjalankan test")
