require "kemal"

base_url = "https://code-maven.com"

get "/" do
  "Hello Kemal"
end

# source
get "/sitemap.xml" do |env|
  now = Time.utc
  now_str = now.to_s("%Y-%m-%d")
  env.response.content_type = "application/xml"
  xml = %{
     <?xml version="1.0" encoding="UTF-8"?>
     <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
     <url>
       <loc>#{base_url}/</loc>
       <lastmod>#{now_str}</lastmod>
     </url>
     </urlset>
  }
  xml
end

Kemal.run
