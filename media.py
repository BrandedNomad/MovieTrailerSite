#
import webbrowser


class Movie:
    def __init__(self, title = None, story = None, image = None, trailer = None):
        self.title = title
        self.storyline = story
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def __repr__(self):
        return self.storyline

    def set_title(self, title):
        self.title = title

    def set_story(self, storyline):
        self.storyline = storyline

    def set_image(self,image):
        self.poster_image_url = image

    def set_trailer(self,trailer):
        self.trailer_youtube_url = trailer

    def get_title(self):
        return self.title

    def get_story(self):
        return self.storyline

    def get_poster_image(self):
        return self.poster_image_url

    def get_trailer(self):
        return self.trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
    
            
