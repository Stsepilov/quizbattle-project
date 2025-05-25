"""add initial data

Revision ID: 1111_add_initial_data
Revises: 1a3739475972
Create Date: 2025-05-21 13:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1111_add_initial_data'
down_revision = '1a3739475972'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
                INSERT INTO quiz (id, title, description, image_url) VALUES
                (1, 'Лучшие автомобили','Какой автомобиль самый стильный?','https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bWVyY2VkZXN8ZW58MHx8MHx8fDA%3Da'),
                (2, 'Топ фильмов всех времен','Какой фильм достоин звания "шедевр"?','https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_66dd838683f0604cbb71b9cd_66e55ce99494bc23ba222cdf/scale_1200'),
                (3, 'Лучшие города для жизни', 'Где бы вы хотели жить?', 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8dG9reW98ZW58MHx8MHx8fDA%3D'),
                (4,'Лучшие смартфоны', 'Какой телефон заслуживает корону?', 'https://images.unsplash.com/photo-1591337676887-a217a6970a8a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8aXBob25lfGVufDB8fDB8fHww'),
                (5,'Вкуснейшие десерты', 'Что выберете для завершения ужина?', 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dGlyYW1pc3V8ZW58MHx8MHx8fDA%3D'),
                (6,'Легендарные рок-группы', 'Кто король рок-н-ролла?', 'https://images.unsplash.com/photo-1601779436248-4c269c0a0793?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8YmVhdGxlc3xlbnwwfHwwfHx8MA%3D%3D'),
                (7,'Красивейшие места природы', 'Где самые захватывающие пейзажи?', 'https://images.unsplash.com/photo-1615551043360-33de8b5f410c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z3JhbmQlMjBjYW55b258ZW58MHx8MHx8fDA%3D'),
                (8,'Лучшие книги XX века', 'Какая книга изменила ваше мышление?', 'https://images.unsplash.com/photo-1622609184693-58079bb6742f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8MTk4NCUyMGJvb2t8ZW58MHx8MHx8fDA%3D');
            """)

    op.execute("""
                INSERT INTO quiz_item (quiz_id, image_url, wins, losses, title) VALUES
                (1,'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8bWVyY2VkZXN8ZW58MHx8MHx8fDA%3D',0,0,'Mercedes'),
                (1,'https://images.unsplash.com/photo-1617531653332-bd46c24f2068?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGJtd3xlbnwwfHwwfHx8MA%3D%3D',0,0,'BMW'),
                (1,'https://images.unsplash.com/photo-1606152421802-db97b9c7a11b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGF1ZGl8ZW58MHx8MHx8fDA%3D',0,0,'Audi'),
                (1,'https://images.unsplash.com/photo-1560958089-b8a1929cea89?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8dGVzbGF8ZW58MHx8MHx8fDA%3D',0,0,'Tesla'),
                (1,'https://images.unsplash.com/photo-1580274455191-1c62238fa333?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cG9yc2NoZXxlbnwwfHwwfHx8MA%3D%3D',0,0, 'Porsche'),
                (1,'https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bGFtYm9yZ2hpbml8ZW58MHx8MHx8fDA%3D',0,0, 'Lamborghini'),
                (1,'https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZmVycmFyaXxlbnwwfHwwfHx8MA%3D%3D',0,0,'Ferrari'),
                (1,'https://images.unsplash.com/photo-1577496550006-f24a50e9d50c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8bGV4dXN8ZW58MHx8MHx8fDA%3D',0,0,'Lexus'),
                (1,'https://images.unsplash.com/photo-1604054094723-3a949e4a8993?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8cmFuZ2UlMjByb3ZlcnxlbnwwfHwwfHx8MA%3D%3',0,0,'Range Rover'),
                (1,'https://images.unsplash.com/photo-1584345604476-8ec5e12e42dd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8bXVzdGFuZ3xlbnwwfHwwfHx8MA%3D%3D',0,0,'Mustang'),
                (2,'https://voiretmanger.fr/wp-content/uploads/2014/07/parrain-coppola-marlon-brando.jpg',0,0,'Godfather'),
                (2,'https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_6706e68560479e7c51aee94b_6706eac95c5e4f1cf481f2df/scale_1200',0,0,'Shawshank'),
                (2,'https://img.championat.com/i/m/q/1671633909862479295.jpg',0,0,'Pulp Fiction'),
                (2,'https://i.ytimg.com/vi/Gwbc4UFaJow/maxresdefault.jpg',0,0,'Dark Knight'),
                (2,'https://wallpaper.forfun.com/fetch/3d/3dbd09e4e0558eb22051addaa6efa2e6.jpeg',0,0, 'Inception'),
                (2,'https://pic.rutubelist.ru/video/f2/b2/f2b2aac158ac7367281738025c4a97d1.jpg',0,0, 'Matrix'),
                (2,'https://m.media-amazon.com/images/S/pv-target-images/28ad5a615d61071e9d1aebbf684c89fcc3a8c5b3528d8ba778bb13198764d840.jpg',0,0,'Forrest Gump'),
                (2,'https://avatars.mds.yandex.net/i?id=a7b9f2ac4e50849e51632310ff56ce5b_l-4818427-images-thumbs&n=13',0,0,'Fight Club'),
                (2,'https://avatars.mds.yandex.net/i?id=6445babe269d98eedeabf89045635d18_l-5175149-images-thumbs&n=13',0,0,'Interstellar'),
                (2,'https://i.ytimg.com/vi/FN09XvCpeAA/maxresdefault.jpg',0,0,'Schindlers List'),
                (3,'https://avatars.mds.yandex.net/i?id=3147d20501f7dfea79e78ab959ae031f_l-10289673-images-thumbs&n=13',0,0,'Tokyo'),
                (3,'https://i.pinimg.com/originals/25/78/73/257873870f4a2b84be919b5602c6f7a8.jpg',0,0,'Vienna'),
                (3,'https://avatars.dzeninfra.ru/get-zen_doc/1595469/pub_64d7265ed5a4066e1ad7851c_64d7942e60b16c687fc69a63/scale_1200',0,0,'Zurich'),
                (3,'https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1uTSvI.img?w=1860&h=1200&m=4&q=74',0,0,'Singapore'),
                (3,'https://avatars.mds.yandex.net/i?id=e151b7476776aa2826a40877c8649eab_l-9245081-images-thumbs&n=13',0,0, 'Osaka'),
                (3,'https://avatars.mds.yandex.net/i?id=4a8cc89f6f8055fa0c718c772fb95729_l-6475641-images-thumbs&n=13',0,0, 'Munich'),
                (3,'https://img.championat.com/i/u/a/17278472131631175323.jpg',0,0,'Vancouver'),
                (3,'https://www.lot.com/content/dam/lot/lot-com/destination-photos/dania/GettyImages-173673114_cph.coreimg.jpg/1723626010982/GettyImages-173673114_cph.jpg',0,0,'Copenhagen'),
                (3,'https://sun9-58.userapi.com/impg/aDzR90tGPe9UzXiBrjYqoBezwdFwS1-5hykZBA/9klWASYJZVs.jpg?size=1200x800&quality=95&sign=6599c42237c03f984760a13346f1f43e&type=album',0,0,'Sydney'),
                (3,'https://cdn.culture.ru/images/158ea53d-85cb-5525-ab17-a8b383d562ce',0,0,'Moscow'),
                (4, 'https://avatars.mds.yandex.net/i?id=f112248cea4cf39a0a48a680e2a7c426_l-7006309-images-thumbs&n=13', 0, 0, 'Nokia'),
                (4, 'https://img.baba-blog.com/2024/05/Sony-Xperia-1-VI.jpg?x-oss-process=style%2Ffull', 0, 1, 'Sony Xperia'),
                (4, 'https://ogo1.ru/upload/iblock/7a4/7a4ad0322a65e3c00e668723d48db241.jpeg', 0, 1, 'Asus Zenfone'),
                (4, 'https://content.onliner.by/news/1100x5616/530f49d5c9336e7392ad5a633c7b25cd.jpg', 0, 1, 'Huawei'),
                (4, 'https://goodmi.ru/images/cp_blog_post/114/1_v4jm-7i.jpg', 0, 1, 'Xiaomi'),
                (4, 'https://technoimpuls.by/pics/items/20240718110716788_New-Project.jpg', 0, 1, 'Oneplus'),
                (4, 'https://www.ixbt.com/img/n1/news/2022/9/3/OPPO-A77s-_large.jpg', 0, 1, 'Oppo'),
                (4, 'https://static.tildacdn.com/tild6466-6461-4236-b134-346166313065/Apple-iPhone-16-fini.png', 0, 1, 'Iphone'),
                (4, 'https://avatars.mds.yandex.net/i?id=a088b17af696f8b5fcaea06d76ff7e4d_l-10595999-images-thumbs&n=13', 0, 1, 'Samsung Galaxy'),
                (4, 'https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_66cb792e6e0d2e2fbeee6033_66cb79366e0d2e2fbeee6266/scale_1200', 1, 0, 'Google Pixel'),
                (5, 'https://image.mel.fm/i/b/b6J5FH4G6O/1280.jpg', 0, 0, 'Tiramisu'),
                (5, 'https://avatars.mds.yandex.net/i?id=d1ef9399714a2b63c7a769744b27559c_l-5338985-images-thumbs&n=13', 0, 0, 'Cheesecake'),
                (5, 'https://avatars.mds.yandex.net/i?id=53dcafd67d01845e46a3670d53cccba3c1bd7ded-5008718-images-thumbs&n=13', 0, 0, 'Chocolate Cake'),
                (5, 'https://aif-s3.aif.ru/images/026/171/55cf0a51079c9bff9cffd9a9b562f459.jpg', 0, 0, 'Macarons'),
                (5, 'https://avatars.mds.yandex.net/i?id=90e5e57700a7d6e3cd4d58f567dafc76_l-8454246-images-thumbs&n=13', 0, 0, 'Ice Cream'),
                (5, 'https://static.insales-cdn.com/r/S92c21gMT30/rs:fit:800:0:1/q:100/plain/images/articles/1/4581/1978853/10785_eggnog_creme_brulee-2000x1333.jpg@jpg', 0, 0, 'Creme Brulee'),
                (5, 'https://avatars.mds.yandex.net/i?id=f266c2a8a13cf130790204ed05717e74_l-5233258-images-thumbs&n=13', 0, 0, 'Apple Pie'),
                (5, 'https://i.pinimg.com/originals/37/5f/02/375f0249bb9f7b9c4daaa2c8ed41436a.jpg', 0, 0, 'Panna Cotta'),
                (5, 'https://avatars.mds.yandex.net/i?id=9432f0cad0bfcbcec50a9b4964255687_l-5870227-images-thumbs&n=13', 0, 0, 'Churros'),
                (5, 'https://avatars.mds.yandex.net/i?id=bc907a4624bc16fe177aa65c3be298c0_l-5173525-images-thumbs&n=13', 0, 0, 'Red Velvet'),
                (6, 'https://avatars.mds.yandex.net/i?id=baea8200f8c5b2ba34bca90c50f3dd7c_l-10672158-images-thumbs&n=13', 0, 0, 'Rolling Stones'),
                (6, 'https://i.pinimg.com/originals/ca/8d/27/ca8d279f42e2622630d7ea4939054283.jpg', 0, 1, 'Queen'),
                (6, 'https://www.rockfm.ru/uploads/photos/1/2020/11/ACDC-press-pic.jpg', 0, 1, 'AC/DC'),
                (6, 'https://avatars.mds.yandex.net/i?id=67739c369f5a1a0d2a86b94b7323199f_l-5282838-images-thumbs&n=13', 0, 1, 'Beatles'),
                (6, 'https://avatars.mds.yandex.net/get-kinopoisk-image/4774061/63cb1f7d-48cf-489b-877b-8070e5da5403/1920x', 0, 1, 'The Doors'),
                (6, 'https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_66b5e7b398b8b550787aab68_66c4972dafc77301db7403f2/scale_1200', 0, 1, 'Guns N Roses'),
                (6, 'https://i.ytimg.com/vi/lXQqLMRJsc8/maxresdefault.jpg', 0, 1, 'Metallica'),
                (6, 'https://avatars.mds.yandex.net/i?id=b1069aa8d064ad631bea67d86a1eb6fc_l-13125018-images-thumbs&n=13', 0, 1, 'Led Zeppelin'),
                (6, 'https://www.castlerock.ru/upload/resize_cache/iblock/766/1140_452_2/766969e5c88b76a83459945cb83407a8.jpg', 0, 1, 'Pink Floyd'),
                (6, 'https://cs9.pikabu.ru/post_img/2017/07/03/7/og_og_1499083162243412352.jpg', 1, 0, 'Nirvana'),
                (7, 'https://avatars.mds.yandex.net/i?id=4c687c94f0c5734a201ff40845e27c0d_l-5179059-images-thumbs&n=13', 0, 0, 'Amazon Rainforest'),
                (7, 'https://avatars.mds.yandex.net/i?id=402a480b1d42d75bef4d274148c7755c_l-8220915-images-thumbs&n=13', 0, 1, 'Mount Everest'),
                (7, 'https://cdn.culture.ru/images/3c808f6f-0383-520c-8f90-42d323df9339', 0, 1, 'Baikal Lake'),
                (7, 'https://i0.wp.com/www.australiangeographic.com.au/wp-content/uploads/2023/08/620573-56-scaled.jpg?fit=2560%2C1697&ssl=1', 0, 1, 'Great Barrier Reef'),
                (7, 'https://avatars.mds.yandex.net/i?id=782046c7d1c21bd687b6d5318403f591_l-12768700-images-thumbs&n=13', 0, 1, 'Grand Canyon'),
                (7, 'https://cdn.getyourguide.com/img/tour/8ec926febf22db49.jpeg/148.jpg', 0, 1, 'Victoria Falls'),
                (7, 'https://avatars.mds.yandex.net/get-mpic/2016828/img_id3877966895425277084.jpeg/orig', 0, 1, 'Yosemite'),
                (7, 'https://i3.wp.com/priroda.club/uploads/posts/2023-10/1697885833_priroda-club-p-severnoe-siyanie-nad-oblakami-pinterest-34.jpg?ssl=1', 0, 1, 'Northern Lights'),
                (7, 'https://news-img.gismeteo.st/ru/2023/05/shutterstock_768360604.jpg', 0, 1, 'Sahara Desert'),
                (7, 'https://avatars.mds.yandex.net/i?id=d7596e93a39e52667474386766a6c4dd_l-4577841-images-thumbs&n=13', 1, 0, 'Banff National Park'),
                (8, 'https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_66a896bc2c44ad659cc6d1a7_66a8993aadc91e18bbd96624/scale_1200', 0, 0, 'Brave New World'),
                (8, 'https://i.ytimg.com/vi/_j3uB-O158U/maxresdefault.jpg', 0, 1, 'The Catcher In The Rye'),
                (8, 'https://cdn1.ozone.ru/s3/multimedia-y/6353881258.jpg', 0, 1, '1984 Book'),
                (8, 'https://static10.labirint.ru/books/966431/cover.jpg', 0, 1, 'The Great Gatsby'),
                (8, 'https://pictures.abebooks.com/inventory/22455734823.jpg', 0, 1, 'One Hundred Years Of Solitude'),
                (8, 'https://sun9-38.userapi.com/impg/bB6XiJX3nseMmSIhS2d0WrbP404dgo', 0,1,'Lord Of The Rings'),
                (8,'https://avatars.mds.yandex.net/i?id=cc266a4b6d9eb82ddd4b15e5b720fe8d_l-5221353-images-thumbs&n=13',0,1,'Anna Karenina'),
                (8,'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg/640px-To_Kill_a_Mockingbird_%28first_edition_cover%29.jpg',0,1,'To Kill A Mockingbird'),
                (8,'https://img-s1.onedio.com/id-590e5090992b4515140c944e/rev-0/w-1200/h-1809/f-jpg/s-62541199e946e7a7901c4a0a9db3f1d2b5bf1d7a.jpg',0,1,'The Bell Jar'),
                (8,'https://i.pinimg.com/736x/97/9d/03/979d036f42a9ad54d619663e0c5c42ba.jpg',0,1,'Crime And Punishment');
            """)
