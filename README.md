# Bu proje sadece azimle s*** taşı deler diyenler içindir!!!
  Öncelikle se lam lar. Bu proje napsamda ne etsemde şu kripto piyasasını otomatik hale getirsem diyen mühendislerin var olduğunun kanıtıdır. Amaç algoritmik trade yapabilmek için machine learning kullanarak bu alım satım işlerini otomatize edip sandalyede şöyle bir arkaya yaslanmaktır. Eğerki bu yazıyı okudun ve " ULAN bende aynısını yapcaktım" diyosan her türlü katkıya açığız. Pull request atman yeterli. Ama diyosan ki " Ben buraya katkı için değil sizin sistemi bi deniyip çalışıyosa kullanmaya geldim."  tamam sıkantı yok tepe tepe kullan. 
# Basitçe Kurulumu
- conifg.py isimli bir dosya oluşturun ve içine alttaki yapıyı koruyarak kendi bilgilerinizi ve birim seçimlerinizi yerleştirin.
    
        COIN_CHOICES = [('ETHUSDT'), ('BTCUSDT')]
        INTERVAL_CHOICES = [ ('15MIN'), ('1HOUR'),('4HOUR'),('1DAY')]
            class Config(object):
                API_KEY = 'aaaaaa'
                API_SECRET = 'aaaaaa'
                SECRET_KEY = '#$%^&*'

- Sistem için gerekli olan python paketlerini aşağıdaki komut ile yükleyin.

        pip install -r requirements.txt

- Make scripti ile uygulama için gerekli docker işlemlerini gerçekleştirmeliyiz. Önce postgre imajı çekelim:
`docker pull postgres:latest`
- Daha sonra `make start` komutu ile docker container'kari ayaga kaldiralim, gerekli ENV VARs icin `start-script` dosyasini guncelleyebiliriz.
- 

- Flaskın çalışması için gerekli olan bazı enviromental variable ları sisteme elle de tanitabiliriz.
    - Ubuntu/MacOs
	
            export FLASK_APP=flaskr
            export FLASK_ENV=development
            flask run
    - Windows
	
            set FLASK_APP=flaskr
            set FLASK_ENV=development
            flask run
- Hayırlı olsun aşamasına geçebiliriz.
# Bazı API endpointleri
- /dataref/
	- Bu endpointi kullanarak config.py dosyası içinde tanımlamış olduğumuz birimler için binance.api üzerinden mum verisi indirilebilir.
   
- /process/
   	- Bu endpoint ise dataların küçültülmesi ve machine learning modellerine uygun hale getirilmesi gibi data işleme fonksiyonlarının bulunduğu yerdir.
   	
# Bu arada öğrenci olduğumu söylemiş miydim??
 Evet hocam öğrenciyim. Olurda bi ekibe katkım olsun, bu çocuklar ne yiyip ne içiyolar dolar olmuş.... 
 
 Adresim bu--> 0xe4e4527825311aa9a0c459c1481dd0514359eae9
 
 Burdan yardımcı olabilirsin. 
 
 Ha " Ben daha kripto miripto yeniyim usta " diyosan da bana referral olursan çok sevinirim. %10 sana %10 bana şeklinde bir link bırakıyorum aşağıya hemen. Bu link üzerinden kayıt olursan yaptığın işlemlerdeki işlem ücretinin %10 unu kendine %10 unu da kendine kazandırmış olursun kiii nerden baksan mantıklı iş.
 
 https://accounts.binance.me/en/register?ref=M1RRIYQ7
 
 
