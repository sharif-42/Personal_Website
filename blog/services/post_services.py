from ..models import Post, Comment


class PostService:
    model = Post

    def get_post_by_uuid(self, post_uuid) -> object:
        try:
            post_instance = Post.objects.get(uuid=post_uuid)
        except Post.DoesNotExist:
            post_instance = None
        return post_instance

    def create_comment(self, post_uuid, created_by, form_data):
        post_instance = self.get_post_by_uuid(post_uuid=post_uuid)
        field_values = {
            "post": post_instance,
            "name": form_data.get('name', ''),
            "email": form_data.get('email', ''),
            "description": form_data.get('description'),
            "user": created_by,
        }
        print(form_data)
        comment_obj = Comment.objects.create(**field_values)
        return post_instance
