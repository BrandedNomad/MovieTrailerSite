from media import Movie
import fresh_tomatoes

toystory = Movie()
toystory.set_title("Toy Story")
toystory.set_story("Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.")
toystory.set_image("https://shop.line-scdn.net/themeshop/v1/products/cc/ed/e8/ccede8cb-80f5-491f-a64a-12e825865038/61/WEBSTORE/icon_198x278.png?__=20161019")
toystory.set_trailer("https://www.youtube.com/watch?v=KYz2wyBy3kc")

bohemian = Movie()
bohemian.set_title("Bohemian Rapsody")
bohemian.set_story("Bohemian Rhapsody is a foot-stomping celebration of Queen, their music and their extraordinary lead singer Freddie Mercury. Freddie defied stereotypes and shattered convention to become one of the most beloved entertainers on the planet. The film traces the meteoric rise of the band through their iconic songs and revolutionary sound. They reach unparalleled success, but in an unexpected turn Freddie, surrounded by darker influences, shuns Queen in pursuit of his solo career. Having suffered greatly without the collaboration of Queen, Freddie manages to reunite with his bandmates just in time for Live Aid. While bravely facing a recent AIDS diagnosis, Freddie leads the band in one of the greatest performances in the history of rock music. Queen cements a legacy that continues to inspire outsiders, dreamers and music lovers to this day")
bohemian.set_image("https://upload.wikimedia.org/wikipedia/en/2/2e/Bohemian_Rhapsody_poster.png")
bohemian.set_trailer("https://www.youtube.com/watch?v=mP0VHJYFOAU")

movies = [toystory, bohemian]
fresh_tomatoes.open_movies_page(movies)

    
            
