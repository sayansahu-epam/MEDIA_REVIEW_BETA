import sys
sys.stdout.reconfigure(encoding="utf-8")

import argparse


import argparse

from services.recommendation_service import get_recommendations_for_user

from services.recommendation_service import get_top_rated_media

from services.review_service import get_reviews_for_media

from services.media_service import list_all_media, add_media, search_media

from services.user_service import list_all_users


from patterns.observer import UserObserver
from services.notification_service import notification_service
from services.media_service import list_all_media,add_media
from database.db_connection import create_tables
from services.user_service import add_user
from services.review_service import add_review




def main():
    # Ensure database tables exist
    create_tables()
    
    # Temporary observer registration
    notification_service.register_observer(
        UserObserver("Sayan")
    )
    
    


    parser = argparse.ArgumentParser(
        description="CLI-based Media Review System"
    )
    
    
    
    parser.add_argument(
    "--search",
    metavar="TITLE",
    help="Search media by title"
    )
    
    
    parser.add_argument(
    "--recommend",
    metavar="USER_ID",
    help="Get media recommendations for a user"
    )


    parser.add_argument(
    "--reviews",
    metavar="MEDIA_ID",
    help="View all reviews for a media item"
    )
    
    
    parser.add_argument(
    "--top-rated",
    action="store_true",
    help="View top-rated media"
    )


    
    
    
    
    
    parser.add_argument(
    "--list-users",
    action="store_true",
    help="List all users"
    )


    parser.add_argument(
        "--list",
        action="store_true",
        help="View all media"
    )
    
    
    
    
    
    
    parser.add_argument(
    "--add-media",
    nargs=3,
    metavar=("MEDIA_ID", "TITLE", "TYPE"),
    help="Add a new media item"
    )
    
    
    parser.add_argument(
    "--add-user",
    nargs=2,
    metavar=("USER_ID", "NAME"),
    help="Add a new user"
    )
    
    
    parser.add_argument(
    "--review",
    nargs=4,
    metavar=("USER_ID", "MEDIA_ID", "RATING", "COMMENT"),
    help="Add a review for a media item by a user"
    )





    
    
    
    
    

    args = parser.parse_args()

    if args.list:
        media_items = list_all_media()

        if not media_items:
            print("No media found.")
            return

        for media in media_items:
            media_id, title, media_type = media
            print(f"[{media_id}] {title} ({media_type})")
            
            
    elif args.search:
        results = search_media(args.search)

        if not results:
            print("No matching media found.")
            return

        for media in results:
            media_id, title, media_type = media
            print(f"[{media_id}] {title} ({media_type})")
            
            
    elif args.reviews:
        media_id = int(args.reviews)
        reviews = get_reviews_for_media(media_id)

        if not reviews:
            print("No reviews found for this media.")
            return

        print(f"Reviews for media ID {media_id}:")
        for review in reviews:
            review_id, user_id, rating, comment = review
            print(f"User {user_id} → Rating: {rating} | {comment}")


            
            
    elif args.top_rated:
        results = get_top_rated_media()

        if not results:
            print("No rated media found.")
            return

        print("Top Rated Media:")
        for media in results:
            media_id, title, media_type, avg_rating = media
            print(f"[{media_id}] {title} ({media_type}) → Avg Rating: {round(avg_rating, 2)}")
            
            
    elif args.recommend:
        user_id = int(args.recommend)
        recommendations = get_recommendations_for_user(user_id)

        if not recommendations:
            print("No recommendations available.")
            return

        print(f"Recommendations for User {user_id}:")
        for media in recommendations:
            media_id, title, media_type = media
            print(f"[{media_id}] {title} ({media_type})")




            
    
    
    
    elif args.add_media:
        media_id = int(args.add_media[0])
        title = args.add_media[1]
        media_type = args.add_media[2]

        add_media(media_id, title, media_type)
        print("Media added successfully.")
        
        
    elif args.add_user:
        user_id = int(args.add_user[0])
        name = args.add_user[1]

        add_user(user_id, name)
        print("User added successfully.")
        
    elif args.review:
        
        user_id = int(args.review[0])
        media_id = int(args.review[1])
        rating = int(args.review[2])
        comment = args.review[3]

        import time
        review_id = int(time.time())

        add_review(review_id, user_id, media_id, rating, comment)
        print("Review added successfully.")
        
        
    elif args.list_users:
        users = list_all_users()

        if not users:
            print("No users found.")
            return

        for user in users:
            user_id, name = user
            print(f"[{user_id}] {name}")







if __name__ == "__main__":
    main()
