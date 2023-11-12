import requests

def main():
    Process_API()

def Process_API():
        # Make an API call and store that response
    url = 'https://api.github.com/search/repositories?=language:python&sort=stars'
    r = requests.get(url)
    if r.status_code == 200:
            
        # Store API response in a variable
        response_dict = r.json()
        # Process results
        print(response_dict.keys())
    elif r.status_code >= 404:
        print("Resource not found")
    else:
        print(f"Error: {r.status_code}")
        


main()