import webbrowser
import os.path

while 1:
    year = input("Tell me the Batch of the class: ")
    year = str(year)

    if year == "n":
        break

    sub = input("Subject (only p,c,b,m): ")
    if sub == "m":
        sub = "Higher Math"
        sub_path = "higher_math"
        instructor_link = "https://i.postimg.cc/0NBqsr4C/25487446-2078715289017118-575051190755419269-o.jpg"
        instructor_name = 'Abhi Datta Tushar'
        instructor_edu = "Mechanical Engineering"
        instructor_ins = "BUET"

    elif sub == 'p':
        sub = "Physics"
        sub_path = "physics"
        instr = input("Instructor: (a for Apurbo, b for Apar) : ")
        if instr == 'a':
            instructor_link = "https://i.postimg.cc/43SLXTfR/Screenshot-2023-04-04-at-5-39-51-PM.png"
            instructor_name = 'Apurbo Opu'
            instructor_edu = "BSc. in EEE"
            instructor_ins = "RUET"
        if instr == 'b':
            instructor_link = "https://d1yreyj8btzg0t.cloudfront.net/images/special/ssc/2.%20Numeri%20Sattar%20Apar.png"
            instructor_name = 'Numeri Sattar Apar'
            instructor_edu = "Civil Engineering"
            instructor_ins = "BUET"

    elif sub == 'c':
        sub = "Chemistry"
        sub_path = "chemistry"
        instr = input("Instructor: (a for Sanjoy, b for Apar) : ")
        if instr == 'a':
            instructor_link = "https://i.postimg.cc/dVSqqWkd/Screenshot-2021-11-19-001737.png"
            instructor_name = 'Sanjoy Chakraborty'
            instructor_edu = "Mechanical Engineering"
            instructor_ins = "BUET"
        if instr == 'b':
            instructor_link = "https://i.postimg.cc/bvD9XVHS/H-Nazmus-Sakib-Full-Resolution.jpg"
            instructor_name = 'Md. Nazmus Sakib'
            instructor_edu = "Chemistry"
            instructor_ins = "DU"

    elif sub == 'b':
        sub = "Biology"
        sub_path = "biology"
        instructor_link = "https://i.postimg.cc/DychPq8r/Screenshot-2021-09-20-174533.png"
        instructor_name = 'Hasnat Shuvro'
        instructor_edu = "Shaheed Suhrawardy Medical"
        instructor_ins = "College (Undergraduate)"

    paper_path = ""
    paper = input("Paper (only 1,2): ")
    if paper == "1":
        paper = "1st"
        paper_path = "1"
    elif paper == "2":
        paper = "2nd"
        paper_path = "2"

    chap = input("Chapter Number: ")
    chap = str(chap)

    lec = input("Lecture Number: ")
    lec = str(lec)

    thumbnail = input("Thumbnail Link: ")

    link_hd = input("1080p Link :")
    hw = ""
    cmnt = input("Do you have HW? (y/n) :")
    if cmnt == 'y':
        hw = input("Enter HW Link: ")
        cmnt = ""

    elif cmnt == 'n':
        cmnts = "<!-- "
        cmnte = " -->"

    chap_path = f"{paper_path}{chap}"

    filepath = f"e:\ACS-Free-Classes\subjects\{sub_path}\chapters\{chap_path}\{lec}-{year}b.html"

    exp_var = os.path.expandvars(filepath)

    file = open(exp_var, "w")

    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Class {lec} - Chapter {chap} - {sub} {paper} Paper - ACS Free Classes</title>

        <link rel="stylesheet" href='/ACS-Free-Classes/style.css'>
        
        <!-- Favicon -->
        <link rel="apple-touch-icon" sizes="180x180" href="/ACS-Free-Classes/apple-touch-icon.png">
        <link rel="icon" type="image/png" sizes="32x32" href="/ACS-Free-Classes/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="16x16" href="/ACS-Free-Classes/favicon-16x16.png">
        <link rel="manifest" href="/ACS-Free-Classes/site.webmanifest">
    </head>
    <body>
        <header id="class-page-header">
            <div class="navbar">
                <nav>
                    <ul class="nav-links">
                        <li><a class="nav-link" href="/">Home</a></li>
                        <li>
                            <a class="nav-link">Subjects</a>

                            <ul class="dropdown">
                                <li><a href='/ACS-Free-Classes/subjects/higher_math'>Higher Mathematics</a></li>
                                <li><a href='/ACS-Free-Classes/subjects/physics'>Physics</a></li>
                                <li><a href='/ACS-Free-Classes/subjects/chemistry'>Higher Mathematics</a></li>
                                <li><a href='/ACS-Free-Classes/subjects/biology'>Higher Mathematics</a></li>

                            </ul>
                        </li>

                        <!-- <li><a href="\about.html">About</a></li>
                        <li><a href="\contact.html">Contact</a></li>
                        <li><a class="log-in" href="\log-in.html">Log in</a></li> -->
                    </ul>
                </nav>
                <a href="/ACS-Free-Classes/" class="nav-logo"><span class="blue-text">ACS</span> FREE Classes</a>
            </div>
        </header>

        <div id="ad-top-pc">
            <script type="text/javascript">
                atOptions = {{
                    'key' : '284e988ead40e28cb8386ae55f38b8aa',
                    'format' : 'iframe',
                    'height' : 90,
                    'width' : 728,
                    'params' : {{}}
                }};
                document.write('<scr' + 'ipt type="text/javascript" src="//www.highcpmcreativeformat.com/284e988ead40e28cb8386ae55f38b8aa/invoke.js"></scr' + 'ipt>');
            </script>
        </div>
        <div id="ad-top-tab">
            <script type="text/javascript">
                atOptions = {{
                    'key' : 'c5f5de5799a3718f28df249ba0ef828b',
                    'format' : 'iframe',
                    'height' : 60,
                    'width' : 468,
                    'params' : {{}}
                }};
                document.write('<scr' + 'ipt type="text/javascript" src="//www.highcpmcreativeformat.com/c5f5de5799a3718f28df249ba0ef828b/invoke.js"></scr' + 'ipt>');
            </script>
        </div>
        <div id="ad-top-mbl">
            <script type="text/javascript">
                atOptions = {{
                    'key' : '841da04b9bc26518cb6b69552edc255d',
                    'format' : 'iframe',
                    'height' : 50,
                    'width' : 320,
                    'params' : {{}}
                }};
                document.write('<scr' + 'ipt type="text/javascript" src="//www.highcpmcreativeformat.com/841da04b9bc26518cb6b69552edc255d/invoke.js"></scr' + 'ipt>');
            </script>
        </div>


        <section class="bb class-page-sec">
            <div class="class-grid">      
                <div class="player">
                    <script src="https://cdn.fluidplayer.com/v3/current/fluidplayer.min.js"></script>
                    <video id="video-id">
                        <source src="{link_hd}" title="1080p" type="video/mp4" />
                    <script>
                    var myFP = fluidPlayer(
                        'video-id',	{{
                            "layoutControls": {{
                                "controlBar": {{
                                    "autoHideTimeout": 3,
                                    "animated": true,
                                    "autoHide": true
                                }},
                                "htmlOnPauseBlock": {{
                                    "html": null,
                                    "height": null,
                                    "width": null
                                }},
                                "autoPlay": true,
                                "mute": false,
                                "allowTheatre": false,
                                "playPauseAnimation": true,
                                "playbackRateEnabled": true,
                                "allowDownload": false,
                                "playButtonShowing": true,
                                "fillToContainer": true,
                                "posterImage": "{thumbnail}",
                                "primaryColor": "#53b3f3"
                            }},
                        "vastOptions": {{
                            "adList": [
                                {{
                                    "roll": "preRoll",
                                    "vastTag": "",
                                    "adText": ""
                                }},
                                {{
                                    "roll": "midRoll",
                                    "vastTag": "",
                                    "adText": ""
                                }},
                                {{
                                    "roll": "postRoll",
                                    "vastTag": "",
                                    "adText": ""
                                }}
                            ],
                            "adCTAText": false,
                            "adCTATextPosition": ""
                        }}
                        }});
                    </script>
                </div>       
                <!-- ####### Video Description ######## -->
                <p id="Video_Description" class="bangla">
                    {sub} {paper} Paper || Chapter {chap} || Lec {lec}
                </p>

                <div id="instructor">
                    <h4>Instructor</h4>
                    <img src="{instructor_link}" alt="{instructor_name}">
                    <span id="name">{instructor_name}</span>
                    <span id="qua">{instructor_edu}<br>{instructor_ins}</span>
                </div>  
                {cmnts}<div id="hw">
                    <button class="card" onclick="window.location.href='https://drive.google.com/file/d/{hw}';" target="_blank">HW</button>
                </div>{cmnte}
            </div>
            
        </section>




        <footer class="footer">
            <a href="/ACS-Free-Classes/" class="nav-logo"><span class="blue-text">ACS</span> FREE Classes</a>
        </footer>



        <script src="https://cdn.fluidplayer.com/v3/current/fluidplayer.min.js"></script>
        <script>
            var player = fluidPlayer('v-player');
        </script>
        <script type='text/javascript' src='//pl21271297.toprevenuegate.com/2e/20/f7/2e20f7373c348e0a2ed19056f3d10996.js'></script>
    </body>
    </html>
    """

    file.write(html_content)
    file.close()

print("well done MOUIN. ALHAMDULILLAH")
