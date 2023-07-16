def create_youtube_video(title, description):
	youtubevideo = {'title' : title, 'description' : description, 'likes' : 0, 'dislikes' : 0, 'comments' : {}}
	return youtubevideo

def like(youtubevideo):
	if 'likes' in youtubevideo:
		youtubevideo['likes'] += 1
	return youtubevideo

def dislike(youtubevideo):
	if 'dislikes' in youtubevideo:
		youtubevideo['dislikes'] += 1 
	return youtubevideo 

def add_comment(youtubevideo, username, comment_text):
	youtubevideo['comments'][username] = comment_text
	return youtubevideo

new_youtube_video = create_youtube_video("cats","this is the cat")
like(new_youtube_video)
dislike(new_youtube_video)
add_comment(new_youtube_video, 'alma', 'kkk')
while new_youtube_video['likes']<495:
	like(new_youtube_video)
print(new_youtube_video)