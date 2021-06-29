# CI systems: Travis-CI / GitHub Actions
require "http/client"
require "json"

main

def main
  token = read_config
  # get_page(token)
  search(token)
end

def read_config
  config_file = "config.txt"
  line = File.read_lines(config_file).first
  # puts line
  return line
end

def get_page(token)
  url = "https://api.github.com/users/szabgab"
  response = HTTP::Client.get(url, headers: HTTP::Headers{"AUthentication" => "token #{token}"})

  puts response.status_code
  puts response.body
end

def search(token)
  per_page = 3 # max is 100
  query = "language:crystal"
  page = 1
  sort = "updated" # stars, forks, help-wanted-issues, updated
  order = "desc"
  url = "https://api.github.com/search/repositories?q=#{query}&per_page=#{per_page}&page=#{page}&sort=#{sort}&order=#{order}"
  response = HTTP::Client.get(url, headers: HTTP::Headers{"AUthentication" => "token #{token}"})
  # puts typeof(response) # HTTP::Client::Response
  # puts typeof(response.body) # string
  # data = Hash(String, Any).from_json(response.body)
  json_text = response.body
  puts json_text
  # data = Hash(String, Bool | Array(Hash) | Int32 | Nil).from_json(json_text)
  # puts typeof(data)
  # puts data.keys

  # puts response.status_code
  # puts response.body
end
