from markdownx.utils import markdownify


def prepare_posts(request, *posts):
    for post in posts:
        post.content = markdownify(post.content)

        post.updated = False
        post.downvoted = False

        if request.user.is_authenticated:
            if any(p.user == request.user for p in post.upvote_set.all()):
                post.upvoted = True

            if any(p.user == request.user for p in post.downvote_set.all()):
                post.downvoted = True

    if len(posts) > 1:
        return posts
    return posts[0]
