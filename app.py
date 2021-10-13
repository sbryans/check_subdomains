import requests

def request(url):
        try:
                return requests.get("https://"+url)
        except requests.exceptions.ConnectionError:
                pass
print("Enter a URL \"without https://\"\n")

target = input()

with open("subs.txt", 'r') as file:
        for line in file:
                word = line.strip()
                full_url = word + "." + target
                response = request(full_url)

                if response:
                        print("Subdomain {} exists.".format(full_url))

print("\nAll done! Try adding more subdomains in the subs.txt file.")
