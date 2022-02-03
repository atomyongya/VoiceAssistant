import webbrowser
import os
import subprocess
import sys

def open_Application(application_Name):
    print(application_Name) 
    chrome_path = "/usr/bin/google-chrome %s"
    
    
    # To open webbrowser like chrome  
    if application_Name.strip() == "chrome":
        webbrowser.get(chrome_path).open("https://google.com/")
        
    # To open folder 
    elif application_Name.strip() == "folder" or application_Name.strip() == "file":
        # sudo chmod 775 Desktop -> If any problem occurs do this
        folder_path = "/home/atomyongya"
        open_folder = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([open_folder, folder_path])
        
    # To open youtube in default browser
    elif application_Name.strip() == "youtube":
        webbrowser.get(chrome_path).open("https://youtube.com/")
        
    # To open Canvas
    elif application_Name.strip() == "canvas":
        webbrowser.get(chrome_path).open("https://sso.wlv.ac.uk/adfs/ls/?SAMLRequest=fZJfT8IwFMXf%2FRRL3%2FeHDZA12xKEGElQF5g%2B%2BGK6rkBj12JvC%2Frt7YZGfJCkT7fnd889t82AtGKPp9bs5Iq9WwbG%2B2iFBNxf5MhqiRUBDliSlgE2FK%2Bn90scBxHea2UUVQKdIZcJAsC04UoibzHP0euIpDGraepPxgnxh2ky8usxpT6J4vS6HtV02MTIe2YaHJMj18KBAJYtJBgijStFcexH7iRVNMFJggejF%2BTNXQ4uiempnTF7wGEIoIKjOASEBvYtJM0GQgEh8qY%2FQ82UBNsyvWb6wCl7Wi1%2FYUrkgcAZL9SWy7CLjLzyexE3XDZcbi%2FvoD6JAN9VVemXj%2BsKFVnXB%2FfJdNFZOsfOiruY2lJjNQuoanu7OAvP1dnpBR%2Bcz2JeKsHpp3erdEvM%2F2MMgkFf4Y2%2F6aXYStgzyjecNW4hQqjjTDNiWI6cP0NhcTL9%2B1OKqy8%3D&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=Vl8J3SStGZrLOcb1ua%2BTy%2BBnSkdj%2BuRT2C7dGaHmT7uypdIyFeDDiK%2F%2FaJx5PDdhv17%2F%2BXL4uYS0C0HM55Nc3dd32Pqn4V5%2BPGM%2Fvs126iNGvQR6YOfUMyv6gZ6EJhuhybwqVy21qtnnucyE%2BzH%2FBqhUWRisyIM5p%2FwtkNdpt6LkZ%2BNuJnt4wlxwcUcQXFepoJhKTRQDkM4xY6D3a7BF7KGgm%2BIoXzSsM%2FLEWBEQp1FFUFvdy5zYV3jXxWEvhTtaubhSrz1T%2FXEJbXAtvV7sDJElqUKQziFbz2h2SYDlBBCzpnz91gHPmJFbtOaiiMCbKM8f85KW2DrbCbYwolPR5A%3D%3D&client-request-id=7954e9e4-9d07-44fc-6e0e-0080011000d6")
        
    # To open classroom
    elif application_Name.strip() == "classroom":
        webbrowser.get(chrome_path).open("https://classroom.google.com/c/Mzc4MjA5ODU2NDYy") 
    
    # To open brave browser
    # elif application_Name.strip() == "brave":
    #     brave_path = "/snap/bin/brave"
    #     webbrowser.get(brave_path).open()
        
    else:
        print("No such file exits")
        exit()
        
