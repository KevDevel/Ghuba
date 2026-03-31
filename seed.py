from app import app
from models import db, Game

games = [
        {
            "thumb": "img/thumb/fc26.avif",
            "price": "75,81 NZ",
            "logo": "img/video-game-logos/Electronic-Arts-Logo.svg",
            "title": "EA SPORTS FC 26",
            "author": "EA Entertainment",
            "meta": "Vistas de 3.4M - Hace 6 meses"
        },
        {
            "thumb": "img/thumb/red-dead-redemption-II.jpg",
            "price": "80,50 NZ",
            "logo": "img/video-game-logos/Rockstar_logo_for_tweets.png",
            "title": "Red Dead Redemption II",
            "author": "RockStar Games",
            "meta": "Vistas de 10M - Hace 5 anos"
        },
        {
            "thumb": "img/thumb/good-of-war-rk.gif",
            "price": "120,00 NZ",
            "logo": "img/video-game-logos/playStation-logo.svg",
            "title": "God of war Ragnarow",
            "author": "PlayStation",
            "meta": "Vistas de 9.79M - Hace 1 ano"
        },
        {
            "thumb": "img/thumb/nfs-unbound.jpg",
            "price": "150,00 NZ",
            "logo": "img/video-game-logos/criterionGames-logo.png",
            "title": "Need for Speed Unbound",
            "author": "Criterion Games",
            "meta": "Vistas de 7M - Hace 2 anos"
        },
        {
            "thumb": "img/thumb/tc-motorfest.jpg",
            "price": "130,00 NZ",
            "logo": "img/video-game-logos/playStation-logo.svg",
            "title": "The Creew MotoSport",
            "author": "Xbox",
            "meta": "Vistas de 5M - Hace 2 anos"
        },
        {
            "thumb": "img/thumb/spider-man2.jpg",
            "price": "130,00 NZ",
            "logo": "img/video-game-logos/xbox-logo.svg",
            "title": "Amazing Spider Man II",
            "author": "PlayStation",
            "meta": "Vistas de 16M - Hace 3 anos"
        },
        {
            "thumb": "img/thumb/the-last-of-us-part-2-remastered.jpg",
            "price": "100,00 NZ",
            "logo": "img/video-game-logos/Rockstar_logo_for_tweets.png",
            "title": "EA Madden 25",
            "author": "RockStar Games",
            "meta": "Vistas de 9M - Hace 1 ano"
        },
        {
            "thumb": "img/thumb/ea-madden25.jpg",
            "price": "80,00 NZ",
            "logo": "img/video-game-logos/Electronic-Arts-Logo.svg",
            "title": "EA Madden 25",
            "author": "Electronic Arts",
            "meta": "Vistas de 4.6M - Hace 1 ano"
        },
        {
            "thumb": "img/thumb/cyberpunk-2077.jpg",
            "price": "60,00 NZ",
            "logo": "img/video-game-logos/CD-project.png",
            "title": "Cyberpunk 2077",
            "author": "CD Project",
            "meta": "Vistas de 25M - Hace 5 ano"
        },
        {
            "thumb": "img/thumb/Grand-theft-auto-5-online.jpg",
            "price": "100,00 NZ",
            "logo": "img/video-game-logos/Rockstar_logo_for_tweets.png",
            "title": "A Safehouse in the Hills",
            "author": "RockStar Games",
            "meta": "Vistas de 3M - Hace 2 meses"
        },
        {
            "thumb": "img/thumb/assassins-creed-shadows.jpg",
            "price": "80,00 NZ",
            "logo": "img/video-game-logos/playStation-logo.svg",
            "title": "Assassins Creed Shadows",
            "author": "PlayStaion",
            "meta": "Vistas de 6.8M - Hace 1 ano"
        },
        {
            "thumb": "img/thumb/street-fighter6.jpg",
            "price": "60,00 NZ",
            "logo": "img/video-game-logos/playStation-logo.svg",
            "title": "Street Figther VI",
            "author": "PlayStaion",
            "meta": "Vistas de 12.4M - Hace 1 ano"
        }
    ]

with app.app_context():
    for game in games:
        db.session.add(Game(**game))
    db.session.commit()