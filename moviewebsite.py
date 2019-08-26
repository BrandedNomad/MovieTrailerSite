from media import Movie
import fresh_tomatoes

toystory = Movie()
toystory.set_title("Toy Story")
toystory.set_story("Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.")
toystory.set_image(
    "https://shop.line-scdn.net/themeshop/v1/products/cc/ed/e8/ccede8cb-80f5-491f-a64a-12e825865038/61/WEBSTORE/icon_198x278.png?__=20161019")
toystory.set_trailer("https://www.youtube.com/watch?v=4KPTXpQehio")

bohemian = Movie()
bohemian.set_title("Bohemian Rapsody")
bohemian.set_story("Bohemian Rhapsody is a foot-stomping celebration of Queen, their music and their extraordinary lead singer Freddie Mercury. Freddie defied stereotypes and shattered convention to become one of the most beloved entertainers on the planet. The film traces the meteoric rise of the band through their iconic songs and revolutionary sound. They reach unparalleled success, but in an unexpected turn Freddie, surrounded by darker influences, shuns Queen in pursuit of his solo career. Having suffered greatly without the collaboration of Queen, Freddie manages to reunite with his bandmates just in time for Live Aid. While bravely facing a recent AIDS diagnosis, Freddie leads the band in one of the greatest performances in the history of rock music. Queen cements a legacy that continues to inspire outsiders, dreamers and music lovers to this day")
bohemian.set_image("https://upload.wikimedia.org/wikipedia/en/2/2e/Bohemian_Rhapsody_poster.png")
bohemian.set_trailer("https://www.youtube.com/watch?v=mP0VHJYFOAU")

wild = Movie()
wild.set_title("Into the Wild")
wild.set_story("This is the true story of Christopher McCandless (Emile Hirsch). Freshly graduated from college with a promising future ahead, McCandless instead walked out of his privileged life and into the wild in search of adventure. What happened to him on the way transformed this young wanderer ")
wild.set_image(
    "https://images-na.ssl-images-amazon.com/images/I/51f34GSeBXL._SY445_.jpg")
wild.set_trailer("https://www.youtube.com/watch?v=g7ArZ7VD-QQ")

romeo = Movie()
romeo.set_title("Romeo and Juliet")
romeo.set_story("The classic story of Romeo and Juliet, set in a modern-day city of Verona Beach. The Montagues and Capulets are two feuding families, whose children meet and fall in love. They have to hide their love from the world because they know that their parents will not allow them to be together.")
romeo.set_image("https://m.media-amazon.com/images/M/MV5BMGU4YmI1ZGQtZjExYi00M2E0LTgyYTAtNzQ5ZmVlMTk4NzUzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg")
romeo.set_trailer("https://www.youtube.com/watch?v=5ZqxOb2tJIo")

inception = Movie()
inception.set_title("Inception")
inception.set_story("The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious, and is offered a chance to have his criminal history erased as payment for the implantation of another person's idea into a target's subconscious.")
inception.set_image(
    "https://images-na.ssl-images-amazon.com/images/I/7106uLYY2LL._SY606_.jpg")
inception.set_trailer("https://www.youtube.com/watch?v=YoHD9XEInc0")

king = Movie()
king.set_title("Romeo and Juliet")
king.set_story("The story of King George VI, his impromptu ascension to the throne of the British Empire in 1936, and the speech therapist who helped the unsure monarch overcome his stammer. Biopic about Britain's King George VI (father of present day Queen Elizabeth II) and his lifelong struggle to overcome his speech impediment.")
king.set_image("https://blogs.fco.gov.uk/wp-content/uploads/Kings-speech.jpg")
king.set_trailer("https://www.youtube.com/watch?v=EcxBrTvLbBM")

movies = [toystory, bohemian, wild ,romeo, inception, king]
fresh_tomatoes.open_movies_page(movies)
