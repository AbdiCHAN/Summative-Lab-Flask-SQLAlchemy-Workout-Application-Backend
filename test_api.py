import requests
import json
from datetime import date

BASE_URL = "http://127.0.0.1:5000"

def test_api():
    print("Testing Workout Tracking API...")

    # Test 1: Get all exercises (should be empty initially)
    print("\n1. Testing GET /exercises")
    response = requests.get(f"{BASE_URL}/exercises")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test 2: Create a new exercise
    print("\n2. Testing POST /exercises")
    exercise_data = {
        "name": "Test Exercise",
        "category": "Test Category",
        "equipment_needed": True
    }
    response = requests.post(f"{BASE_URL}/exercises", json=exercise_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    exercise_id = response.json()['id']

    # Test 3: Get the created exercise
    print("\n3. Testing GET /exercises/{id}")
    response = requests.get(f"{BASE_URL}/exercises/{exercise_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test 4: Update the exercise
    print("\n4. Testing PUT /exercises/{id}")
    update_data = {
        "name": "Updated Exercise",
        "category": "Updated Category",
        "equipment_needed": False
    }
    response = requests.put(f"{BASE_URL}/exercises/{exercise_id}", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test 5: Delete the exercise
    print("\n5. Testing DELETE /exercises/{id}")
    response = requests.delete(f"{BASE_URL}/exercises/{exercise_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test 6: Get all workouts (should be empty initially)
    print("\n6. Testing GET /workouts")
    response = requests.get(f"{BASE_URL}/workouts")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test 7: Create a new workout
    print("\n7. Testing POST /workouts")
    workout_data = {
        "date": str(date.today()),
        "duration_minutes": 60,
        "notes": "Test workout"
    }
    response = requests.post(f"{BASE_URL}/workouts", json=workout_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    workout_id = response.json()['id']

    # Test 8: Get the created workout
    print("\n8. Testing GET /workouts/{id}")
    response = requests.get(f"{BASE_URL}/workouts/{workout_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test 9: Update the workout
    print("\n9. Testing PUT /workouts/{id}")
    update_data = {
        "date": str(date.today()),
        "duration_minutes": 90,
        "notes": "Updated workout"
    }
    response = requests.put(f"{BASE_URL}/workouts/{workout_id}", json=update_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Test 10: Delete the workout
    print("\n10. Testing DELETE /workouts/{id}")
    response = requests.delete(f"{BASE_URL}/workouts/{workout_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    print("\nAPI Testing Complete!")

if __name__ == "__main__":
    test_api()