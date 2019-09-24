from string import ascii_letters, digits
from random import choice
import requests
import config
import random


host = 'http://127.0.0.1:8000/social_network/'
create_user_url = ''.join([host, 'api/users/'])
get_token = ''.join([host, 'token/'])
create_post_url = ''.join([host, 'api/posts/'])
like_url = ''.join([host, 'api/posts/{}/like/'])


def activity():
    for i in range(config.number_of_users):
        name = ''.join(choice(ascii_letters) for _ in range(5))
        password = ''.join(choice(ascii_letters) for _ in range(2)).join(choice(digits) for i in range(3))
        data = {'username': name, 'password': password}
        create = requests.post(create_user_url, data=data)
        print("User was created", create.json(), ' with password {}'.format(password))
        token = requests.post(get_token, data=data)
        token = token.json()
        header = {'Authorization': 'Token {}'.format(token['token'])}
        posts_number = random.randint(1, config.max_posts_per_user)
        # creating posts
        for _ in range(posts_number):
            title = ''.join(choice(ascii_letters) for _ in range(8))
            body = ''.join(choice(ascii_letters) for _ in range(50))
            post_data = {'title': title, 'body': body}
            add_post = requests.post(create_post_url, data=post_data, headers=header)
            print("Post was created", add_post.json())
        # liking
        post_add = add_post.json()
        if int(post_add["id"]) >= config.max_likes_per_user:
            likes = random.randint(1, config.max_likes_per_user)
        else:
            likes = random.randint(1, int(post_add["id"]))
        for j in range(likes):
            post_number = random.randint(1, int(post_add["id"]))
            requests.post(like_url.format(str(post_number)), headers=header)
            print('Post {} was liked'.format(str(post_number)))


if __name__ == '__main__':
    activity()
