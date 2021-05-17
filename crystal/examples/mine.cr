# Fetch all the Crystal projects from Github
# Create a cross reference with the authors
# Create a page with the pictures of the authors
# Collect all the contributors as well and show them as well
# Allow people to ask to be excluded (a config file in the mine or in their own GitHub repo?)

# CI systems: Travis-CI / GitHub Actions
require "http/client"

main

def main 
    token = read_config
    get_page(token)
end

def read_config
    config_file = "config.txt"
    line = File.read_lines(config_file).first
    #puts line
    return line
end

def get_page(token)
    url = "https://api.github.com/users/szabgab"
    response = HTTP::Client.get(url, headers: HTTP::Headers{"AUthentication" => "token #{token}"})
   
    puts response.status_code
    puts response.body
end