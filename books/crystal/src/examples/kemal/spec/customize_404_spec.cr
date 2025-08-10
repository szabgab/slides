ENV["KEMAL_ENV"] = "test"
require "spec-kemal"
require "../src/customize_404"

describe "Web Application" do
  it "renders /" do
    get "/"
    response.status_code.should eq 200
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{Hello World})
  end

  it "renders /other" do
    get "/other"
    response.status_code.should eq 404
    response.headers["Content-Type"].should eq "text/html"
    response.body.should contain(%{This is a customized 404 page.})
  end
end
