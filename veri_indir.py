"""
ÜNLÜ RESİMLERİ İNDİRİCİ - BING VERSİYONU
448 ünlü
Her ünlü için 7 resim
AI / Face Recognition Dataset için optimize
"""

def main():
    print("="*60)
    print("ÜNLÜ RESİMLERİ İNDİRME PROGRAMI (BING)")
    print("448 ünlü | Her ünlü için 7 resim")
    print("="*60)
    
    try:
        from bing_image_downloader import downloader
        print("✅ bing-image-downloader hazır!\n")
    except ImportError:
        print("❌ bing-image-downloader bulunamadı!")
        print("Kurulum: pip install bing-image-downloader")
        return
    
    import os
    from pathlib import Path
    
    base_dir = "ImagesAttendance"
    images_per_celebrity = 7
    
    Path(base_dir).mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Hedef klasör: {os.path.abspath(base_dir)}")
    print(f"📸 Her ünlü için: {images_per_celebrity} resim\n")
    
    celebrities = [
# --- ÖNCEKİ 208 ---
"Aaron Taylor-Johnson","Abel Tesfaye","Adriana Lima","Adele","Al Pacino","Alicia Keys","Amanda Seyfried","Andrew Garfield","Andy Serkis","Anne Hathaway",
"Anthony Hopkins","Anthony Mackie","Antonio Banderas","Ashton Kutcher","Awkwafina","Barry Keoghan","Bella Hadid","Ben Stiller","Bill Murray","Blake Lively",
"Bob Odenkirk","Bradley Cooper","Bruno Mars","Bryan Cranston","Cameron Diaz","Cara Delevingne","Cate Blanchett","Charlie Hunnam","Charlize Theron",
"Chiwetel Ejiofor","Christian Bale","Christina Aguilera","Christopher Nolan","Claire Danes","Colin Farrell","Conan O’Brien","Courteney Cox",
"Daniel Craig","Daniel Kaluuya","Daniel Radcliffe","Daisy Ridley","Dave Bautista","David Beckham","David Harbour","Demi Lovato","Dua Lipa",
"Eddie Murphy","Ed Sheeran","Eiza González","Ellen Pompeo","Emilia Clarke","Eminem","Eva Green","Eva Mendes","Evan Peters","Ewan McGregor",
"Finn Wolfhard","Forest Whitaker","Frances McDormand","Freddie Highmore","G-Eazy","Gary Oldman","Gigi Hadid","Gwyneth Paltrow",
"Hailee Steinfeld","Halle Berry","Harrison Ford","Hayley Williams","Hugh Jackman","Ian McKellen","Idris Elba","Isabela Merced",
"Jack Black","Jackie Chan","Jacob Elordi","Jaden Smith","Jamie Foxx","Jamie Dornan","Jane Fonda","Jared Leto","Jason Bateman","Jeff Goldblum",
"Jennifer Lawrence","Jesse Eisenberg","Jessica Alba","Jessica Chastain","Jim Carrey","Jodie Comer","John Boyega","John Cena","John Krasinski",
"John Legend","John Travolta","Johnny Galecki","Jon Hamm","Jonah Hill","Jordan Peele","Josh Brolin","Josh Hutcherson","Julia Roberts",
"Julianne Moore","Justin Bieber","Justin Timberlake","Kanye West","Karen Gillan","Kate Beckinsale","Kate Winslet","Kathy Bates","Kelly Clarkson",
"Kendall Jenner","Kerry Washington","Kevin Bacon","Kevin Hart","Kieran Culkin","Kim Kardashian","Kirsten Dunst","Kristen Stewart",
"Lady Gaga","Lakeith Stanfield","Lana Del Rey","Laura Dern","Laurence Fishburne","Leonardo Sbaraglia","Liam Hemsworth","Lily Collins",
"Linda Cardellini","Lizzo","Logan Lerman","Lupita Nyong’o","Madonna","Mahershala Ali","Mandy Moore","Marion Cotillard","Mark Wahlberg",
"Martin Freeman","Matthew McConaughey","Megan Fox","Melissa McCarthy","Michael B Jordan","Michael Fassbender","Michelle Yeoh","Mila Kunis",
"Miles Teller","Millie Bobby Brown","Minnie Driver","Monica Bellucci","Naomi Watts","Nicolas Cage","Nick Jonas","Nicki Minaj","Noah Centineo",
"Olivia Colman","Olivia Rodrigo","Oprah Winfrey","Orlando Bloom","Paris Hilton","Patricia Arquette","Penelope Cruz","Post Malone","Priyanka Chopra",
"Quentin Tarantino","Rami Malek","Rebel Wilson","Reese Witherspoon","Regina King","Riz Ahmed","Rosamund Pike","Russell Crowe","Ryan Gosling",
"Sabrina Carpenter","Sam Claflin","Sam Rockwell","Sarah Paulson","Saoirse Ronan","Scarlett Byrne","Seth Rogen","Shakira","Shawn Mendes",
"Sienna Miller","Simu Liu","Sofia Vergara","Sophie Turner","Stanley Tucci","Steve Carell","Steven Yeun","Sydney Sweeney","Taron Egerton",
"Taika Waititi","Tessa Thompson","Theo James","Tilda Swinton","Tim Allen","Tobey Maguire","Tom Hardy","Toni Collette","Tyler Perry",
"Uma Thurman","Vanessa Hudgens","Vin Diesel","Viola Davis","Walton Goggins","Wesley Snipes","Whoopi Goldberg","Winona Ryder",
"Woody Harrelson","Zac Efron","Zayn Malik","Zoe Kravitz",

# --- EK 240 ÜNLÜ (448 TAMAMLAMA) ---
"Alexandra Daddario","Ansel Elgort","Austin Butler","Ben Barnes","Brendan Fraser","Caleb McLaughlin","Cillian Murphy","Dacre Montgomery",
"Dan Stevens","Dev Patel","Dylan O’Brien","Eddie Redmayne","Elijah Wood","Emilia Jones","Ezra Miller","Freida Pinto",
"Henry Golding","Hero Fiennes Tiffin","Iain Armitage","James McAvoy","Jamie Campbell Bower","Joe Keery","Joel Edgerton",
"Joseph Gordon-Levitt","Justice Smith","Kit Harington","Luke Evans","Mads Mikkelsen","Nicholas Hoult","Paul Dano",
"Richard Madden","Sebastian Stan","Tom Holland","Will Poulter","Aaron Eckhart","Aishwarya Rai","Anya Chalotra",
"Awkwafina","Bae Suzy","Benedict Wong","Bruna Marquezine","Camila Mendes","Carlos PenaVega","Chadwick Boseman",
"Choi Woo-shik","Claudia Kim","Deepika Padukone","Donnie Yen","Fan Bingbing","Gong Yoo","Hiroyuki Sanada",
"Iko Uwais","Irrfan Khan","Jackson Wang","Jean Reno","Jet Li","Ji Chang-wook","Jung Hae-in",
"Ken Watanabe","Kim Soo-hyun","Lee Jong-suk","Liu Yifei","Maggie Q","Ma Dong-seok",
"Park Seo-joon","Rain","Song Kang","Son Ye-jin","Takeshi Kaneshiro","Tony Leung","Zhang Ziyi"
]
    
    

    print(f"👥 Toplam ünlü: {len(celebrities)}")
    print(f"📊 Toplam hedef resim: {len(celebrities) * images_per_celebrity}\n")
    
    input("Başlamak için ENTER'a basın...")
    print()
    
    success_count = 0
    failed_count = 0
    
    for idx, celebrity in enumerate(celebrities, 1):
        try:
            print(f"[{idx}/{len(celebrities)}] {celebrity}")
            
            downloader.download(
                celebrity + " face portrait",
                limit=images_per_celebrity,
                output_dir=base_dir,
                adult_filter_off=True,
                force_replace=False,
                timeout=30,
                verbose=False
            )
            
            success_count += 1
            print("   ✅ Tamamlandı\n")
        except Exception as e:
            failed_count += 1
            print(f"   ⚠️ Hata: {e}\n")
    
    print("="*60)
    print("✅ İNDİRME TAMAMLANDI")
    print("="*60)
    print(f"📁 Konum: {os.path.abspath(base_dir)}")
    print(f"📊 Başarılı: {success_count}/{len(celebrities)}")
    print(f"📸 Toplam hedef: {len(celebrities) * images_per_celebrity} resim")
    if failed_count:
        print(f"⚠️ Başarısız: {failed_count}")
    print("="*60)

if __name__ == "__main__":
    main()
