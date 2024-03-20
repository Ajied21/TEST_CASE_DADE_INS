from google.oauth2 import service_account
from google.cloud import storage

keys = service_account.Credentials.from_service_account_file("Key/google-credential.json")

def upload_to_gcs(dataset, bucket_name, local_file_path):

    client  = storage.Client(credentials=keys)

    bucket  = client.get_bucket(bucket_name)

    blob    = bucket.blob(f"test-data/{dataset}")
    
    blob.upload_from_filename(local_file_path)

def main():

    bucket          = "test-case-dade-ins"

    data            = "ArifReport.csv"

    local_file_path = "C:/Users/G2 Academy/OneDrive/Desktop/TEST_CASE_DADE_INS/Data/ArifReport.csv"

    upload_to_gcs(data, bucket, local_file_path)


if __name__ == "__main__":
        
    try:
        
        main()
        print(f"data success to upload gcs")
    
    except:

        print(f"unsuccess data to upload gcs")