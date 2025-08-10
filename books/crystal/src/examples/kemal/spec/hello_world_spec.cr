ENV["KEMAL_ENV"] = "test"
require "spec-kemal"
require "../src/hello_world"

describe "Web Application" do
  it "renders /" do
    get "/"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain("Welcome to Kemal")
  end
end
