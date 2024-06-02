import os
import json
from datetime import datetime, timezone, timedelta
import pandas as pd
import tweepy
from google.cloud import bigquery

DATASET_ID = "tweets_dataset"
TABLE_ID = "tweets_tbl"

def fetch_recent_tweets_for_user(client, user_id, start_time):
    # https://docs.tweepy.org.en/stable/client.html#tweepy.Client.get_users_tweets
    response = client.get_users_tweets(user_id, tweet_fields=['created_at'], start_time=start_time)
    print(type(response.data[0]))
    rows = []

    if response.data is not None:
        for tweet in response.data:
            #print(tweet.created_at)
            created_at = pd.Timestamp(tweet.created_at).strftime("%Y-%m-%d %H:%M:%S")
            values = {"tweet_id": tweet.id, "author-id": user_id, "created_at": created_at, "text": tweet.text}
            rows.append(values)
    
    return rows

def insert_rows_to_bq(rows):
    client = bigquery.Client()
    dataset_ref = client.dataset(DATASET_ID)
    table_ref = dataset_ref.table(TABLE_ID)
    error = client.insert_rows_json(table_ref, rows)
    if len(error) == 0:
        print("New row has been added")
    else:
        print("Encounter error  while inserting rows: {} ".format(error))

def entry_point(request): # Flask Request
    # Get Request
    token = os.environ.get("BEARER_TOKEN")
    
    client = tweepy.Client(bearer_token = token)

    user_id = 123456789
    start_time = datetime.now(timezone.utc) - timedelta(days = 30)
    start_time = start_time.strftime("Y-%m-%dT%H:%M%SZ")
    tweet_rows = fetch_recent_tweets_for_user(client, user_id=user_id, start_time=start_time)
    print(tweet_rows)
    insert_rows_to_bq(tweet_rows)
    return "Success", 200

if __name__ == "__main__":
    entry_point(None)