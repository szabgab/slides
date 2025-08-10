ENV["KEMAL_ENV"] = "test"
require "spec-kemal"
require "../src/set_header"

describe "Web Application" do
  it "renders /" do
    get "/"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{Hello Kemal})
  end

  it "renders /sitemap.xml" do
    get "/sitemap.xml"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "application/xml"
    response.body.should contain(%{<?xml version="1.0" encoding="UTF-8"?>})
  end
end
