import requests
import csv

def fetch_and_print_posts():
    """API-dən postları çəkir və başlıqlarını çap edir."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Status kodunu çap edirik
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # JSON məlumatını parse edirik
        posts = response.json()

        # Hər bir postun başlığını çap edirik
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """API-dən postları çəkir və posts.csv faylına qeyd edir."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
               # Məlumatı id, title və body olacaq şəkildə strukturlaşdırırıq
        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']} 
            for post in posts
        ]

        # CSV faylına yazma prosesi
        filename = "posts.csv"
        fieldnames = ['id', 'title', 'body']

        with open(filename, mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Başlıqları yazırıq
            writer.writeheader()
            # Məlumatları yazırıq
            writer.writerows(structured_data)
