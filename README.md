# Web-presentation-tool
This is a self-hosted web tool to make a simple txt-based presentation in team. As a personal try-out for a side-project, this tool is free for downlard and use. Comments are welcome.

# File Structure:

The code is written in Python & Flask:

  - ./presentation_web.py
  
      the main web app, with two inline classes: 
      - File: the presentation file
      - Page: a single presentation page
  
  - ./txt
  
      the folder to host source prensetation file in plain txt format with a .txt suffix
  
  - ./static
  
      the folder to host background images, stylesheets and some static test pages
  
  - ./ templates
  
      the folder to host flask templates for file lists page, presentation page and test pages
  
# Usage:
  
  - to start the server:
    
        python presentation_web.py
      
      the app is using Flask default configuration, and you can access the app by http://localhost:5000
    
  - presentation files was located at ./txt folder. two sets of markup tags are used as convention.
  
    - '<' and '>': to identify the start and the end of a page
    - '+' and '-': to increase or decrease indents
    
    each markup tag should be in a standalone line in the file.
    
  - the hyperlink of the page number on top-left coner of each page is for reload the page (actually reload the file) and reflect your changes on the fly.
