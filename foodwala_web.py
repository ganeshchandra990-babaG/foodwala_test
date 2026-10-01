from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser
import os
import urllib.request


# ============================================================
# FOODWALA - REAL RIDER IMAGE
# ============================================================

IMAGE_URL = (
    "https://images.unsplash.com/"
    "photo-4y4AvfyJk7g"
)

# Direct image URL used for the local copy
IMAGE_URL = (
    "https://images.unsplash.com/"
    "photo-4y4AvfyJk7g"
    "?auto=format&fit=crop&w=1200&q=85"
)

IMAGE_FILE = "rider.jpg"


def download_rider_image():

    if os.path.exists(IMAGE_FILE):
        print("✓ FOODWALA rider image already exists.")
        return

    print("Downloading rider photograph...")

    try:

        urllib.request.urlretrieve(
            IMAGE_URL,
            IMAGE_FILE
        )

        print("✓ Rider photograph downloaded.")

    except Exception as e:

        print("⚠ Could not download rider photograph.")
        print("Error:", e)


download_rider_image()


# ============================================================
# WEBSITE
# ============================================================

HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>FOODWALA - Food Delivery</title>


<style>

/* ============================================================
   RESET
============================================================ */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}


body {

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    background: #fff8f2;

    color: #333;
}


/* ============================================================
   HEADER
============================================================ */

header {

    height: 75px;

    background:
        linear-gradient(
            90deg,
            #ff512f,
            #ff7043
        );

    color: white;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 0 7%;

    box-shadow:
        0 3px 12px
        rgba(0,0,0,0.18);

    position: sticky;

    top: 0;

    z-index: 1000;
}


.logo {

    font-size: 30px;

    font-weight: bold;

    letter-spacing: 1px;
}


.logo span {

    color: #ffe082;
}


.order-status {

    background: white;

    color: #ff5722;

    padding:
        11px 22px;

    border-radius: 25px;

    font-weight: bold;

    cursor: pointer;

    transition: 0.3s;
}


.order-status:hover {

    background: #ffe082;

    color: #333;
}


/* ============================================================
   HERO
============================================================ */

.hero {

    min-height: 430px;

    background:

        linear-gradient(
            135deg,
            #ff512f,
            #ff7043,
            #ff9800
        );

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding:
        40px 8%;

    color: white;
}


.hero-text {

    width: 45%;
}


.hero-text h1 {

    font-size: 48px;

    line-height: 1.15;

    margin-bottom: 20px;
}


.hero-text p {

    font-size: 20px;

    line-height: 1.6;
}


/* ============================================================
   RIDER PHOTO AREA
============================================================ */

.rider {

    width: 50%;

    display: flex;

    justify-content: center;

    align-items: center;
}


.rider-photo-container {

    position: relative;

    width: 100%;

    max-width: 570px;
}


.rider-photo {

    width: 100%;

    height: 330px;

    object-fit: cover;

    border-radius: 25px;

    border:
        5px solid
        rgba(255,255,255,0.9);

    box-shadow:
        0 15px 35px
        rgba(0,0,0,0.30);

    display: block;
}


/* ============================================================
   FOODWALA DELIVERY BOX
============================================================ */

.foodwala-box {

    position: absolute;

    right: 28px;

    bottom: 25px;

    width: 175px;

    height: 115px;

    background:
        linear-gradient(
            135deg,
            #ff5722,
            #d84315
        );

    border-radius: 12px;

    border:
        4px solid white;

    color: white;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;

    box-shadow:
        0 8px 22px
        rgba(0,0,0,0.40);

    transform: rotate(-2deg);

    z-index: 5;
}


.foodwala-logo {

    width: 38px;

    height: 38px;

    background: white;

    color: #ff5722;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 21px;

    margin-bottom: 3px;
}


.foodwala-name {

    font-size: 19px;

    font-weight: 900;

    letter-spacing: 1px;
}


.foodwala-tagline {

    font-size: 8px;

    font-weight: bold;

    letter-spacing: 0.8px;

    margin-top: 3px;

    color: #ffe0b2;
}


/* ============================================================
   SEARCH
============================================================ */

.search-section {

    background: white;

    width: 85%;

    margin:
        -35px auto
        45px;

    padding: 25px;

    border-radius: 15px;

    box-shadow:
        0 5px 25px
        rgba(0,0,0,0.15);

    position: relative;

    z-index: 10;
}


.search-box {

    display: flex;

    gap: 15px;
}


.search-box input {

    flex: 1;

    padding: 16px;

    border:
        2px solid
        #eeeeee;

    border-radius: 8px;

    font-size: 16px;

    outline: none;
}


.search-box input:focus {

    border-color:
        #ff5722;
}


.search-btn {

    background:
        #ff5722;

    color: white;

    border: none;

    padding:
        0 32px;

    border-radius: 8px;

    font-size: 17px;

    font-weight: bold;

    cursor: pointer;
}


.search-btn:hover {

    background:
        #e64a19;
}


/* ============================================================
   GENERAL SECTIONS
============================================================ */

.section {

    width: 85%;

    margin:
        45px auto;
}


.section-title {

    font-size: 28px;

    margin-bottom: 25px;
}


.section-title span {

    color:
        #ff5722;
}


/* ============================================================
   FOOD CATEGORIES
============================================================ */

.categories {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(150px, 1fr)
        );

    gap: 20px;
}


.food-card {

    background: white;

    border-radius: 15px;

    padding: 15px;

    text-align: center;

    box-shadow:
        0 4px 15px
        rgba(0,0,0,0.08);

    cursor: pointer;

    transition: 0.3s;
}


.food-card:hover {

    transform:
        translateY(-7px);

    box-shadow:
        0 8px 25px
        rgba(0,0,0,0.15);
}


.food-image {

    width: 120px;

    height: 120px;

    margin:
        auto auto 12px;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 65px;

    background:
        #fff3e0;
}


.food-card h3 {

    color:
        #444;
}


/* ============================================================
   RESTAURANTS
============================================================ */

.offers {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(280px, 1fr)
        );

    gap: 25px;
}


.restaurant {

    background: white;

    border-radius: 15px;

    overflow: hidden;

    box-shadow:
        0 5px 20px
        rgba(0,0,0,0.1);

    transition: 0.3s;
}


.restaurant:hover {

    transform:
        translateY(-6px);
}


.restaurant-image {

    height: 190px;

    display: flex;

    justify-content: center;

    align-items: center;

    font-size: 85px;

    background:
        linear-gradient(
            135deg,
            #ffcc80,
            #ff7043
        );
}


.restaurant-content {

    padding: 20px;
}


.restaurant-content h3 {

    font-size: 22px;

    margin-bottom: 8px;
}


.restaurant-content p {

    color: #777;

    margin-bottom: 14px;
}


.offer {

    display: inline-block;

    background:
        #fff0e8;

    color:
        #e64a19;

    padding:
        8px 12px;

    border-radius: 6px;

    font-weight: bold;
}


.order-btn {

    float: right;

    background:
        #ff5722;

    color: white;

    border: none;

    padding:
        8px 15px;

    border-radius: 6px;

    cursor: pointer;
}


.order-btn:hover {

    background:
        #e64a19;
}


/* ============================================================
   SPECIAL OFFER
============================================================ */

.banner {

    background:

        linear-gradient(
            135deg,
            #ff5722,
            #ff9800
        );

    color: white;

    border-radius: 18px;

    padding: 35px;

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-top: 35px;
}


.banner h2 {

    font-size: 30px;

    margin-bottom: 10px;
}


.banner button {

    background: white;

    color:
        #ff5722;

    border: none;

    padding:
        13px 25px;

    border-radius: 8px;

    font-weight: bold;

    cursor: pointer;
}


/* ============================================================
   FOOTER
============================================================ */

footer {

    background:
        #252525;

    color: white;

    margin-top: 70px;

    padding:
        50px 8% 25px;
}


.footer-content {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(200px, 1fr)
        );

    gap: 40px;
}


footer h3 {

    color:
        #ff7043;

    margin-bottom: 15px;
}


footer p {

    color: #ccc;

    line-height: 1.8;
}


.footer-bottom {

    border-top:
        1px solid #444;

    margin-top: 35px;

    padding-top: 20px;

    text-align: center;

    color: #aaa;
}


/* ============================================================
   MOBILE
============================================================ */

@media(max-width: 768px) {

    header {

        padding:
            0 20px;
    }


    .logo {

        font-size: 23px;
    }


    .order-status {

        padding:
            9px 14px;

        font-size: 13px;
    }


    .hero {

        flex-direction:
            column;

        text-align:
            center;

        padding:
            40px 20px;
    }


    .hero-text {

        width: 100%;

        margin-bottom:
            30px;
    }


    .hero-text h1 {

        font-size:
            35px;
    }


    .rider {

        width: 100%;
    }


    .rider-photo {

        height:
            270px;
    }


    .foodwala-box {

        right: 15px;

        bottom: 15px;

        width: 145px;

        height: 95px;
    }


    .foodwala-name {

        font-size:
            16px;
    }


    .search-box {

        flex-direction:
            column;
    }


    .search-btn {

        padding:
            15px;
    }


    .banner {

        flex-direction:
            column;

        text-align:
            center;

        gap: 20px;
    }

}

</style>

</head>


<body>


<!-- ============================================================
     HEADER
============================================================ -->

<header>

    <div class="logo">

        🍴 FOOD<span>WALA</span>

    </div>


    <div
        class="order-status"
        onclick="checkOrder()">

        📦 Order Status

    </div>

</header>



<!-- ============================================================
     HERO
============================================================ -->

<section class="hero">


    <div class="hero-text">

        <h1>

            Delicious Food,
            Delivered Fast! 🍔

        </h1>


        <p>

            Discover your favourite food
            from the best restaurants around you.

            Order delicious meals and enjoy
            them at your doorstep.

        </p>

    </div>



    <div class="rider">

        <div class="rider-photo-container">


            <!-- REAL RIDER PHOTOGRAPH -->

            <img
                class="rider-photo"
                src="/rider.jpg"
                alt="FOODWALA Delivery Rider">



            <!-- =================================================
                 FOODWALA OWN BRANDING
            ================================================== -->

            <div class="foodwala-box">


                <div class="foodwala-logo">

                    🍴

                </div>


                <div class="foodwala-name">

                    FOODWALA

                </div>


                <div class="foodwala-tagline">

                    DELIVERING HAPPINESS

                </div>


            </div>


        </div>

    </div>

</section>



<!-- ============================================================
     SEARCH
============================================================ -->

<section class="search-section">

    <div class="search-box">


        <input
            type="text"
            id="foodSearch"
            placeholder="🔍 Search food item...">


        <input
            type="text"
            id="location"
            placeholder="📍 Enter location">


        <button
            class="search-btn"
            onclick="searchFood()">

            Search

        </button>


    </div>

</section>



<!-- ============================================================
     FOOD CATEGORIES
============================================================ -->

<section class="section">


    <h2 class="section-title">

        What are you
        <span>Craving?</span> 😋

    </h2>



    <div class="categories">


        <div
            class="food-card"
            onclick="selectFood('Biryani')">

            <div class="food-image">
                🍛
            </div>

            <h3>
                Biryani
            </h3>

        </div>



        <div
            class="food-card"
            onclick="selectFood('Veg Thali')">

            <div class="food-image">
                🍱
            </div>

            <h3>
                Veg Thali
            </h3>

        </div>



        <div
            class="food-card"
            onclick="selectFood('Pizza')">

            <div class="food-image">
                🍕
            </div>

            <h3>
                Pizza
            </h3>

        </div>



        <div
            class="food-card"
            onclick="selectFood('Burger')">

            <div class="food-image">
                🍔
            </div>

            <h3>
                Burger
            </h3>

        </div>



        <div
            class="food-card"
            onclick="selectFood('Desserts')">

            <div class="food-image">
                🍰
            </div>

            <h3>
                Desserts
            </h3>

        </div>



        <div
            class="food-card"
            onclick="selectFood('Chinese')">

            <div class="food-image">
                🍜
            </div>

            <h3>
                Chinese
            </h3>

        </div>


    </div>

</section>



<!-- ============================================================
     RESTAURANT OFFERS
============================================================ -->

<section class="section">


    <h2 class="section-title">

        🔥 Today's
        <span>Restaurant Offers</span>

    </h2>



    <div class="offers">


        <div class="restaurant">


            <div class="restaurant-image">

                🍛

            </div>


            <div class="restaurant-content">

                <h3>
                    Spice Garden
                </h3>


                <p>
                    Authentic Indian cuisine
                    and delicious biryani.
                </p>


                <span class="offer">
                    40% OFF
                </span>


                <button
                    class="order-btn"
                    onclick="orderNow('Spice Garden')">

                    Order

                </button>

            </div>

        </div>



        <div class="restaurant">


            <div
                class="restaurant-image"
                style="
                    background:
                    linear-gradient(
                        135deg,
                        #ffecb3,
                        #ff9800
                    );
                ">

                🍕

            </div>


            <div class="restaurant-content">

                <h3>
                    Food Paradise
                </h3>


                <p>
                    Delicious meals prepared
                    fresh every day.
                </p>


                <span class="offer">
                    30% OFF
                </span>


                <button
                    class="order-btn"
                    onclick="orderNow('Food Paradise')">

                    Order

                </button>

            </div>

        </div>



        <div class="restaurant">


            <div
                class="restaurant-image"
                style="
                    background:
                    linear-gradient(
                        135deg,
                        #ffccbc,
                        #e64a19
                    );
                ">

                🍽️

            </div>


            <div class="restaurant-content">

                <h3>
                    Royal Kitchen
                </h3>


                <p>
                    Royal Indian flavours
                    delivered to your door.
                </p>


                <span class="offer">
                    BUY 1 GET 1
                </span>


                <button
                    class="order-btn"
                    onclick="orderNow('Royal Kitchen')">

                    Order

                </button>

            </div>

        </div>


    </div>



    <!-- SPECIAL OFFER -->

    <div class="banner">


        <div>

            <h2>
                🎉 Special Weekend Offer!
            </h2>


            <p>
                Get up to 50% OFF on selected restaurants.
            </p>

        </div>


        <button
            onclick="claimOffer()">

            Claim Offer

        </button>


    </div>


</section>



<!-- ============================================================
     FOOTER
============================================================ -->

<footer>


    <div class="footer-content">


        <div>

            <h3>
                🍴 FOODWALA
            </h3>


            <p>
                Your favourite food,
                delivered right to your doorstep.
            </p>

        </div>



        <div>

            <h3>
                Company
            </h3>


            <p>About Us</p>

            <p>Careers</p>

            <p>Restaurants</p>

            <p>Partner With Us</p>

        </div>



        <div>

            <h3>
                Help
            </h3>


            <p>Customer Support</p>

            <p>Order Tracking</p>

            <p>FAQs</p>

            <p>Terms & Conditions</p>

        </div>



        <div>

            <h3>
                Contact Us
            </h3>


            <p>
                📞 +91 98765 43210
            </p>

            <p>
                📧 support@foodwala.com
            </p>

            <p>
                📍 New Delhi, India
            </p>

        </div>


    </div>



    <div class="footer-bottom">

        © 2026 FOODWALA.
        All Rights Reserved.

    </div>


</footer>



<!-- ============================================================
     JAVASCRIPT
============================================================ -->

<script>


function searchFood() {

    let food =
        document
        .getElementById("foodSearch")
        .value
        .trim();


    let location =
        document
        .getElementById("location")
        .value
        .trim();


    if (food === "") {

        alert(
            "Please enter a food item."
        );

        return;
    }


    if (location === "") {

        alert(
            "Please enter your location."
        );

        return;
    }


    alert(
        "🔍 Searching for " +
        food +
        " near " +
        location +
        "..."
    );

}



function selectFood(food) {

    document
        .getElementById("foodSearch")
        .value = food;


    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

}



function orderNow(restaurant) {

    alert(
        "🍽️ Thank you! You selected " +
        restaurant +
        "."
    );

}



function claimOffer() {

    alert(
        "🎉 Congratulations! " +
        "Your special offer has been claimed."
    );

}



function checkOrder() {

    alert(
        "📦 Order Status: " +
        "No active orders."
    );

}


</script>


</body>

</html>
"""


# ============================================================
# PYTHON SERVER
# ============================================================

class WebsiteHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        # -----------------------------
        # HOME PAGE
        # -----------------------------

        if self.path == "/":

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "text/html; charset=utf-8"
            )

            self.end_headers()

            self.wfile.write(
                HTML.encode("utf-8")
            )

            return


        # -----------------------------
        # RIDER IMAGE
        # -----------------------------

        if self.path == "/rider.jpg":

            try:

                with open(
                    IMAGE_FILE,
                    "rb"
                ) as image:

                    data = image.read()


                self.send_response(200)

                self.send_header(
                    "Content-Type",
                    "image/jpeg"
                )

                self.send_header(
                    "Content-Length",
                    str(len(data))
                )

                self.end_headers()

                self.wfile.write(data)


            except FileNotFoundError:

                self.send_response(404)

                self.end_headers()

                self.wfile.write(
                    b"Rider image not found."
                )

            return


        # -----------------------------
        # 404
        # -----------------------------

        self.send_response(404)

        self.send_header(
            "Content-Type",
            "text/plain; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            b"Page not found"
        )


# ============================================================
# START SERVER
# ============================================================

HOST = "127.0.0.1"
PORT = 8000


server = HTTPServer(
    (HOST, PORT),
    WebsiteHandler
)


url = f"http://{HOST}:{PORT}"


print()
print("=" * 60)
print("                 FOODWALA")
print("=" * 60)
print()
print(f"Website: {url}")
print()


if os.path.exists(IMAGE_FILE):

    print("✓ Rider photograph: READY")

else:

    print("⚠ Rider photograph: NOT FOUND")


print()
print("✓ FOODWALA branding added to delivery box")
print("✓ No third-party delivery branding is intentionally added")
print()
print("Press CTRL+C to stop the server.")
print("=" * 60)
print()


webbrowser.open(url)


server.serve_forever()
