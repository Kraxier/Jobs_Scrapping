
# History or Timeline of What I currently Gonna do In "Project_Job_PH"
# 
# Timeline/History:

# August 2, 2025: 
r'''
    1. Learning to Investigate a Website First Before Touching  a code
        A. Understanding robot.txt (Done)
        B. Can i somehow Read the robot.txt or automate it in python? 
        C. Understanding Incognito and Browser Investigation in Website
        D. Learning the Dev Tools for Furthermore Investigation of the Website
'''

# August 1, 2025:
r'''
    1. Trying the BS4 and Request 
    2. Sticking to Playwright BS4 and REquest DIdn't work 
'''

# July 31, 2025 
r'''
I want to Learn and Analyze a Website in terms of Legality whether i can scrape it or not 

'''

# July 30, 2025
r'''

Learning the Gray Area of Web Scrapping and The Legality of Web Scrapping 
    1. Scrapping a Third Party Website : "Jora" Similar to the other Website like Jobstreet or Even Linkdiln because i had no idea how to navigate things in terms of legality
    2. 

Fixing the Github of Why i can't just upload things in there 
    "
    💡 Only push your code and essential files to GitHub. 
    Keep large or system-specific folders (like venv/) out using .gitignore. Use requirements.txt to share your environment.
    " 
    # Requirment of Learning Things in here 
'''

# July 29 2025
r'''
    Measurable: 
         I think in terms of History i will measure it but i lacking of Time for this 

        Phase: 
            1. Defining The Objective
            2. Target Website: "Jobstreet.ph"
            3. Careful Experimenting to not Get blocked


    Actionable: 
        # I'm currently Thinking that should i always write the SMARTER goal for every Project The Heck 
   1. Putting VENV :  python -m venv job_venv
   job_venv\Scripts\activate
   2. Installing the Playwright: 
        a. pip install playwright ✅ 2. Install Playwright
        b. playwright install # ✅ 3. Install the required browser binaries

    3. Defining What Things i should scrape: 
        Job title
        Company name
        Location (city, country, remote status)
        Posting date (e.g., “2 days ago”)
        Job description
        Employment type (full‑time, part‑time, contract)
        Salary range (if disclosed)
        Application URL/link
        Requirements/qualifications
        Tags/categories (e.g., Developer, Customer Service)
        On some platforms (e.g., Kalibrr, OnlineJobs.ph), you might also scrape:
        Resume snippets or skill matrices
        Assessment results (Kalibrr)
        Employer ratings or chat metadata (Bossjob)

    4. Goal Statement:
        To identify the most in-demand hard skills for Mechatronics or Automation Engineer roles in the Philippines by scraping job listings from relevant local job websites.
            A. Collecting job listings related to Mechatronics and Automation Engineering.
            B. Extracting job titles, descriptions, and particularly required skills.
            C. Analyzing the frequency of specific hard skills (e.g., PLC programming, AutoCAD, MATLAB).
            D. Producing insights about which skills are most frequently demanded, helping guide skill development or hiring strategy.
    You said:

    🧭 Process to Define and Achieve the Goal
    Here’s how you define and implement this project step-by-step:

    1. Clarify Your Research Questions (Define Goal Precisely)
        * Break your broad idea into concrete questions:
        * What are the most frequently mentioned hard skills in job listings for Mechatronics or Automation Engineers?
        * Which companies or industries are hiring the most for these roles?
        * How do skill demands vary between locations or job levels?

    2. Identify Target Websites for Scraping
        Find Philippine-based job portals that list engineering jobs:
        JobStreet Philippines (https://www.jobstreet.com.ph/)
        Indeed Philippines (https://ph.indeed.com/)
        Kalibrr (https://www.kalibrr.com/)
        LinkedIn Jobs (PH location filtered)

    3. Determine Data to Collect (Data Fields)
        For each job listing, collect:
            Job Title
            Company Name
            Location
            Posted Date
            Job Description
            Skills / Requirements (Key Field!)
            Employment Type (optional)
            Seniority Level (optional)

    4. Store the Data
        Store the scraped data in:
        A local CSV or JSON file for initial analysis
        Or a database like SQLite or MongoDB for scalability
     
    5. Clean and Parse the Data
    Focus especially on:
        Cleaning messy text
        Tokenizing and extracting hard skills from job descriptions
        Example: using keyword matching (e.g., ["PLC", "AutoCAD", "SCADA", "Python", "SolidWorks"]) or NLP

    6. Analyze the Data
        Use Pandas or SQL to count frequencies of skills
        Plot using Matplotlib or Seaborn

    7. Interpret & Visualize Results
        Create visual insights like:
        Bar chart of Top 10 In-Demand Skills
        Word cloud from job descriptions
        Time-series if you scrape over weeks/months

            
'''
r'''
July 28 2025:
    1. Starting to Create "history.py" to document what i'm going to do in Project_Job_PH
    2. Why i created this project? 
        * To Showcase my Skill in Playwright and overall Web Scrapping Skills 
        * For Personal use to Determine what is the current Demand on Job in the Philippines targeting the specific Career Path and their Hard Skills, Location, and information 
            - for Example "Mechatronics Engineer or Mechatronics Technician" The Average Salary, What hard Skills are Needed, What Location are Currently finding it? 
    3. My Implementation or my "Meta Proccess"
        * Jumping with an Uncofident in my Skills in terms of the Foundation or Core in "Playwright"
        * Implementing the Project Learning Approach in this Case
    4. Let's Define a SMARTER Goal:
        S Specific:
            Scrape a Mechatronics Areas
                1. Industrial Automation / Control Systems
                    Roles: Automation Engineer, PLC Programmer, Control Systems Engineer
                    Skills: PLCs (Siemens, Allen Bradley), SCADA, HMI, sensors, actuators, PID control
                    Industries: Manufacturing, oil & gas, automotive, packaging
                2. Robotics
                    Roles: Robotics Engineer, Robot Programmer, Maintenance Engineer
                    Skills: Kinematics, dynamics, ROS (Robot Operating System), microcontrollers, C++/Python
                    Industries: Automotive (e.g. assembly lines), medical robotics, aerospace

                3. IoT (Internet of Things)
                    Roles: IoT Developer, Embedded Systems Engineer
                    Skills: Arduino, Raspberry Pi, wireless communication (BLE, Zigbee, MQTT), sensors, cloud (AWS/ThingsBoard)
                    Industries: Smart homes, agriculture, logistics, healthcare

                4. Embedded Systems / Firmware Development
                    Roles: Embedded Systems Engineer, Firmware Developer
                    Skills: C/C++, microcontrollers (STM32, PIC), RTOS, circuit design
                    Industries: Consumer electronics, medical devices, automotive

                5. Product Design & Development
                    Roles: Mechatronics Designer, R&D Engineer
                    Skills: CAD (SolidWorks, Fusion 360), prototyping, 3D printing, simulations
                    Industries: Consumer goods, industrial tools, startups

                6. Maintenance & Field Engineering
                    Roles: Mechatronics Technician, Maintenance Engineer
                    Skills: Troubleshooting, diagnostics, machine maintenance, wiring, hands-on skills
                    Industries: Manufacturing, energy, rail, defense
                7. Artificial Intelligence + Mechatronics
                    Roles: AI Robotics Engineer, Machine Vision Engineer
                    Skills: Python, OpenCV, TensorFlow, AI/ML for robotics
                    Industries: Automation, autonomous vehicles, smart robotics
            What is the Current Demand 
        M Measurale
            Basing the History and the Work i will be Doing 
        A Actionable
        R Relevance
        T Timebound
        E 
        R  
'''
