# Workout Tracking API

A RESTful Flask API for tracking workouts, exercises, and workout sessions.

## Features

- Manage exercises (create, read, delete)
- Manage workouts (create, read, delete)
- Link exercises to workouts with sets, reps, and duration
- Nested data serialization with Marshmallow
- Input validation at both model and schema levels
- SQLAlchemy relationships for data integrity

## Project Structure

```
workout-api/
├── Pipfile
├── README.md
├── .gitignore
└── server/
    ├── app.py         # Flask application and routes
    ├── models.py      # SQLAlchemy models
    ├── schemas.py     # Marshmallow schemas
    └── seed.py        # Database seed script
```

## Installation

1. Install dependencies with pipenv:

```bash
pipenv install
```

2. Activate the virtual environment:

```bash
pipenv shell
```

3. Initialize the database migrations:

```bash
flask db init
```

4. Generate the migration:

```bash
flask db migrate -m "Initial migration"
```

5. Apply the migration:

```bash
flask db upgrade
```

6. Seed the database with sample data:

```bash
python server/seed.py
```

## Running the Application

Start the Flask development server:

```bash
FLASK_APP=server.app flask run
```

The API will be available at `http://127.0.0.1:5000`

## API Endpoints

### Exercises

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/exercises` | Get all exercises |
| GET | `/exercises/<id>` | Get a single exercise by ID |
| POST | `/exercises` | Create a new exercise |
| DELETE | `/exercises/<id>` | Delete an exercise |

**POST /exercises body example:**
```json
{
  "name": "Bench Press",
  "category": "Chest",
  "equipment_needed": true
}
```

### Workouts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workouts` | Get all workouts |
| GET | `/workouts/<id>` | Get a single workout by ID |
| POST | `/workouts` | Create a new workout |
| DELETE | `/workouts/<id>` | Delete a workout |

**POST /workouts body example:**
```json
{
  "date": "2026-04-12",
  "duration_minutes": 60,
  "notes": "Morning chest workout"
}
```

### Workout Exercises

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Add an exercise to a workout |

**POST body example (all fields optional):**
```json
{
  "reps": 10,
  "sets": 4,
  "duration_seconds": null
}
```

## Data Models

### Exercise
- `id` (integer, primary key)
- `name` (string, required, unique, min 3 chars)
- `category` (string, required)
- `equipment_needed` (boolean, required)

### Workout
- `id` (integer, primary key)
- `date` (date, required)
- `duration_minutes` (integer, required, must be > 0)
- `notes` (text, optional)

### WorkoutExercise (join table)
- `id` (integer, primary key)
- `workout_id` (integer, foreign key)
- `exercise_id` (integer, foreign key)
- `reps` (integer, optional, must be >= 0)
- `sets` (integer, optional, must be >= 0)
- `duration_seconds` (integer, optional, must be >= 0)

## Validation

The API enforces validation at multiple levels:
- Model-level validation using SQLAlchemy `@validates` decorators
- Schema-level validation using Marshmallow `@validates` decorators
- Database constraints (CheckConstraints) for data integrity

## Error Responses

All errors return JSON in the following format:
```json
{
  "error": "Error type",
  "message": "Detailed error message"
}
```

Status codes:
- 400: Bad request (validation errors)
- 404: Not found
- 500: Internal server error