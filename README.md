# PythonScraper

Python scraper for Njuškalo

# Installation
1. Clone repo 
2. Rename .env.example to .env and fill missing info (add info about Njuškalo link and ScraperAPI and Slack)
3. Install Docker and Docker Compose ([See instructions](https://docs.docker.com/engine/install/))
4. If you are not running containers as root (and you shouldn't) make sure that user has capatibilities to run Docker ([See instructions](https://docs.docker.com/engine/install/linux-postinstall/))
5. Run Docker Compose with: `docker-compose up --build -d`
