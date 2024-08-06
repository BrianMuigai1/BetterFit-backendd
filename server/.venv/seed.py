from datetime import date, timedelta
from app import db
from models import User, WorkoutPlan, NutritionPlan, ProgressTracking

# Function to create sample users
def create_users():
    users = [
        User(
            username="john_doe",
            email="john@example.com",
            password="password123",
            age=25,
            nationality="American",
            description="Fitness enthusiast and marathon runner.",
            hobbies="Running, Hiking, Reading"
        ),
        User(
            username="jane_smith",
            email="jane@example.com",
            password="securepass",
            age=30,
            nationality="British",
            description="Yoga instructor and nutrition coach.",
            hobbies="Yoga, Cooking, Traveling"
        ),
    ]
    return users

# Function to create sample workout plans
def create_workout_plans(users):
    workout_plans = [
        WorkoutPlan(
            user_id=users[0].id,
            title="Marathon Training",
            description="12-week training plan for running a marathon.",
            duration=12,
            start_date=date.today(),
            end_date=date.today() + timedelta(weeks=12)
        ),
        WorkoutPlan(
            user_id=users[1].id,
            title="Yoga for Beginners",
            description="A 6-week yoga plan for beginners.",
            duration=6,
            start_date=date.today(),
            end_date=date.today() + timedelta(weeks=6)
        ),
    ]
    return workout_plans

# Function to create sample nutrition plans
def create_nutrition_plans(users):
    nutrition_plans = [
        NutritionPlan(
            user_id=users[0].id,
            title="Marathon Diet",
            description="High carb, high protein diet for marathon training.",
            start_date=date.today(),
            end_date=date.today() + timedelta(weeks=12)
        ),
        NutritionPlan(
            user_id=users[1].id,
            title="Balanced Yoga Diet",
            description="A balanced diet for yoga practitioners.",
            start_date=date.today(),
            end_date=date.today() + timedelta(weeks=6)
        ),
    ]
    return nutrition_plans

# Function to create sample progress tracking entries
def create_progress_tracking(users):
    progress_tracking_entries = [
        ProgressTracking(
            user_id=users[0].id,
            weight=70.5,
            measurements="Chest: 90cm, Waist: 80cm, Hips: 95cm",
            date=date.today()
        ),
        ProgressTracking(
            user_id=users[1].id,
            weight=60.0,
            measurements="Chest: 85cm, Waist: 75cm, Hips: 90cm",
            date=date.today()
        ),
    ]
    return progress_tracking_entries

# Function to seed the database
def seed_database():
    # Create all tables
    db.create_all()
    
    # Create sample data
    users = create_users()
    workout_plans = create_workout_plans(users)
    nutrition_plans = create_nutrition_plans(users)
    progress_tracking_entries = create_progress_tracking(users)
    
    # Add data to the session
    db.session.add_all(users)
    db.session.flush()  # Flush to get user IDs before adding related data

    db.session.add_all(workout_plans)
    db.session.add_all(nutrition_plans)
    db.session.add_all(progress_tracking_entries)

    # Commit the session to the database
    db.session.commit()

if __name__ == "__main__":
    seed_database()
    print("Database seeded successfully!")
